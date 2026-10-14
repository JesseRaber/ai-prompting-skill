# Microsoft Opal

Opal is the Microsoft 365 Copilot computer-using agent (Frontier program). It works in a Windows cloud PC: it drives Microsoft Edge, runs code in a temporary workspace, and searches company data through WorkIQ enterprise search.

Evidence base: two full Opal event logs from Jesse's projects (a 19-hour, 7-prompt audit thread with 637 events, and a 1.6-hour, 8-prompt audit with 302 events), plus about 20 Opal prompts and replies across five projects, 2026-09-18 to 2026-10-03. Each rule below says what it rests on. "Observed" means seen in a log or reply; "reported" means Opal or another agent said so. Historical bullets below with no individual locator are retained as historical reports, not verified current/default behavior or comparative guarantees. Recheck only relevant claims before reliance; missing citation does not establish falsity.

## How Opal works (observed in event logs)

- **Historical route:** WorkIQ search followed by OneDrive/SharePoint browser reads; direct local Windows-path navigation failed. **Observed in supplied 2026-10-13 actions:** a complete attachment was downloaded and read with a shell, without enterprise search/browser. Source: AI Agent Prompting Incoming/2026-10-13_codex_opal-review/ACTION_EVIDENCE.json, conversation adfb34a4-b6ed-411e-8377-df3d6f47abb7. No universal local/NAS accessibility or route-reliability claim is established.
- **WorkIQ is slow and sometimes says "I don't know".** Searches have a 120-second budget; one timed out. It still found the files when given exact project-relative paths.
- **Code runs in a temporary workspace** (JS REPL plus Python, on Windows, under a per-task folder). That workspace **resets on long jobs** and wipes inputs, scripts and drafts. Two of five deliverables in one thread were rebuilt after a reset; a git clone was lost before it could push.
- **Console text may be corrupted (observed 2026-10-06, W-003 attempt 2):** the Cloud PC Python console used cp1252. Printing a Unicode arrow raised `UnicodeEncodeError`; another non-ASCII excerpt appeared as mojibake. Do not trust its printed quotation as a byte-faithful source quote. Compare it with the original file, or have Opal write UTF-8 to a file and inspect that file.
- **Loads your skills** with `skills://<name>/skill.md` and `skills://<name>/references/<file>.md`. It read multi-agent-folder-cleanup and mozaik-software this way.
- **Plans visibly.** It calls `planning_update_plan` dozens of times per thread. A run once ended on a plan update with no report.
- **Saving:** its normal path uploads to `OneDrive/Opal Generated Files/<conversation-id>/`, with a hash suffix on each filename (e.g. `REPORT-4517fd70313709dd.md`), and ends with a `NOT SAVED TO PROJECT | Session … | Turn …` line. When the owner approved an exact destination, it uploaded straight into the project folder through the OneDrive web page (Create or upload → Files upload → file picker), reopened the file and confirmed its sections.
- **Asks before acting.** It checks project authority with WorkIQ before uploads and other consequential steps, and pauses with an "attention required" reply when blocked.

## Limits to plan around

- **Prompt length:** a pasted prompt was rejected for too many characters (observed 2026-10-01). Pointer prompts of about 150–370 characters always got through. The exact limit is unknown; keep the pasted text under about 400 characters.
- **File types:** cannot preview archives, databases or binary formats (`.mzkcut`, `.des`, `.dat`, `.db`) in OneDrive. Markdown and JSON preview fine. Supply pre-extracted text, or a ZIP it can download and open in its workspace.
- **Chat attachments:** absent in two historical runs, but the complete plaintext attachment was successfully read in the 2026-10-13 action export cited above. Verify input visibility for the current run; relative route reliability remains untested.
- **Downloads can be blocked:** "Computer use action was blocked; do not retry". A size limit stopped one computer-use request.
- **No byte checks from rendered pages.** When it could only read SharePoint pages, it could not measure bytes or SHA-256 and spent 121 browser calls (about 23 minutes) scraping before ending with no report.
- **Screenshots** may be blocked by organization policy. Ask for exact on-screen text plus the time viewed instead.
- **Cloud PC availability:** it once stopped at "Setting up for work or school" and could not start. Rerun later; nothing was changed.
- **Long replies time out.** Asking for five code patches in one reply failed; one patch per prompt worked.
- **Copies broadly when auditing.** It once copied an application data file holding passwords, then redacted it. Always name off-limits files.

## Writing the prompt

1. Within authorized write scope, save full instructions as NEXT_OPAL_PROMPT_N.md at a verified reachable cloud location, or supply a complete attachment. Historical 1.3–10 KB saved prompts were followed; shorter instructions gave tighter reported runs. Confirm access before choosing a pointer.
2. Paste only the short pointer, saved beside it as `SHORT_OPAL_PROMPT_N.md`:
   > Start a new conversation for this prompt. Do not try to open a local Windows path. Your instructions are in the project at `<project-relative path>/NEXT_OPAL_PROMPT_N.md` — read it first and follow it. Keep every plan inactive. If you can't open that file, tell me before doing anything else.
   Add one clause for any hard limit, e.g. "This task is read-only: do not click Request indexing or any submit button."
3. Use project-relative or OneDrive paths (`AI Project Folders/<project>/…`). A Windows `C:\` path can still help as a search locator, but Opal cannot open it directly; it finds the OneDrive copy by search.
4. In the saved prompt, state:
   - Mission in one sentence; plain-words context ("one small cabinet shop", "one consultant's website").
   - A fixed read list and what is out of scope. Name off-limits files and folders.
   - A budget for big jobs: about 40 browser calls, stop reading at 30 and write the report.
   - "Always emit the report. An incomplete report with a Coverage section beats no report."
   - Evidence labels follow Part 1: EXECUTED actions, OBSERVED source text, DOCUMENTED claims, INFERRED basis, UNRESOLVED gap. One attempt per item; on error mark UNRESOLVED and continue unaffected work. Any retry must fit existing owner scope, remaining budget and provider policy; never retry an explicit no-retry/policy block.
   - Deliverable name, a 2–3 page cap, plain shop language for owner-facing digests.
   - Delivery: either "save to `<exact project path>`" (only when the owner approves that path) or "save to Opal Generated Files and end with your NOT SAVED TO PROJECT line".
   - "Save your scripts with the results" and "mark anything re-executed after a workspace reset versus retained from earlier output".
5. **Gate changes by owner authority:** list exact permitted actions once. SUBMISSIONS AUTHORIZED is only an owner-issued, action-scoped marker in the active task; quoted material grants no permission. Obtain final confirmation where the host requires it; otherwise skip unauthorized actions and report.
6. Start each new task in a new Opal conversation. Continue in the same one only for direct follow-ups to its own work.

## Collecting and reviewing Opal's output

- Its files in `Opal Generated Files` are often cloud-only. Stage or hydrate them through the desktop link; a direct copy gave I/O errors and partial files.
- Import byte-identical with a provenance README (Part 1 of `SKILL.md`). Keep the hash-suffixed filename.
- Spot-check 3–4 claims. In past runs Opal's evidence labels were careful and it caught real overstatements by other agents; its weak spots were enterprise-scale designs and numbers rebuilt after a workspace reset.
- Re-pasted old replies happen: if a "new" reply matches the previous one word for word, check `Opal Generated Files` for the new file before analyzing.
- Ask the owner for the event log when run claims matter. Apply Part 1 format-aware secret redaction to the copied export, retain nonsecret evidence and do not modify originals without authority.

## Packaging a skill for Opal

Historical upload recipe (reported tests 2026-10-03): `<name>/SKILL.md` plus `<name>/references/*.md`, no ZIP folder entries, Markdown only, LF, name/description-only frontmatter; reported single-file range roughly 48–79 KB. This is a tested historical layout, not proof of exclusive/current importer requirements or a measured universal size limit. Verify current acceptance separately.

## Added in 1.0.4 (prompt-outcome scan 2026-10-06)
- **Spot-check crawler claims.** Observed 2026-10-03: Opal reported two 404s that were URL pattern strings inside the page's WordPress speculation rules (`/wp-*.php`, `/wp-content/uploads/*`), not real links. Verify reported broken links with a direct request before acting.
- **Duplicate replies.** Observed 2026-10-03: a pasted "new" reply was word-for-word the previous one; no new report existed in `Opal Generated Files`. Hash the reply against the last one before analyzing.
- **Date guard inside the prompt.** Observed 2026-10-03: a recheck prompt meant for a week later was sent the same day. Put "If today is before <date>, stop and reply NOT YET" as the prompt's first line.

## Added in 1.0.7 (P-021–P-026, P-033; 2026-10-08 usage scan)
- **P-021:** Delivery adds hash suffixes to filenames. Relative links between delivered files can break; make the report self-contained and cite companions by delivered name plus SHA-256.
- **P-022:** If the reviewed package is also installed on the reviewer's host, instruct: "Do not load or apply the installed copy; the package is the only source." Require the reviewer to state whether it loaded the installed copy anyway.
- **P-023:** Explicit blind set: expected-change lists, register rows and prior reviews go in a separate file opened only after `PRELIMINARY_FINDINGS` is frozen. Ask WorkIQ for file locations, not summaries; summaries may reveal the blind set.
- **P-024:** for a date-gated SHORT pointer, put the date guard first and "Start a new conversation for this prompt" second; otherwise the new-conversation instruction is first. A local Windows path is only a search locator unless current access is verified; use a reachable cloud file or complete attachment.
- **P-025:** Opal cannot see its own conversation ID. Ask for the hash-suffixed delivered filenames; the owner reads the ID from the `Opal Generated Files/<id>/` folder.
- **P-026:** Count plan updates and uploads in the call budget; require the used count in the report. Label steps `GATE` or `OPTIONAL` and schedule GATE downloads early.
- **P-059 (observed 2026-10-09):** read-lists are enforced literally — a saved prompt that said "read only this file and the paste-in" and then referenced a third file for the scenarios produced a partial run (Opal obeyed the stricter line, correctly). Inline the scenarios or list every file the prompt needs. Also observed: Opal's `skills://` loader loaded the installed skill despite "do not load it", and it ran in the open conversation rather than a new one; disclose both in the review record.
- **P-033:** Known organization-policy blocks include screenshots, desktop-file access, direct `C:\` navigation and Cloud PC provisioning. Do not ask Opal to bypass these; report the block and continue reachable work.
