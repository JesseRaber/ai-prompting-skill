# Grok

xAI Grok (including Think Mode and DeepSearch).

Evidence base: Grok audits and reviews in Mozaik Software Skill and Multi Agent Folder Cleanup Skill (2026-10-01 to 2026-10-03), research reports in jesseraber.net, and hosting reviews in uniquewoodworx.com. Historical bullets below with no individual locator are retained as historical reports, not verified current/default behavior or comparative guarantees. Recheck only relevant claims before reliance; missing citation does not establish falsity.

## How it reaches files and tools
- **Observed:** worked from a large self-contained handoff file, uploaded files, and a read-only Google Drive copy of the project (`G:\My Drive\…`). That copy lagged the OneDrive original; tell Grok which copy is authoritative.
- **Observed (GaugeWorx, 2026-10-07/08):** with the Google Drive connector, chat Grok also *writes* to a Drive project. See the Drive-writer block below.
- **Reported:** fetched a missing file from GitHub when an upload was incomplete.
- **Observed:** sandboxes are POSIX; OneDrive placeholder (hydration) state cannot be checked there.

## Strengths and weak spots
- Strong: careful file-by-file audits; listed reference hashes that matched local bytes; clear engineering math in Think Mode; good "leave alone" lists.
- Weak: external claims without source URLs; treats one release checklist as complete; overstated "every AI can edit your repo" in a hosting review.

## Writing the prompt
- Supply a single handoff file with the authority order, the project tree, and the canonical repo and commit.
- Require a direct URL for every external claim and a statement of what was not covered.
- Ask for findings with file:line references.

## Installing skills on it
- Upload the UNIVERSAL package (or the whole skill folder) and paste the instruction block from its INSTALL.md.

## Open questions
- Upload size and file-count limits; whether its GitHub connector can write.

## Chat Grok and Grok Bot (P-029; 2026-10-08 usage scan)
- For chat Grok, pin the provider and exact root (for example the named OneDrive tree, not a Google Drive replica) and require Grok to echo the root listing it used. If disconnected, send a register snapshot and request a reproducible fixture script; number proposed rows during import. Do not put `.ps1` files in Grok uploads; a skill archive containing one was rejected.
- Read-only prohibits task edits; own-session logging follows owner scope/project rules, shared records follow their write controls. Explicit no-writes means a chat NOT SAVED checkpoint (P-041). Historical lead: PROJECT_ROADMAP.md P-041/P-042 cites MAFC `35ced8da`, not a verified GaugeWorx chat attribution; original incident not rerun here.

## Grok Bot (P-042; corrected 2026-10-09)
- **Observed (MAFC log `35ced8da`):** Grok Bot is an executor agent that runs on **its own Linux computer** and reaches OneDrive only through the **Microsoft Graph connector**. It is not on the owner's PC and is not the xAI Grok app; it did not use the Google Drive copy. The connector offers whole-file replacement only, no conditional write, so it staged `PENDING_SHARED_EDITS.md` with base SHA-256s and ran helpers only on synthetic fixtures on its own machine.
- Prompt it with OneDrive paths (not a Drive replica), expect staged edits with base hashes rather than direct record updates, and do not ask it to run project helpers. Say: "Log each turn as you go in `<project>`; write only under `<project>`; preserve exact product spellings from the source." Do not reconstruct hours of work as if it were contemporaneously logged.
- Slug the session by runtime (`cursor-grokbot` or similar), never the `grok` slug another host already uses in that project; put model, connector and machine in the log header.

## Chat Grok writing through the Google Drive connector (P-052, P-047, P-054; GaugeWorx 2026-10-07/08)
- **Observed:** its first write landed in its local sandbox, not Drive; the owner had to correct it. Name the **Drive folder id** as the destination, say the sandbox is staging only, and require a Drive listing as proof.
- **Historical observation (GaugeWorx, 2026-10-07/08):** the exposed Drive route used create/trash rather than in-place edits. Replacement requires owner-authorized scope and a supported conditional operation protecting the old version, cooperating lock covering writers/devices, or designated/sequential control under destination rules. Otherwise stage PENDING and retain the original. If distinct-name upload or final rename is unavailable, stage instead; do not trash. If permitted: checkpoint → read by id → upload with a distinct temporary name → verify bytes/size/hash by new id → authorized trash of old id → assign canonical name and verify a single live result. Re-read/hash alone is not writer exclusion. A by-name download previously returned an old version.
- **Observed:** records another agent created as Google Docs cannot be appended; pending rows accumulated in one log for ~16 h. Require plain Markdown files (`text/markdown`), never Google Docs.
- **Observed:** it wrote a .NET WPF project it could not compile ("sandbox has no .NET SDK"). For code, state whether it can build; if not, require a `NOT COMPILED` label and the owner's first build command, and send code to a repository, not a sync-mirrored tree (a mirror showed `SensorCollector (1).cs`).
- Every listing or finding states its view (connector API, local mirror, sync client, download) and time; a name that resolves to more than one id → stop and report (P-047).
- **Delivery distinction:** downloadable/user-visible `/workspace/artifacts` output is not proof of a save into the owner's project. Report NOT SAVED TO PROJECT and the artifact name until the named destination is verified, unless the owner chose artifact-only delivery. Historical basis: Grok preference review 2026-10-03 (P-006, pending rerun); the 2026-10-13 review only reported user visibility, not a project save.
