# Claude

Another Claude conversation, a Claude project, Claude Cowork, or Claude Code, given a handoff from this one.

Evidence base: Claude session logs and handoffs across Jesse's projects, 2026-08 to 2026-10, and a linked-session preference review (Incoming, 2026-10-03, session c641db92). Historical bullets below with no individual locator are retained as historical reports, not verified current/default behavior or comparative guarantees. Recheck only relevant claims before reliance; missing citation does not establish falsity.

## How it reaches files and tools
Which Claude host matters more than the model name. Recheck this table when host features change.

| Host | Owner's PC files | Shell | Notes |
|---|---|---|---|
| claude.ai chat/project, not linked | Attachments, project knowledge, connectors only | Cloud container | Ask for attachments instead of giving a `C:\` path |
| claude.ai cloud session linked to the desktop app | Connected folders (mounted under `$HOME/mnt/<folder>`) | Linux VM on the PC, per-call time limit | Give the Windows path; it maps it. Deleting needs an owner permission prompt |
| Claude Code on the PC | Working directory and what the CLI can reach | Native shell | Reads `CLAUDE.md`; its settings decide permissions (documented, not tested here) |
| claude.ai with Google Drive connector (P-057) | Reported Drive files by id; create/trash route | Cloud container | Historical GaugeWorx report 2026-10-08: conversion stopped on hash mismatch with checkpoint only. Checkpoint before replacement; apply destination authority/concurrency controls or stage. The previously described read_file_content schema lacks a pinned source/version here; Markdown readability and current operations remain unverified |

- **Observed 2026-10-03 (linked session):** the owner's Windows path resolved; a ~2,900-word pasted prompt arrived as an attachment file and was read fully; shell calls were capped at a few minutes each, so long jobs need staging.
- **Observed:** cloud container and PC folder are separate stores; a file saved only in the container never reaches the owner.
- **Historical report (P-040, 2026-10-08/09):** linked-PC shell reads returned "Invalid argument" for some tool-written files and could not mount a Drive virtual disk; staging by path reportedly worked. Source lead: AI Agent Prompting PROJECT_ROADMAP.md P-040 and Deliverables/GAUGEWORX_PROJECT_SCAN_2026-10-09.md; cause and current behavior unverified. Do not call an inaccessible file absent; stage authorized inputs or report the gap.
- **Observed:** installed skills appear in the session; a skill-save card saves a single `SKILL.md` only, so multi-file skills ship as a zip.

## Writing the prompt
- Put first: mission, task mode, root path. Order after that matters little.
- **Name the output literally:** "plain Markdown file at <path>", "reply in chat only", or "publish an artifact/doc". Unstated, the Claude app tends to publish an artifact or doc.
- A `HANDOFF.md` (goal, inputs with paths and hashes, rules, PASS/FAIL acceptance checks, deliverables) plus a short pointer is good for reuse and provenance; for linked sessions it is optional, not required.
- Tell it what to do if an input is unreachable: "say exactly what's missing, finish unaffected sections, ask one question".
- Name installed skills and canonical files it must not change.
- For work in the PC shell, ask for staged steps (inventory, read, write) rather than one long script.
- **Correction pass (P-014):** first answers can overstate (observed 2026-08-25, Local AI Model Research: "the only answer", a tool "reaches MCP only through a proxy" — both wrong). A follow-up asking "withdraw or narrow anything you overstated; mark what is documented vs. inferred" produced the most accurate reply in that set. Use it on any recommendation that will drive a decision.

Compact block:

```text
Mission: <one sentence>
Mode: answer | review | plan | implement | test; read-only logging follows owner scope/project rules; explicit no-writes → chat checkpoint (P-041)
Root: <Windows path as the owner sees it>
Read first: <3-6 paths>
May change: <paths>   Must not touch: <paths>
External actions: none | <named, scoped>
Deliverable: <form> at <path>, <length cap>; no artifact unless stated
Done when: <checks it can run> / <checks the owner must run>
```

## Reviewing what it sends back
- Ask for a build or review report with each acceptance check marked PASS/FAIL and the evidence beside it.
- Ask it to end with: inspected / not inspected / saved path / canonical files changed (yes/no) / next action.
- Confirm the file exists on the PC path, not only in the cloud container, before importing.
- **Point, don't paste (P-045):** with folder access, read the other agent's output in place and save a dated review at an authorized destination; paste-import when no folder access. Historical lead: AI Agent Prompting PROJECT_ROADMAP.md P-045 and Deliverables/MAFC_PROJECT_SCAN_2026-10-09.md P-045 cite MAFC R203 and Codex `8a3d0c7b` T002–T004; original logs not rerun here.

## Installing skills on it
- Claude app: upload the UNIVERSAL zip (Settings → Capabilities → Skills). It rejects plugin manifests and nested `skills/<name>/SKILL.md`. Claude Code: the `-claude-code-plugin` package or `/plugin install` from the repository marketplace.

## Sender discipline (P-032; 2026-10-08 usage scan)
- Within authorized write scope, save NEXT_/SHORT_ prompts, hash final saved bytes and propose/update the saved-prompts row under shared-write rules. Otherwise state NOT SAVED / NOT HASHED and the reason.
- **Cross-project delivery (P-046):** use To: <project>; copy or point into its Incoming/ only when destination writes are authorized, and record delivery under shared-write rules; otherwise propose the destination. Historical lead: AI Agent Prompting PROJECT_ROADMAP.md P-046 and Deliverables/MAFC_PROJECT_SCAN_2026-10-09.md P-046 trace GitHub Release Skill/Handoffs/2026-10-08_HANDOFF_folder-cleanup-work-mode-lessons.md → MAFC register R206. This is scan evidence, not a rerun.
- Before the first project write, read the applicable `AGENTS.md` version and record the clock source and timezone in the session log.
