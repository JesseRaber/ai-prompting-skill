# Sending one prompt to several models

Used in Jesse's projects for skill reviews (Mozaik Software Skill review kits r1–r5) and research triangulation (jesseraber.net "5-way" research packages with Gemini, Copilot, Grok, Meta AI and Claude).

## Build a review kit
- Freeze a copy of exactly what is reviewed, with a SHA-256 manifest. Re-check that the kit holds the installed or current files; one kit shipped a stale `SKILL.md` while its README said "as installed".
- Write two prompts:
  - **Connected agents** (can read the project folder): paste the prompt; it reads the kit folder.
  - **Upload chats** (cannot read the folder): attach the kit folder or zip. For chats with file-count limits, attach one `ALL_IN_ONE.md` that holds every kit file under `===== FILE: <path> =====` headers.
- Tell each reviewer to say at the top if anything listed is missing and review only what it has.
- **Pre-flight the packet for sensitive files (P-011):** before sending, list every file and remove pricing, customer, credential and internal-only scans. Observed 2026-10-01: one reviewer's packet included a shop pricing scan.
- **Startup context (P-010):** use an isolated review context where supported; request kit-only reads subject to higher-priority host instructions. A prompt cannot undo prior exposure or override host requirements. Disclose automatic instructions/memory/skill metadata separately from full content and intentional reads; any prior-findings or installed-content exposure makes the pass not blind.

## Run it
- New chat for every reviewer, so none sees another's answers.
- **Keep the first pass blind:** do not tell a reviewer another reviewer's conclusion, a suspected defect or the verdict you hope for. Acceptance criteria and neutral examples are fine.
- Ask for the final answer in a clearly headed section. Some hosts (Antigravity) return a tool trace — commands run, searches, recomputed math — ahead of the answer; useful for seeing how it checked, but keep it out of the imported verdict.
- Same prompt for all, except a short model-specific focus line (e.g. Copilot: Microsoft platform and tenant data; Grok: math and file-by-file checks; Gemini Deep Research: cited web sources).
- Owner saves each reply into an incoming folder, non-governing until reviewed. Reviewers that reach the project folder save their own report there as a dated file and the reconciling agent reads it in place; the owner points instead of pasting (P-045).

## Combine the answers
- Re-check each reviewer's claims against the files before counting agreement. Agreement between models is not evidence on its own.
- **Shared-brief agreement is not independence (P-009).** If every model got the same seeded brief, matching answers may only repeat the brief. In the synthesis, say what each model was given and which claims it confirmed from an outside source. Do not label results "unanimous", "100% consensus" or "authoritative"; observed 2026-10-02/03, jesseraber.net syntheses did, and one consensus figure had no data source behind it.
- A synthesis is non-governing until the owner adopts it, whichever agent wrote it.
- Record which reviewer raised each item, the verdict (accept / narrow / reject) and why.
- Keep model outputs separate from the synthesized result, and keep the source report for each.

## Host comprehension test — scenario walk (P-060; 2026-10-09)
For a self-contained no-folder handoff, list 6–10 scenarios (S1…Sn), one expected behavior each; mark responses PASS/FAIL, and retest changed handoffs with a new hash. No pointers outside the complete delivered input set. Historical lead: AI Agent Prompting Deliverables/MAFC_PROJECT_RESCAN_2026-10-09.md P-060 cites MAFC Rules 4.0.0 section-0 walk, `1cdc3b65` T005/T011 and R226; scan reports candidate 1 failed on two inaccessible section pointers and candidate 2 passed 8/8. This was not the ai-prompting review kit; not rerun here.

## Blind review additions (P-022, P-023; 2026-10-08 usage scan)
- **P-022:** forbid optional installed-copy reads and ask for disclosure of metadata versus full expansion and timing. Kit isolation/non-loading names reduce accidental loading but do not guarantee blindness. Historical lead: AI Agent Prompting Deliverables/MAFC_PROJECT_RESCAN_2026-10-09.md P-059 cites Opal provenance and `1cdc3b65` T008; Antigravity also reported loading. The 2026-10-13 Opal selected actions verify installed v1.0.7 was read AFTER candidate input; host-mandated cause remains reported.
- **P-023:** Name the blind set explicitly: expected-change lists, register rows and prior reviews. Put them in a separate file that opens only after a dated, hashed `PRELIMINARY_FINDINGS` is frozen. Do not order startup reads that expose that set before the freeze; if exposure occurs, label the pass not blind.
