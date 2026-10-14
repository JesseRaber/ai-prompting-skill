# Meta AI

Meta AI chat, its deep-research mode, and **Muse** (Meta's agent that works through the browser and can add files to a shared folder; owner-identified 2026-10-09).

Evidence base: Meta AI outputs in Local AI Model Research (2026-08-22), Cabinet Price Research (2026-08-26), uniquewoodworx.com hosting review (2026-08-27) and jesseraber.net research packages (2026-10-02 to 2026-10-03); one Muse upload into a project folder and its review (Multi Agent Folder Cleanup Skill, `Incoming/2026-10-08_Muse_BlogDrafts_Review/`, 2026-10-08).

## Strengths and weak spots
- Strong: produces complete artifacts (one run returned a standalone interactive web app); deep-research mode returned a 41-observation dataset with a source index.
- Weak (observed): pricing figures and project inventories were wrong; real capabilities were combined into overbroad claims ("any AI can edit and publish"); footnote markers lost their source links when pasted.

## Writing the prompt
- Give it the real project facts (apps, runtimes, repos) rather than letting it guess.
- Ask for a source URL beside every number, and for files rather than pasted text when citations matter.

## Reviewing what it sends back
- Treat every claim as a lead that needs a primary source before it changes a plan.
- Save the original download, not a pasted copy, so links survive.

## Muse (P-044; observed 2026-10-08)
- **Observed:** Muse added four files to a project folder by creating a new top-level folder. It left no session log, no index row, no tracker item and no provenance note, and it read a stale record header as current state. Its own shell clock was UTC, so one event was labeled 23:38 in the wrong zone. Image names did not match the post they came with.
- **Add-only agent:** treat Muse as one that can add files but not edit shared records. The prompt names the minimum it leaves behind: upload into `Incoming/YYYY-MM-DD_muse_<topic>/` with a `_PROVENANCE.md` (tool and session or "browser upload", time with UTC offset, file list, one-line purpose, the index and tracker rows it wants added, marked pending). The next editing agent applies those rows.
- Say which existing folder its material belongs in; without that it creates a new top-level folder. Name the files it may touch and the records it must not create.
- Ask for times with a UTC offset and for the current-state source it used (file and date), since it quoted a superseded header.
- **Owner-stated 2026-10-09 (untested here):** Muse can read the project folder through its web browser over OneDrive; it remains add-only for records. Its statements about project state were wrong in a blog draft (test count, stale register and package claims) — treat every such claim as unverified, require file + date per claim, and run an accuracy pass (Manus or Codex) before anything it writes is published.

## Open questions
- Meta AI: file access, upload limits and skill support. Muse: whether it can read a pointer file before acting, whether it keeps a session, and whether skills can be installed on it (untested).
