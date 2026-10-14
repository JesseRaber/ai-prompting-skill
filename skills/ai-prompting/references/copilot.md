# Microsoft Copilot

Microsoft 365 Copilot chat, Copilot Researcher and Copilot Notebooks, used with Jesse's work tenant. Opal is covered separately in `references/opal.md`.

Evidence base: Copilot audits and research reports in the Mozaik Software Skill, Multi Agent Folder Cleanup Skill, uniquewoodworx.com, Local AI Model Research, Cabinet Price Research and jesseraber.net projects, 2026-08-21 to 2026-10-03.

## How it reaches files and tools
- **Observed:** reads OneDrive/SharePoint content through tenant search and connectors, not through a direct folder mount. Prompts that named the exact OneDrive folder path worked better than "the project folder".
- **Observed:** its unique strength is company data: Viva Engage posts, Word documents, meetings and OneDrive items. One research run cited 727 internal tenant records.
- **Observed:** connector renderings can change line wrapping. A 196-line file came back as "268 lines", which looked like a different version until compared.

## Limits to plan around
- **Observed:** partial reading. In one "full audit" it fully read 4 of 16 skill files and summarized the rest from the index. Ask for a per-file coverage ledger (read fully / skimmed / indexed only / not found).
- **Observed:** cannot compute hashes or prove byte identity; it correctly declined to claim them.
- **Observed:** CSV outputs had truncated URL fragments and a one-row offset between values and descriptions. Re-check tabular data.
- **Observed 2026-10-02 (jesseraber.net, session T021):** Copilot refused a request for machine-ready CNC feeds, speeds and tooling. Wording such as "production-grade parameters" and "drive machining" read as direct machine control under its physical-safety policy (tool failure, ejected parts, operator injury). It offered an educational/verification scope instead. A re-prompt framed as "teach the formula, cite manufacturer sources, no machine-ready values, every result REFERENCE ONLY until a supervised test cut" succeeded and produced a useful report. Write it that way from the start for any machine- or safety-adjacent topic.

## Strengths and weak spots
- Strong: Windows/OneDrive/Microsoft platform detail (reparse points, Cloud Files API, sharing violations, PowerShell 5.1 vs 7); sound self-corrections when challenged; candid about connector limits.
- Weak: proposes additions that already exist in the source; treats search hit counts as coverage; dates and items from company search need locators (item ID, group, timestamp) before they count as provenance.

## Writing the prompt
- Give the exact OneDrive path (`OneDrive - <org>` › `AI Project Folders` › `<project>`) and the canonical repo URL, if any.
- Ask for: a coverage ledger, direct links or item IDs for every company-data claim, "new evidence" vs "repeats known material" labels, and EDIT / ADD / DELETE / MODIFY lists.
- Point it at the domains where it adds the most (Microsoft platform, tenant data) rather than a general re-review.
- Keep the request bounded; for machine or safety-adjacent topics, state the scope up front (educational, sourced, no operating values).
- Label each recommendation `GATE` or `OPTIONAL`. Observed 2026-08-25 (Local AI Model Research): an otherwise accurate Copilot reply turned optional diagnostics into new prerequisites.
- Do not carry a safety notice into unrelated prompts; a CNC disclaimer pasted into an SEO prompt added noise without changing the result.
- **Reported by Copilot's own 2026-10-03 preference review (P-006; not yet confirmed by a source-connected rerun):** a local `C:\` or OneDrive path is a search locator, not a file it can open — give the path and expect retrieval by name; completion is synchronous — do not assume background delivery or a later follow-up.

## Reviewing what it sends back
- Compare its quoted text with the pinned local file before accepting "the source has changed".
- Reject duplicate additions; keep source locators.

## Installing skills on it
- The multi-agent-folder-cleanup UNIVERSAL package is listed for Copilot; Copilot-side install was not upload-tested in that project. A short entry document with direct links to the reference files was Copilot's own suggestion for retrieval.

## Open questions
- Exact prompt length and attachment limits; how skills load in each Copilot surface.
