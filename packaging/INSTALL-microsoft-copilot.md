# Microsoft Copilot agent package

Version 1.0.8. This ZIP contains `ai-prompting/SKILL.md`, all Markdown files in `ai-prompting/references/`, and this guide. It is prepared for a Microsoft Copilot agent's knowledge or file upload. An owner-reported 2026-10-14 Copilot Agent test loaded v1.0.8 from its installed skill catalog after this dedicated ZIP was selected. The remote package bytes and future-session persistence were not independently verified.

Upload this ZIP to the intended Copilot agent or workspace if that surface accepts ZIPs. If it requires individual files, upload `SKILL.md` and the reference files while preserving their names. For an agent performing the install, supply the ZIP's absolute path and require an existence check before it replaces any installed copy. Do not claim the agent can open a local `C:\` path unless it has a tested bridge to that PC.

Give the agent this instruction:

> When writing a prompt for another AI agent or reviewing its reply, read `SKILL.md` and report `Loaded AI Prompting v1.0.8`. Apply Part 1. For Part 2, use the reference for the **agent receiving the prompt**. If none is named, use Part 1 only. State which files you actually read and which were unavailable.

Smoke test in a fresh Copilot conversation: ask it to write a short prompt for Microsoft Opal that points to a saved instruction file. Record whether it reports v1.0.8, uses `references/opal.md`, and keeps the prompt short. A text reply alone proves only that conversation's behavior; record the upload path and what files Copilot could access.
