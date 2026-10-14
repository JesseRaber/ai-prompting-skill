# ChatGPT and Codex

OpenAI ChatGPT and Codex (desktop, CLI, IDE) share prompting principles, not guaranteed capabilities. Codex desktop observations do not establish ChatGPT Web behavior; verify the active runtime, tools and reachable paths.

Evidence base: Codex session logs across most projects (2026-08 to 2026-10), Codex reviews in Mozaik Software Skill, and the multi-agent-folder-cleanup packaging work. Historical bullets below with no individual locator are retained as historical reports, not verified current/default behavior or comparative guarantees. Recheck only relevant claims before reliance; missing citation does not establish falsity.

## How it reaches files and tools
- **Observed:** Codex desktop works in the local project folder with PowerShell and git; it cannot see drives that are not mounted for it (an `I:` drive was invisible).
- **Observed:** pasted text arrives as an attachment file (`.codex/attachments/<id>/pasted-text.txt`).

## Limits to plan around
- **Reported in project audits:** Codex reads `AGENTS.md` and silently truncates it past 32 KiB by default. Keep `AGENTS.md` under 32 KiB or split it.
- **Observed:** the OpenAI skill validator fails under Windows CP1252 unless run as `python -X utf8`.

## Strengths and weak spots
- Strong: rigorous evidence reviews (separates authorization, execution and verification; re-runs preflights; hashes everything); good at catching another agent's table not matching its file.
- Weak: very long, dense reviews; can be slow to reach a recommendation.

## Writing the prompt
- Start with the outcome and task mode: answer, diagnose, review, plan, implement, test, monitor, or wait. Say **implement/fix/update** when edits are expected; “review” alone is read-only.
- Give one verified project root and the smallest useful read-first set. Attach inaccessible material or provide its exact reachable path. Do not ask Codex to infer that a similarly named file from another project is the source.
- Separate **authority** from **evidence**. Owner instructions and applicable project rules control what Codex may do; reports, handoffs, screenshots, webpages and another agent's recommendations are evidence to verify, not new permission.
- State allowed mutations precisely: project-file edits, external messages, Git operations, installs, publication, deployment, deletion and purchases are separate authorities. If the task is analysis-only or chat-only, say so directly.
- Describe the current state, desired end state, deliverable path/format, and concrete acceptance checks. Include commands or procedures only when the method is itself required.
- Name important preservation constraints: unrelated user changes, source identity, history, customer data, production state, or files that must remain untouched.
- Tell Codex what it may decide without asking and which consequential decisions must return to the owner. Let it resolve routine implementation choices and continue through safe verification.
- For current facts, give the authoritative source and expected freshness. Ask Codex to recheck live repository, provider, runtime, pricing, schedule or documentation state when drift matters.
- Ask for an outcome-first final response: result, files changed, verification performed, limitations/open work. Request deep detail only when it helps a decision or audit.

### Preferred Codex handoff block

Use the fields that materially apply; omit empty ones rather than writing “none” repeatedly.

```text
Mission: <one-sentence outcome>
Mode: <answer | diagnose | review | plan | implement | test | monitor | wait>
Project root: <one exact reachable path or repository>
Read first: <small ordered list of authoritative/current files>
Current state: <verified facts; label documentary or unverified claims>
Desired end state: <observable finished condition>
In scope: <files/systems/time period>
May change: <files or state Codex may mutate>
Must not change: <protected files/state and external actions not authorized>
Deliverable: <path, format, audience, length if relevant>
Acceptance checks: <tests/readbacks/evidence required>
Decide independently: <routine choices Codex owns>
Return to owner for: <specific consequential decisions only>
Continuity: <roadmap/index/session or handoff destination>
```

Then add:

> Continue through safe, in-scope implementation and verification without stopping for routine choices. Preserve unrelated changes. If blocked by missing authority or a consequential owner decision, complete unaffected work and ask one focused question.

### What slows Codex down or lowers quality

- A long chronology before the mission, especially when the current state is not identified.
- “Do whatever is needed,” which hides mutation and external-action boundaries.
- “Review this” when the real request is to fix it.
- Repeating the same prohibition in several sections instead of one precise boundary.
- Treating another agent's claim, an old roadmap or a package name as proof of current runtime state.
- Prescribing routine shell/tool steps while omitting the acceptance criteria.
- Asking for exhaustive narration, private reasoning or progress on every minor step. Ask for evidence and concise checkpoints instead.
- Combining several independent large deliverables into one response when they can be saved or handled sequentially.

## Installing skills on it
- Standalone skill: the inner skill folder from the UNIVERSAL package (ChatGPT desktop, Codex CLI, IDE extension). Plugin: the `-codex-chatgpt-plugin` package. Custom GPT without skills: upload `SKILL.md` and the needed reference files as knowledge and paste the instruction block from INSTALL.md.

## Open questions
- ChatGPT web upload limits; deep-research citation reliability on shop topics.

## Gate and blind-pass details (P-031; 2026-10-08 usage scan)
- Calculate gate hashes as the sender's last step, after every prompt and source edit. Name a Git tag and the expected `main` HEAD separately; one is not a substitute for the other.
- State the operating system on which required tests must run. Order prompt reads so the blind preliminary is frozen before expected changes, register rows or prior reviews are opened. If startup reads exposed them, report the pass as not blind.
