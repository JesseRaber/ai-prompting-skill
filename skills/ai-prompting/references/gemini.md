# Gemini

Google Gemini apps (including Gemini Deep Research and Gemini skills) and the Gemini models behind other tools. Antigravity is covered in `references/antigravity.md`.

Evidence base: Gemini cleanup tests and audits in the Multi Agent Folder Cleanup Skill and Mozaik Software Skill projects (2026-09-29 to 2026-10-01), Gemini Deep Research reports in jesseraber.net and Sanding Robot, and hosting reviews in uniquewoodworx.com. Historical bullets below with no individual locator are retained as historical reports, not verified current/default behavior or comparative guarantees. Recheck only relevant claims before reliance; missing citation does not establish falsity.

## How it reaches files and tools
- **Observed:** worked from attached handoff files and a single all-in-one handoff document; also reported reading Google Drive items.
- **Reported historically:** lookup_skills/get_skill_resources loaders. Gemini Argon review 2026-10-13 reports automatic metadata plus retriever:expand_skills and supplementary skills:get_skill_resources; expansion was not exercised. Source: AI Agent Prompting Incoming/2026-10-13_codex_gemini-argon-review-retry/GEMINI_ARGON_REVIEW_v108.txt. Tool names are runtime-specific; availability is not executed retrieval.
- **Observed:** Deep Research returns long, well-cited reports (one run: 45 primary citations).

## Limits to plan around
- **Observed (upload tests 2026-10-03):** the Gemini Apps skill uploader rejects `.ps1` and `.yaml` files and nested optional folders, and its security scan rejected defensive code that names credential files. Ship Gemini a Markdown-only package; never disguise code to pass the scan.
- **Observed:** displayed a 75-row approval table that differed from the CSV it had validated in 13 rows (six nonexistent paths). Require tables generated from the file and bound to its hash and row count.

## Strengths and weak spots
- Strong: broad web research with citations; follows a mode (stayed in Plan, changed no files) when told.
- Weak: misidentified a supplied skill copy as different (all 16 files were byte-identical); listed Drive IDs in a checksum column; marked static walkthroughs "PASS"; overstated consequences (machine damage, permanent loss) beyond the evidence; mixed up app names and runtimes in an inventory; repeated customer names it was asked to leave out.

## Writing the prompt
- Attach one handoff file, or one all-in-one packet when file count is limited.
- Ask for exact source identity for every file it compares: path, full hash or resource name, quoted text.
- Say "static review is not a test; label it static" and "state consequences only as far as the evidence goes".
- Name what to leave out (customer names, internal data).
- **Drive-connected Gemini (P-053; GaugeWorx 2026-10-07):** say "save as you go into folder id <id> as plain Markdown files, not Google Docs", and give the root as a folder id. Observed: two turns of advice were not saved until the owner asked; the shared records it then wrote were Google Docs that other agents could not append to; it read the root folder name as a file.

## Reviewing what it sends back
- Re-derive any table or list it presents against the real file.
- Check "already fixed" and "missing" claims against the pinned source.

## Installing skills on it
- Use the `-gemini-apps-only` package (no scripts, no YAML).
- **P-050 historical lead:** AI Agent Prompting PROJECT_ROADMAP.md P-050 and Deliverables/MAFC_PROJECT_SCAN_2026-10-09.md P-050 cite MAFC R182/host table: regular Gemini rejected a script-bearing package while Spark loaded it. The ai-prompting Gemini package has no scripts. Original uploader behavior not rerun; verify current acceptance separately.

## Open questions
- Prompt/attachment limits and executed cross-session installed-skill persistence remain untested here. Gemini Argon 2026-10-13 reported persisted metadata in a fresh chat; this is a dated host report, not a controlled persistence test.
