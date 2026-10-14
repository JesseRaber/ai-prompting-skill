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
import os
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


def check(condition, *detail):
    """Package validation must run even when Python assertions are disabled."""
    if not condition:
        raise ValueError('Package check failed: %r' % (detail or ('',),))


def refuse_linked_path(path):
    """Reject symlinks, junctions and reparse points in a repository path."""
    path = Path(path)
    try:
        parts = path.relative_to(REPO).parts
    except ValueError:
        raise ValueError('Package source is outside repository: %s' % path)
    current = REPO
    if current.is_symlink() or getattr(current.lstat(), 'st_file_attributes', 0) & 0x400:
        raise ValueError('Refusing linked repository root: %s' % current)
    for part in parts:
        current = current / part
        if current.is_symlink() or getattr(current.lstat(), 'st_file_attributes', 0) & 0x400:
            raise ValueError('Refusing linked package source: %s' % current)


def repo_bytes(rel):
    path = REPO / rel
    refuse_linked_path(path)
    return path.read_bytes()


def frontmatter(data):
    """Return the YAML frontmatter and body from a skill Markdown file."""
    text = data.decode('utf-8')
    if not text.startswith('---\n'):
        raise ValueError('SKILL.md has no YAML frontmatter')
    header, body = text[4:].split('---\n', 1)
    return header, body


def source_files():
    files = {}
    refuse_linked_path(SKILL)
    def walk_error(error):
        raise error

    for root, dirs, names in os.walk(SKILL, followlinks=False, onerror=walk_error):
        base = Path(root)
        for name in dirs + names:
            refuse_linked_path(base / name)
        dirs[:] = [name for name in dirs if name != '__pycache__']
        for name in names:
            p = base / name
            if p.suffix == '.pyc':
                continue
            check(p.is_file(), 'not a regular skill file', str(p))
            data = p.read_bytes()
            check(b'\r' not in data, 'CR byte in skill source', str(p))
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
    repo = repo_bytes
    skill = {ROOT + n: d for n, d in files.items()}
    packages = {}

    universal = dict(skill)
    universal[ROOT + 'LICENSE.txt'] = repo('LICENSE')
    universal[ROOT + 'INSTALL.md'] = repo('packaging/INSTALL-universal.md')
    packages['UNIVERSAL-skill'] = (universal, True)

    for flavor, metadata, guide in [('claude-code-plugin', '.claude-plugin', 'INSTALL-claude-code.md'),
                                    ('codex-chatgpt-plugin', '.codex-plugin', 'INSTALL-codex-chatgpt.md')]:
        items = {ROOT + 'skills/' + n: d for n, d in skill.items()}
        refuse_linked_path(REPO / metadata)
        for p in sorted((REPO / metadata).glob('*.json')):
            items[ROOT + metadata + '/' + p.name] = repo(p.relative_to(REPO))
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
            info.create_system = 3
            info.external_attr = 0o40755 << 16 | 0x10
            z.writestr(info, b'')
        for n in names:
            info = zipfile.ZipInfo(n, date_time=STAMP)
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, items[n])
    return dirs


def verify(archive, flavor, items, dirs, files):
    with zipfile.ZipFile(archive) as z:
        check(z.testzip() is None, 'archive CRC', flavor)
        listed = z.namelist()
        check(len(listed) == len(set(listed)), 'duplicate members', flavor)
        check(set(listed) == set(items) | dirs, 'member mismatch', flavor,
              sorted(set(listed) ^ (set(items) | dirs)))
        for name, data in items.items():
            check(z.read(name) == data, 'byte mismatch', flavor, name)
        check(not any('__pycache__' in n or n.endswith('.pyc') for n in listed), 'cache in archive', flavor)
        skill_md = ROOT + ('skills/' + NAME + '/' if flavor.endswith('-plugin') else '') + 'SKILL.md'
        check(skill_md in listed, 'SKILL.md missing', flavor)
        if flavor == 'UNIVERSAL-skill':
            check(not any('plugin.json' in n for n in listed), 'plugin manifest in universal archive')
            check(not any(n.endswith('/SKILL.md') and n != skill_md for n in listed), 'extra skill', flavor)
        if flavor == 'gemini-apps-only':
            check(not any(n.endswith(('.ps1', '.yaml', '.yml', '.py')) for n in listed), 'unsupported file', flavor)
        if flavor == 'opal-only':
            check(not any(n.endswith('/') for n in listed), 'folder entry', flavor)
            check(all(n.endswith('.md') for n in listed), 'non-Markdown file', flavor)
            check(all(b'\r' not in z.read(n) for n in listed), 'CR byte', flavor)
            check(all(len(z.read(n)) < OPAL_MAX_FILE_BYTES for n in listed), 'file too large', flavor)
            check(all(n == ROOT + 'SKILL.md' or re.fullmatch(re.escape(ROOT) + r'references/[^/]+\.md', n)
                      for n in listed), 'unexpected path', flavor)
            front = z.read(ROOT + 'SKILL.md').decode('utf-8').split('---\n')[1]
            check([l.split(':')[0] for l in front.splitlines()] == ['name', 'description'],
                  'Opal frontmatter', flavor)
            # Every reference file must reach Opal.
            expected = {ROOT + n for n in files if n.startswith('references/')}
            check(expected <= set(listed), 'missing references', flavor, sorted(expected - set(listed)))
        if flavor == 'microsoft-copilot-agent-only':
            expected = {ROOT + n for n in files if n == 'SKILL.md' or n.startswith('references/')}
            check(set(items) == expected | {ROOT + 'INSTALL.md'}, 'member mismatch', flavor)
            check(all(n.endswith('.md') for n in items), 'non-Markdown file', flavor)
            check(not any(n.endswith(('.ps1', '.py', '.yaml', '.yml')) for n in listed),
                  'unsupported file', flavor)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output', nargs='?')
    parser.add_argument('--status', default='local candidate, not published')
    parser.add_argument('--describe', action='store_true')
    args = parser.parse_args()
    version = re.search(r'^  version: "([^"]+)"', repo_bytes('skills/' + NAME + '/SKILL.md').decode('utf-8'), re.M)[1]
    if args.describe:
        print(json.dumps({'version': version, 'skill': NAME}))
        return
    if not args.output:
        parser.error('output directory is required unless --describe is used')
    output = Path(args.output).resolve()
    for name in ('.codex-plugin', '.claude-plugin'):
        check(json.loads(repo_bytes(name + '/plugin.json'))['version'] == version,
              'plugin version mismatch', name)
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
