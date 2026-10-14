# Google Antigravity

Google's agentic coding app, run with Gemini models. Describe it by what it can do (local folder access, scripts, tests, git), not by one model version; versions drift (observed 2026-09/10: sessions logged as "Gemini 3.8 Flash High"). It works directly in local project folders.

Evidence base: Antigravity session logs in Multi Agent Folder Cleanup Skill, jesseraber.net and Jesse's Social Research, 2026-09-30 to 2026-10-02. Historical bullets below with no individual locator are retained as historical reports, not verified current/default behavior or comparative guarantees. Recheck only relevant claims before reliance; missing citation does not establish falsity.

## How it reaches files and tools
- **Observed:** reads and writes the local OneDrive project folder, runs scripts, applies git patches and runs test suites on a local clone; saves downloadable artifacts in its own app-data folder.
- **Observed:** follows the project's `AGENTS.md` (session logs, import workflow).
- **Observed:** can install a skill straight from its GitHub repository; the copy matched byte for byte.

## Strengths and weak spots
- Strong: fast at writing prompts for other agents (Opal, Copilot, Gemini, Grok) and turning their replies into follow-ups; did the Opal patch-by-patch loop well.
- Weak: very confident summaries ("production-grade", "100% complete", "zero secrets present") that go beyond what it checked; prompts it writes for other agents tend to be long and padded with role titles. Spot-check its verification claims.
- **Observed:** wrote a first Opal prompt that was too long for Opal; fixed it by saving the prompt to a file and pasting a short kick-off line.

## Writing the prompt
- It can read the project directly, so point it at files instead of pasting them.
- When it writes prompts for other agents, ask for the short-pointer pattern and a length cap.
- Ask it to separate what it ran from what it inferred.
- **Keep read-only checks narrow (observed 2026-10-06, W-006c):** while checking this skill, Antigravity probed gcloud credentials and opened an ADC sign-in for an unrelated Data Agent Kit plugin. For read-only checks, state: "No installs, sign-ins, credential checks, or plugin setup. Stop and report if any is required."

## Installing skills on it
- Install from the GitHub repository, or use the UNIVERSAL package.
- For an owner-authorized install, supply the ZIP's absolute path, confirm it exists, validate the archive and preserve a rollback copy before replacing an installation. Never delete the existing copy first; missing/invalid input → report and stop replacement.

## Shared-record safety on Windows (P-058; observed 2026-10-09)
- **Observed (MAFC session `3a4f02c7`, cleanup skill installed):** in Windows PowerShell 5.1, `>>` appended a session-index row as **UTF-16LE** into a UTF-8 file (278 NUL bytes; file unreadable as text); `Get-Content | Set-Content` rewrote both indexes whole and converted LF to CRLF; a global `-replace '| in progress |'` flipped **another session's** live row to Completed; no read-back. Its own session log was written UTF-16LE end to end. The same host used two slugs that day (`antigravity`, `agy`).
- Put in every Antigravity prompt touching shared records: "State the shell and obey destination shared-write rules. Preserve encoding, BOM state and line endings with an explicit matching writer; verify by read-back. In PowerShell 5.1, `Set-Content`/`Out-File -Encoding utf8` emits a BOM; `>>` may mismatch the file encoding. Do not use these as generic preservation methods. Never globally regex-replace a shared file; insert/update only authorized rows. Use one stable runtime slug." For BOM-free UTF-8, an explicit .NET UTF8Encoding(false) writer is an option, not writer coordination. Documentation: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding?view=powershell-5.1 (checked 2026-10-14).
- Safer still for reviews: "Write your report as a new file and your own session log; do not edit the index or tracker — put proposed rows at the end of your report."

## Open questions
- Context limits; whether its own Gemini model limits (e.g. no audio generation) affect tasks.

## Prompt controls from observed runs (P-028, including P-039; 2026-10-08 usage scan)
- State the absolute project root. Use a shell command to generate a new session UUID for each chat; never reuse an old UUID. Create the session log before substantive work and record the outcome before answering.
- Count register and index edits as task files. Limit writes to the named project and the prompt's allowed files.
- In every prompt, say: "No sign-ins, auth checks (`gcloud auth`), installs, plugin setup or extensions unless explicitly authorized." Report a blocked dependency instead of attempting setup.
- Leave owner placeholders such as `[JESSE: fill]` intact; never invent owner anecdotes. Do not suggest `ExecutionPolicy Bypass` without a safety explanation.
- Bind verdicts to observed tests and coverage; one smoke test cannot establish 100% completion or production readiness.
- Use the replacement sequence in "Installing skills on it"; archive existence alone grants no authority.
