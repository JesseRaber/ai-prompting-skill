# Install - AI Prompting (Claude Code plugin)

**Not for the Claude app skill uploader.** It rejects plugin manifests. For the Claude app, Grok, ChatGPT standalone skills and most other hosts, use `…-UNIVERSAL-skill.zip`. Microsoft Copilot has a dedicated candidate package.

## From the repository

```text
/plugin marketplace add JesseRaber/ai-prompting-skill
/plugin install ai-prompting@ai-prompting-skill
```

## From this ZIP

Extract it, then add the extracted `ai-prompting/` folder as a local marketplace (`/plugin marketplace add <path>`) and install `ai-prompting` from it. Keep the extracted structure intact.

Smoke test: ask for a short Opal pointer prompt. A loaded skill reports **Loaded AI Prompting v1.0.8**.
