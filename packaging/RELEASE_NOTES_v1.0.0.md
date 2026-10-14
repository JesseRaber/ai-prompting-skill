# ai-agent-prompting 1.0.0

## Which ZIP do I use?

| Your AI app | Download |
|---|---|
| **Almost everything**: Claude app skill upload, ChatGPT/Codex standalone skills, Grok, Copilot, local models, any skills folder | `…-UNIVERSAL-skill.zip` |
| Claude Code `/plugin install` (not the Claude app uploader) | `…-claude-code-plugin.zip` |
| Codex / ChatGPT plugin marketplace | `…-codex-chatgpt-plugin.zip` |
| Gemini Apps skill upload | `…-gemini-apps-only.zip` |
| Opal skill import | `…-opal-only.zip` |

Coding agents that install from GitHub (Antigravity, Claude Code, Codex CLI) can use the repository directly.

## What's in it

- **Part 1 rules for every agent:** reachability, input limits, prompt shape, the short-pointer prompt, keeping long runs alive, importing and spot-checking replies.
- **Opal** (`references/opal.md`): how Opal finds, reads and saves files, its limits, a prompt recipe, and the Opal skill package format. Corrects the earlier note that Opal can only save to its own folder: with an approved exact path it uploads into the project folder.
- **Manus** (`references/manus.md` plus 30 files): the full manus-prompt-engineering method, byte-identical. Templates are now `references/TEMPLATE_*.md` and the example `references/EXAMPLE_*.md`.
- **Starter notes** for Copilot, Gemini, Antigravity, Grok, Meta AI, ChatGPT/Codex, Claude and local models, plus `multi-model-review.md` and `agent-template.md`.

## Replaces

The separate `manus-prompt-engineering` skill and the single-file `ai-agent-prompting` skill. Retire `manus-prompt-engineering` after this one is installed and a Manus prompt test passes.

## Not yet verified

Upload tests on each host. The Opal package holds 43 files; Opal's limit on file count or total size is unknown.
