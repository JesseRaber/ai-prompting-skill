# Host install log — AI Prompting

Append-only. One row per attempt. Never edit an old row; add a `superseded` row instead.
Evidence: `observed` (agent saw it), `user-reported`, or a path to a screenshot / error text.
Host load: `confirmed in host` only after an in-host check after restart (skill view, "reveal in folder", arrival line with path); otherwise `files verified; host load not checked`. Matching bytes and `--version` prove the files, not the load.

| Date (TZ) | Version | Asset (sha256 first 12) | Host / account | Channel | Action | Result | Displayed | Evidence | Host load | By |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-14 (time not recorded) | 1.0.8 | `ai-prompting-1.0.8-UNIVERSAL-skill.zip` (`fbcf317b25bd`) | Codex desktop, owner Windows account | standalone local skills folder | install exact post-merge candidate | 47/47 files match; zero extras; one scanned standalone definition | unknown | observed; local gate evidence held by owner | files verified; host load not checked | Codex |
| 2026-10-16T04:29:01.9069391-04:00 | 1.0.8 | `ai-prompting-1.0.8-UNIVERSAL-skill.zip` (`fbcf317b25bd`) | Codex desktop, owner Windows account | standalone local skills folder | recheck installed candidate and explicit skill read | 47/47 files match; zero extras; one standalone definition; core and Codex reference read; authorization comprehension passed | metadata 1.0.8 | observed in current Codex chat; automatic loader origin UNKNOWN; full app restart not established | files verified; host load not checked | Codex |
