# Manus — observed host behavior

Notes from real Manus runs in Jesse's projects. The authoring method is in `references/manus.md`; this file records how the host behaved.

Evidence base: jesseraber.net Manus sessions and `.manus/mcp-results` (2026-10-03); Cabinet Price Research Manus submissions and reviews (2026-08-27 to 2026-08-30).

## How it runs on the owner's PC (Manus User Desktop)
- **Observed 2026-10-03:** with a project folder open, Manus followed the project's `AGENTS.md`: read quick context, roadmap and session index, and wrote its own session log.
- **Observed:** it split work into subagents, each with its own session ID and log, and queued a scripted workflow with an agent-call budget ("requested 15, effective limit 17"). Ask for the subagent session IDs in the final report.
- **Observed:** it wrote output straight to absolute Windows paths given in the prompt.
- **Observed:** `manus-config` was not installed on that device; do not assume Manus CLI tooling exists locally.

## Data honesty
- **Observed 2026-10-03:** asked for a backlink-gap audit with no provider export available, Manus stopped that part, recorded the data gate, and delivered a public-web-only report labeled as such. Chat models given the same brief estimated authority scores. Keep the data-source line from Part 1 in Manus prompts anyway.
- **Observed 2026-08-30:** submissions were mechanically clean and self-assessed honestly, but a `source_date` field held court-opinion dates rather than transaction dates (8 of 13 rows), and nested payments looked additive. Define field semantics in the prompt (Part 1, structured data).

## Dead runs
- **Observed 2026-08-27:** one of four parallel runs (R8C1H) left only a write-access test file. Require a partial deliverable and a coverage note early (for example after the first source batch) so a stalled run is visible.

## Open questions
- Whether subagent budgets are configurable from the prompt; how Manus Desktop resolves OneDrive cloud-only files.

## Review prompts from observed runs (P-030; 2026-10-08 usage scan)
- Name a minimum executed-test list: run each specified command, report its exit code and test count; findings without an executed check are `INFERRED`.
- Freeze `PRELIMINARY_FINDINGS` as actual defects with evidence, not a plan of checks still to run.
- If dependency setup is needed, pre-authorize a reviewer-owned scratch venv and pip there when in scope; do not modify project or system environments by implication.
- For line-ending comparisons, report whether bytes, LF-normalized text or another method was compared so reviewers can reconcile different results.
