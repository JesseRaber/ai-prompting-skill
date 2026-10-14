# Install - AI Prompting

Universal skill package: the `ai-prompting/` skill folder, with this guide and the license inside it. Use it for every skill uploader or skills folder unless the table below names a host-specific package.

| Your AI app | Download |
|---|---|
| **Almost everything**: Claude app skill upload, ChatGPT/Codex standalone skills, Grok, local models, any skills folder | `…-UNIVERSAL-skill.zip` |
| Claude Code `/plugin install` (not the Claude app uploader) | `…-claude-code-plugin.zip` |
| Codex / ChatGPT plugin marketplace | `…-codex-chatgpt-plugin.zip` |
| Gemini Apps skill upload | `…-gemini-apps-only.zip` |
| Opal skill import | `…-opal-only.zip` |
| Microsoft Copilot agent knowledge upload | `…-microsoft-copilot-agent-only.zip` |

Coding agents that install from GitHub (Antigravity, Claude Code, Codex CLI) can use the repository directly.

The folder `ai-prompting/` **is** the skill. Keep `SKILL.md`, `agents/` and `references/` together.

For an owner-authorized ZIP install, supply the absolute source path, confirm archive existence/integrity, preserve a rollback copy and validate extraction before replacement. Existence is not authorization. Never delete the existing copy first; missing/invalid source → stop replacement and report.

When a host has no native skill loader, paste this into its instructions:

> When you write a prompt or handoff for another AI agent, or review what one
> sent back, follow `SKILL.md`. Report as: Loaded AI Prompting v1.0.8.
> Apply Part 1, then read the reference for the agent receiving the prompt.
> If none is named, use Part 1 only. Paths are relative to the skill folder.

## Claude app (skill upload)

Upload this ZIP as it is: Settings -> Capabilities -> Skills -> Upload skill. For Claude Code use `-claude-code-plugin.zip` instead; the Claude app uploader rejects plugin files.

## ChatGPT and Codex

ChatGPT desktop, Codex CLI and the Codex IDE extension support standalone skills: install `ai-prompting/` through the Skills interface or skills directory. Custom GPT without skills: upload `SKILL.md` and the `references/` files you need as knowledge, and paste the block above.

## Grok and other chats

Upload the ZIP or the folder to the conversation or workspace and paste the block above.

## Local models

Point the system prompt or context loader at `ai-prompting/SKILL.md`. Load a reference file only when the skill routes to it.

## Smoke test

> Write a short prompt for Opal that points it to a saved instruction file.

A loaded skill reports **Loaded AI Prompting v1.0.8** and returns a pointer prompt of a few sentences.

## Verify what you downloaded

```bash
sha256sum -c SHA256SUMS.txt          # macOS: shasum -a 256 -c SHA256SUMS.txt
```

```powershell
Get-FileHash .\ai-prompting-*.zip -Algorithm SHA256
```

## Authority

If a downloaded copy disagrees with <https://github.com/JesseRaber/ai-prompting-skill>, the repository is current. MIT licensed - see `LICENSE.txt`.
