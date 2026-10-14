# Changelog

## 1.0.8 — 2026-10-09 (candidate)

- P-041: "Read-only" limits task files, not continuity records (SKILL.md, grok.md, claude.md).
- P-042: Grok Bot runtime corrected — own Linux machine via the Microsoft Graph OneDrive connector; staged edits; runtime slug.
- P-043: Every reported time carries a UTC offset.
- P-044: Minimum upload for add-only agents (SKILL.md, agent-template.md); Muse (Meta) added to the Part 2 route and `meta-ai.md`.
- P-045: Point, don't paste — reviews read and saved in the project folder (SKILL.md, claude.md, multi-model-review.md).
- P-046: `To: <project>` header and target-project `Incoming/` copy for cross-project prompts.
- P-047: Connector reads by file id; listings state their view and time (grok.md).
- P-048: Prompt states direct-edit vs staged PENDING for shared records.
- P-049: Read-first lists name rows or sections of large trackers.
- P-050: Regular Gemini chat rejects packages containing scripts; Spark agents accept them (gemini.md).
- P-051: Reported version comes from the file read; anything not run is "not run" (folded into the P-037 line).
- P-052: Chat Grok writing through the Google Drive connector — folder id destination, Markdown not Docs, upload→verify by id→trash (grok.md).
- P-053: Drive-connected Gemini — save as you go, Markdown not Docs, folder id root (gemini.md).
- P-054: Code deliverables — build capability stated; NOT COMPILED label and first build command.
- P-055: Reply check compares the cited owner quote with the executed scope; sender writes the scope out.
- P-056: Research as Markdown with URLs inline; named data files ship with the report.
- P-057: claude.md host row for claude.ai with the Google Drive connector.
- P-058: Antigravity on Windows PowerShell 5.1 — encoding-safe appends, no cross-file regex, own-line edits only, one slug per runtime (antigravity.md; SKILL.md clause).
- P-059: Opal read-lists are literal; installed-skill contamination on Opal/Antigravity (opal.md, multi-model-review.md).
- P-060: Self-contained handoffs point nowhere outside themselves; scenario-walk comprehension test (SKILL.md clause, multi-model-review.md).
- P-061: Muse reads the folder via browser (owner-stated); its project-state claims need file + date and an accuracy pass (meta-ai.md).
- P-006 (partial): Copilot locator/synchronous notes and Grok `/workspace/artifacts` note, labeled host-reported pending rerun (copilot.md, grok.md).
- P-040: Linked-PC shell read failures → stage instead (claude.md).

## 1.0.7 — 2026-10-08 (candidate)

- P-021: Self-contained Opal report with delivered filenames and hashes.
- P-022: Installed-copy independence disclosure for reviewers.
- P-023: Separate blind set until preliminary findings freeze.
- P-024: Fresh-conversation SHORT pointer and Opal local-path warning.
- P-025: Opal conversation-ID handoff via delivered filename and owner folder.
- P-026: Call accounting, GATE/OPTIONAL labels and early GATE downloads.
- P-027: Executed evidence requires command and exit code or DOM text, time and URL.
- P-028: Antigravity session, scope, setup, placeholder, verdict and replacement controls; P-039 UUID instruction folded in.
- P-029: Grok provider/root, disconnected handoff and Grok Bot controls.
- P-030: Manus executed tests, preliminary defects, scratch venv and normalization method.
- P-031: Codex sender gate hashes, Git heads, test OS and blind-read order.
- P-032: Claude saved and hashed prompt plus prewrite authority/clock record.
- P-033: Opal organization-policy blocks.
- P-034: Six-point pre-send check.
- P-036: Relevant-when description triggers (option B).
- P-037: Loaded guidance version and source channel/path.

## 1.0.6 — 2026-10-06 (candidate)

- Applied owner-approved P-017–P-020: Opal console encoding caution, receiving-agent routing clarification, Antigravity read-only scope guard, and source-ZIP existence check for install prompts.
- Kept the dedicated Copilot package introduced in v1.0.5. Copilot upload and routing remain unverified.
- Condensed repeated `SKILL.md` wording so its body remains below 9,500 characters for the observed Opal read-size concern.

## 1.0.5 — 2026-10-06 (candidate)

- Added a deterministic Microsoft Copilot agent package containing the Markdown skill, all references, and a Copilot install guide. Package construction is locally verified; Copilot upload and routing remain open.
- No prompting guidance changed from v1.0.4. Other host packages carry the new version identity and require affected host checks before release.

## 1.0.4 — 2026-10-06 (candidate)

From the 2026-10-06 prompt-outcome scan (roadmap P-007–P-016, owner-approved):
- Shared rules: unknown data stays `UNKNOWN` (no estimated metrics); define ambiguous fields and forbid agent-set eligibility flags; never name a model as current; mark steps GATE vs OPTIONAL; date guards go inside the prompt; duplicate-reply hash check on import.
- `copilot.md`: records the observed physical-safety refusal and the framing that worked; GATE/OPTIONAL labeling.
- `claude.md`: correction-pass follow-up. `local-models.md`: stale model names; declare research date and unknowns.
- `multi-model-review.md`: packet sensitive-file pre-flight; blind reviews on hosts that auto-load `AGENTS.md`; shared-brief agreement is not independence; no "unanimous/authoritative" labels.
- `opal.md`: crawler false 404s, duplicate replies, in-prompt date guard.
- New `manus-observed.md`: Manus Desktop behavior, data honesty, dead-run detection. `manus.md` unchanged.

## 1.0.3 — 2026-10-05 (candidate)

- Renamed: the skill and plugin are now `ai-prompting` (display name "AI Prompting"); the GitHub repository and Claude marketplace are `ai-prompting-skill`. Skill folder moved to `skills/ai-prompting/`; package files are `ai-prompting-1.0.3-*.zip`.
- No guidance content changed from 1.0.2.
- Hosts with 1.0.2 or earlier installed under `ai-agent-prompting` should install `ai-prompting` and then remove the old name to avoid two copies loading.

## 1.0.2 — 2026-10-03 (candidate)

- Shared local-path rule now distinguishes agents bridged to the PC from unlinked cloud chats, and notes Opal's search-locator use of Windows paths.
- Shared rules ask for the literal output form and say how to handle a missing input (state the gap, finish unaffected work).
- `claude.md` rewritten as a dated host matrix with a literal output-format rule, a compact handoff block and a check that results landed on the PC.
- `multi-model-review.md` adds a blind first-pass rule for independent reviewers.
- `opal.md` clarifies Windows paths as search locators; `antigravity.md` describes the host by capabilities rather than one model version.
- Copilot, Grok and Gemini proposals deferred until source-connected reruns.

## 1.0.1 — 2026-10-03 (candidate)

- Adds a shared executable-handoff contract covering task mode, current versus desired state, scope, source authority, deliverables, acceptance checks, decision boundaries, mutation authority and continuity.
- Expands ChatGPT/Codex guidance with a compact preferred handoff block, autonomy wording, evidence/freshness rules and common prompt patterns that slow execution or reduce quality.
- Preserves v1.0.0 content and packaging while leaving publication, installation and release unapproved.

## 1.0.0 — 2026-10-03 (candidate)

First repository release. Combines:
- the single-file `ai-agent-prompting` skill saved 2026-10-03 (shared rules and Opal section);
- the whole `manus-prompt-engineering` skill (SKILL.md body plus 21 references, 8 templates and 1 example, byte-identical);
- new Opal guidance from two full Opal event logs and about 20 Opal prompts and replies;
- starter notes for Copilot, Gemini, Antigravity, Grok, Meta AI, ChatGPT/Codex, Claude and local models, from runs in Jesse's projects;
- a multi-model review procedure and a template for adding agents.

Layout is flat (`references/*.md`) so the Opal package carries every file.
