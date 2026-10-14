# AI Prompting

Canonical source for the `ai-prompting` Agent Skill and its Claude and OpenAI plugin packages. The repository is named `ai-prompting-skill`; the skill that loads on each host is `ai-prompting`.

One skill for handing work to other AI agents and reviewing what comes back: shared prompt rules, a short-pointer pattern for agents with input limits, the full Opal and Manus methods, and notes for Copilot, Gemini, Antigravity, Grok, Meta AI, ChatGPT/Codex, Claude and local models.

## Version

Current version: `1.0.8`. See `CHANGELOG.md`.

Report as: **Loaded AI Prompting v1.0.8**.

## Install

Prebuilt packages are attached to each [release](https://github.com/JesseRaber/ai-prompting-skill/releases). **Which ZIP do I use?**

| Your AI app | Download |
|---|---|
| **Almost everything**: Claude app skill upload, ChatGPT/Codex standalone skills, Grok, local models, any skills folder | `…-UNIVERSAL-skill.zip` |
| Claude Code `/plugin install` (not the Claude app uploader) | `…-claude-code-plugin.zip` |
| Codex / ChatGPT plugin marketplace | `…-codex-chatgpt-plugin.zip` |
| Gemini Apps skill upload | `…-gemini-apps-only.zip` |
| Opal skill import | `…-opal-only.zip` |
| Microsoft Copilot agent knowledge upload | `…-microsoft-copilot-agent-only.zip` |

Coding agents that install from GitHub (Antigravity, Claude Code, Codex CLI) can use the repository directly.

Host-specific packages leave out what that host rejects:

- `-gemini-apps-only`: no `agents/openai.yaml` (the Gemini uploader rejects `.yaml`).
- `-opal-only`: `SKILL.md` (name and description only in the header) plus `references/*.md`, no folder entries. That is the only layout Opal imports.
- `-microsoft-copilot-agent-only`: Markdown skill and references plus a Copilot install guide. The Copilot Agent upload and fresh v1.0.8 skill-catalog read were owner-reported on 2026-10-14; remote package bytes and future-session persistence remain unverified.

The skill has no scripts, so every package carries the same instructions.

### Claude Code

```text
/plugin marketplace add JesseRaber/ai-prompting-skill
/plugin install ai-prompting@ai-prompting-skill
```

### Other hosts

Copy or upload only `skills/ai-prompting/`, keeping `SKILL.md` and `references/` together. Hosts without a skill loader: paste this into their instructions.

> When you write a prompt or handoff for another AI agent, or review what one
> sent back, follow `SKILL.md`. Report as: Loaded AI Prompting v1.0.8.
> Apply Part 1, then read the reference for the agent receiving the prompt.
> If none is named, use Part 1 only. Paths are relative to the skill folder.

## Repository layout

```text
.codex-plugin/plugin.json        OpenAI plugin manifest
.claude-plugin/                  Claude plugin manifest and marketplace catalog
skills/ai-prompting/
  SKILL.md                       shared rules for every agent + routing table
  agents/openai.yaml             OpenAI display metadata
  references/opal.md             Microsoft Opal
  references/manus.md            Manus method (from manus-prompt-engineering)
  references/<UPPERCASE>.md      Manus references, templates (TEMPLATE_*) and example (EXAMPLE_*)
  references/copilot.md, gemini.md, antigravity.md, grok.md, meta-ai.md,
             chatgpt-codex.md, claude.md, local-models.md
  references/multi-model-review.md  one prompt to several models
  references/agent-template.md   start a file for a new agent
packaging/                       packager, install guides, release notes, Manus source manifest
tests/                           package and content checks
.github/workflows/               PR validation and tagged release
```

Every reference sits directly in `references/` because Opal imports nothing deeper.

## Adding an agent

Copy `references/agent-template.md` to `references/<agent>.md`, fill it from real runs, add a row to the Part 2 table in `SKILL.md`, and bump the version.

## Validation and releases

Every pull request runs the pinned OpenAI skill and plugin validators, the package tests (Manus files byte-identical to their source manifest, every path resolves, flat layout, versions agree) and a full package build. Tagged releases repeat this, build all six archives, re-read and byte-check them, and publish SHA-256 checksums.

The tag must match the versions in `SKILL.md`, `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json`. Tag only the reviewed merge commit after the owner approves the exact version and tag action. A pushed tag creates a **draft** release; verify its downloaded assets and checksums before requesting separate publication approval. Use **Actions → Release → Run workflow** to build artifacts without creating a release.

## Authority rule

If two copies disagree, this repository is current. A release archive, chat upload or host-local cache is not.
