"""Build and verify the install archives. Never tags, uploads or installs.

Usage: python packaging/build_packages.py NEW_OUTPUT_DIRECTORY [--status TEXT]

Used by .github/workflows/release.yml, PR CI and local candidate builds. The
output directory must not exist. Every archive is rebuilt from source,
re-read and byte-compared before SHA256SUMS.txt is written.

Package names say who each archive is for (same scheme as
JesseRaber/multi-agent-folder-cleanup v1.5.0):
  UNIVERSAL-skill         skill folder for every skill uploader or skills folder
  claude-code-plugin      Claude Code /plugin layout (not the Claude app uploader)
  codex-chatgpt-plugin    OpenAI Codex / ChatGPT plugin layout
  gemini-apps-only        Gemini Apps uploader (rejects .yaml)
  opal-only               Opal importer (SKILL.md + references/*.md only)
  microsoft-copilot-agent-only  Copilot agent knowledge: Markdown skill and references
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile

REPO = Path(__file__).resolve().parents[1]
NAME = 'ai-prompting'
SKILL = REPO / 'skills' / NAME
ROOT = NAME + '/'
STAMP = (2026, 1, 1, 0, 0, 0)
# Opal rejected single files somewhere between about 48 and 79 KB (upload tests,
# 2026-10-03). Stay under the lower bound.
OPAL_MAX_FILE_BYTES = 48_000


def digest(data):
    return hashlib.sha256(data).hexdigest()


def source_files():
    files = {}
    for p in sorted(SKILL.rglob('*')):
        if '__pycache__' in p.parts or p.suffix == '.pyc' or not p.is_file():
            continue
        if p.is_symlink():
            raise ValueError('Refusing linked package source')
        data = p.read_bytes()
        if b'\r' in data:
            raise ValueError(f'CR byte in {p}; source must use LF line endings')
        files[p.relative_to(SKILL).as_posix()] = data
    return files


def opal_skill_md(data):
    """Opal accepts only single-line name and description in the frontmatter."""
    text = data.decode('utf-8')
    _, front, body = text.split('---\n', 2)
    keep = [line for line in front.splitlines() if line.startswith(('name:', 'description:'))]
    if len(keep) != 2:
        raise ValueError('SKILL.md frontmatter needs single-line name and description')
    return ('---\n' + '\n'.join(keep) + '\n---\n' + body).encode('utf-8')


def build_packages(files):
    repo = lambda rel: (REPO / rel).read_bytes()
    skill = {ROOT + n: d for n, d in files.items()}
    packages = {}

    universal = dict(skill)
    universal[ROOT + 'LICENSE.txt'] = repo('LICENSE')
    universal[ROOT + 'INSTALL.md'] = repo('packaging/INSTALL-universal.md')
    packages['UNIVERSAL-skill'] = (universal, True)

    for flavor, metadata, guide in [('claude-code-plugin', '.claude-plugin', 'INSTALL-claude-code.md'),
                                    ('codex-chatgpt-plugin', '.codex-plugin', 'INSTALL-codex-chatgpt.md')]:
        items = {ROOT + 'skills/' + n: d for n, d in skill.items()}
        for p in sorted((REPO / metadata).glob('*.json')):
            items[ROOT + metadata + '/' + p.name] = p.read_bytes()
        for name in ('LICENSE', 'README.md', 'CHANGELOG.md'):
            items[ROOT + name] = repo(name)
        items[ROOT + 'INSTALL.md'] = repo('packaging/' + guide)
        packages[flavor] = (items, True)

    gemini = {ROOT + n: d for n, d in files.items()
              if not n.startswith('agents/') and not n.endswith(('.ps1', '.yaml', '.yml'))}
    gemini[ROOT + 'LICENSE.txt'] = repo('LICENSE')
    packages['gemini-apps-only'] = (gemini, True)

    # Opal: same layout as an Opal export - no folder entries, Markdown only.
    opal = {ROOT + 'SKILL.md': opal_skill_md(files['SKILL.md'])}
    for n, d in files.items():
        if n.startswith('references/') and n.count('/') == 1 and n.endswith('.md'):
            opal[ROOT + n] = d
    packages['opal-only'] = (opal, False)
    copilot = {ROOT + n: d for n, d in files.items()
               if n == 'SKILL.md' or (n.startswith('references/') and n.endswith('.md'))}
    copilot[ROOT + 'INSTALL.md'] = repo('packaging/INSTALL-microsoft-copilot.md')
    packages['microsoft-copilot-agent-only'] = (copilot, True)
    return packages


def write_zip(archive, items, folder_entries):
    names = sorted(items)
    dirs = set()
    if folder_entries:
        for n in names:
            parts = n.split('/')[:-1]
            for i in range(1, len(parts) + 1):
                dirs.add('/'.join(parts[:i]) + '/')
    with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED) as z:
        for d in sorted(dirs):
            info = zipfile.ZipInfo(d, date_time=STAMP)
            info.external_attr = 0o40755 << 16 | 0x10
            z.writestr(info, b'')
        for n in names:
            info = zipfile.ZipInfo(n, date_time=STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, items[n])
    return dirs


def verify(archive, flavor, items, dirs, files):
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        listed = z.namelist()
        assert len(listed) == len(set(listed)), 'duplicate members'
        assert set(listed) == set(items) | dirs, sorted(set(listed) ^ (set(items) | dirs))
        for name, data in items.items():
            assert z.read(name) == data, name
        assert not any('__pycache__' in n or n.endswith('.pyc') for n in listed)
        skill_md = ROOT + ('skills/' + NAME + '/' if flavor.endswith('-plugin') else '') + 'SKILL.md'
        assert skill_md in listed, (flavor, 'SKILL.md missing')
        if flavor == 'UNIVERSAL-skill':
            assert not any('plugin.json' in n for n in listed), 'Claude uploader rejects plugin manifests'
            assert not any(n.endswith('/SKILL.md') and n != skill_md for n in listed)
        if flavor == 'gemini-apps-only':
            assert not any(n.endswith(('.ps1', '.yaml', '.yml', '.py')) for n in listed)
        if flavor == 'opal-only':
            assert not any(n.endswith('/') for n in listed)
            assert all(n.endswith('.md') for n in listed)
            assert all(b'\r' not in z.read(n) for n in listed)
            assert all(len(z.read(n)) < OPAL_MAX_FILE_BYTES for n in listed), 'file too large for Opal'
            assert all(n == ROOT + 'SKILL.md' or re.fullmatch(re.escape(ROOT) + r'references/[^/]+\.md', n)
                       for n in listed)
            front = z.read(ROOT + 'SKILL.md').decode('utf-8').split('---\n')[1]
            assert [l.split(':')[0] for l in front.splitlines()] == ['name', 'description']
            # Every reference file must reach Opal.
            expected = {ROOT + n for n in files if n.startswith('references/')}
            assert expected <= set(listed), sorted(expected - set(listed))
        if flavor == 'microsoft-copilot-agent-only':
            expected = {ROOT + n for n in files if n == 'SKILL.md' or n.startswith('references/')}
            assert set(items) == expected | {ROOT + 'INSTALL.md'}
            assert all(n.endswith('.md') for n in items)
            assert not any(n.endswith(('.ps1', '.py', '.yaml', '.yml')) for n in listed)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output')
    parser.add_argument('--status', default='local candidate, not published')
    args = parser.parse_args()
    output = Path(args.output).resolve()
    version = re.search(r'^  version: "([^"]+)"', (SKILL / 'SKILL.md').read_text(encoding='utf-8'), re.M)[1]
    for name in ('.codex-plugin', '.claude-plugin'):
        assert json.loads((REPO / name / 'plugin.json').read_text())['version'] == version
    files = source_files()
    output.mkdir(parents=True, exist_ok=False)
    evidence = {'version': version, 'status': args.status,
                'source_files': {n: digest(b) for n, b in files.items()}, 'packages': {}}
    for flavor, (items, folder_entries) in build_packages(files).items():
        archive = output / f'{NAME}-{version}-{flavor}.zip'
        dirs = write_zip(archive, items, folder_entries)
        verify(archive, flavor, items, dirs, files)
        evidence['packages'][archive.name] = {'sha256': digest(archive.read_bytes()), 'files': len(items),
                                              'byte_verified': True}
    with (output / 'SHA256SUMS.txt').open('x', encoding='utf-8', newline='\n') as f:
        f.write(''.join(row['sha256'] + '  ' + name + '\n' for name, row in sorted(evidence['packages'].items())))
    with (output / 'BUILD_EVIDENCE.json').open('x', encoding='utf-8') as f:
        json.dump(evidence, f, indent=2)
    print(json.dumps({'version': version, 'packages': evidence['packages']}, indent=2))


if __name__ == '__main__':
    main()
