# Manus Controlled Local Preview Restart + Authenticated Validation Template

```text
Perform one controlled restart and authenticated validation of the existing local development preview for [project].

## Current-task restatement

Before tools, restate:
- mission;
- exact mutation allowance;
- prohibited production/repository actions.

Use only the current prompt's terminology.

## Starting gate

Verify exact repository/PR/head/base/candidate state and clean workspace.

Record old:
- PID;
- PPID;
- PGID/SID;
- process start identity;
- command;
- cwd;
- listener PID/port;
- process-tree/group membership.

Stop if process ownership is ambiguous.

## Shell/secret hard gate

Do not execute commands that source or enumerate secret-bearing env/config files.

Explicitly prohibit:
`source`, `. <env-file>`, `env`, `printenv`, `set`, `.env` dump, `/proc/*/environ`.

If the platform automatically prepends such commands and it cannot be disabled, STOP and report that the shell surface cannot satisfy this task.

## Process authorization

Authorize only:
- graceful stop of the proven target process tree/group;
- one replacement using repository-defined `[dev command]`;
- named wrapper/persistent terminal method;
- temporary log outside repo if necessary.

Before group signaling, prove every group member belongs to the target.
Use bounded waits and re-check identity before escalation.

## Start command / wrapper

Report separately:
- repository-defined application command;
- orchestration wrapper;
- actual listener process.

Prefer a persistent terminal/session over wrappers that alter stdin/watch behavior.

## Fresh-runtime attestation

Prove:
- exact source SHA/branch;
- replacement root PID;
- replacement listener PID;
- PGID/SID;
- start time;
- cwd;
- command;
- wrapper;
- port;
- start occurred after gate;
- old listener gone;
- new listener handles requests.

Classify only as `exact-head local development runtime`.

## Startup-log fence

Record startup-log beginning/offset.
Inspect all startup warnings/errors case-insensitively or structurally.
Classify each and report wrapper-induced warnings explicitly.

## Authentication

State whether fresh OAuth is REQUIRED or merely PERMITTED.

If user takeover is required for interactive confirmation:
- Manus may open the OAuth screen;
- Manus must pause before account selection, `Continue as`, consent, MFA, password, or security confirmation.

Define whether incidental post-login landing-page reads are authorized.

For expected login metadata DML, report:
AUTHORIZED / EXPECTED BY CODE / DIRECTLY OBSERVED / UNVERIFIED.

## Test-window fences

Before each target route/procedure:
- record log offset/inode or equivalent time/request marker;
- inspect only new events after that marker.

Do not identify current requests via historical `tail -n 1`.

## Analytics

Use an actual browser.

For `[procedure]`, separately report:
- visual rendering;
- HTTP/tRPC status;
- duration/retry;
- sanitized allowed response fields;
- visible chart semantics;
- hidden fields actually observed versus UNVERIFIED;
- test-window runtime logs.

If exact response fields are required but raw body is prohibited, authorize a sanitized extractor for only those named fields.

## Diagnostics

Repeat the same fenced evidence approach for the independent Diagnostics procedure.

Do not broaden incidental health-widget failures into task conclusions unless relevant.

## Completion

- perform authorized logout if required;
- leave replacement process running if required;
- confirm process provenance remains valid;
- verify ending `git status --short`;
- track/delete/retain external temp artifacts according to policy.

## Final action ledger

Report:
- authorized + performed;
- authorized + expected but not directly observed;
- authorized + not performed;
- prohibited + not performed;
- external temp artifacts;
- incidents.

Do not use blanket `no DML/session/artifact changes` wording if authorized exceptions occurred.

## Final report

Include exact old and replacement process provenance, startup warnings, OAuth interaction mode, expected-vs-observed login side effects, per-check PASS/FAIL/PARTIAL/UNVERIFIED statuses, test-window correlation method, external temp-artifact status, and remaining limitations.
```
