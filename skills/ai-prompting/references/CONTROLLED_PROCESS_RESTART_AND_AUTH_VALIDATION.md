# Controlled Process Restart and Authenticated Validation

Use this reference when Manus is authorized to restart a local preview/dev process and then perform authenticated browser validation.

## Process identity before signaling

Before sending any signal, record:

- root PID;
- PPID;
- PGID and SID when available;
- process/kernel start identity;
- command;
- cwd;
- child tree / process-group membership;
- listening port and actual listener PID.

Do not assume the wrapper/root PID is the network listener.

Before signaling a process group, prove every current member belongs to the authorized target. Re-check PID identity/start time before escalation so PID reuse cannot redirect a signal at an unrelated process.

## Graceful restart ladder

Prefer:

1. identify the complete authorized tree/group;
2. send the normal graceful termination signal;
3. wait a bounded interval;
4. re-inspect surviving members and port ownership;
5. if escalation is explicitly authorized, signal only the still-proven authorized target;
6. confirm the old listener is gone and the target port is released.

Avoid broad `pkill`, name-only matching, or unconstrained process-group signaling.

## Application command versus wrapper

Report separately:

- **repository-defined application command** — e.g. `pnpm run dev`;
- **orchestration wrapper** — e.g. shell, `nohup`, terminal multiplexer, supervisor;
- **actual listener process** — the child that owns the local port.

A wrapper can change stdin/stdout, process lifetime, signal behavior, or watcher semantics. Do not call a wrapped invocation identical to the ordinary interactive dev command unless that equivalence is actually proven.

If the dev watcher expects stdin, prefer an existing persistent terminal/session over detached execution that closes or alters stdin.

## Replacement provenance

After restart, prove:

- source branch/SHA;
- replacement root PID;
- replacement listener PID;
- PGID/SID if relevant;
- start time;
- cwd;
- repository-defined start command;
- wrapper command if any;
- local port;
- old PID/listener no longer serving;
- replacement process started after the starting gate;
- preview requests are handled by the replacement listener.

Call this an **exact-head local development runtime** only when those claims are supported. It is still not an immutable build/checkpoint/published artifact.

## Startup-log baseline

Immediately after startup, inspect the startup log from its beginning or a known clean offset.

Classify every warning/error observed during startup:

- application error;
- database/driver error;
- configuration error;
- migration/schema action;
- wrapper/harness warning;
- benign framework/watch warning;
- unknown.

Do not rely on brittle case-sensitive searches such as only `grep 'error'`; they can miss `Error:`. Prefer structured logs or scoped case-insensitive parsing.

If the wrapper itself causes a warning such as closed-stdin/watch-mode `EBADF`, report it explicitly and explain the evidence for treating it as nonfatal.

## Temporary-artifact ledger

If process output is redirected to a temporary file outside the repository, track:

- path/category;
- purpose;
- whether it may contain sensitive material;
- whether the running process still depends on it;
- retained versus deleted at completion.

`No repository files changed` does not mean `no task artifacts were created`.

## OAuth interaction boundary

If the prompt requires user takeover for interactive confirmation, the following count as confirmation steps:

- selecting an account;
- clicking `Continue as ...`;
- consent approval;
- password entry;
- MFA/passkey;
- security challenge;
- account switching.

Manus may navigate to the OAuth screen if authorized, but it must pause before identity selection/confirmation unless the prompt explicitly authorizes agent completion.

## OAuth callback read footprint

Login/callback may land on a default route that automatically fetches unrelated application data.

Before authentication, define one of:

- those incidental reads are explicitly authorized;
- the callback can safely target the intended validation route;
- unavoidable incidental reads must be disclosed.

Do not claim that only Analytics/Diagnostics reads occurred if the login landing page automatically fetched dashboard/business data.

## Side-effect epistemic status

For login metadata such as `users.lastSignedIn`, use separate labels:

- `AUTHORIZED`;
- `EXPECTED BY CODE`;
- `DIRECTLY OBSERVED`;
- `INFERRED`;
- `UNVERIFIED`.

If direct DB inspection is prohibited, a normal login may make the write expected but not directly observed. Do not say it definitely occurred unless evidence supports that.

## Test-window fencing

Do not identify the current request merely by `tail -n 1` across a historical log.

Before each target browser action, record a safe correlation boundary, such as:

- log inode + byte/line offset;
- monotonic timestamp;
- request sequence marker;
- tool-provided request ID.

Inspect only events after that boundary and correlate by route/procedure and time.

## Network evidence versus semantic evidence

A successful protected request and a rendered chart establish different things.

- HTTP/tRPC success can prove the request path was exercised, subject to runtime provenance.
- Visible chart labels/order prove visible UI semantics.
- Hidden `bucketId` values are not proven by a chart unless displayed.
- Exact averages are not proven unless displayed or extracted by an explicitly authorized sanitized response-field parser.

If the prompt requests fields that cannot be safely observed under its own redaction rules, mark them `UNVERIFIED`.

## Exception-aware closure

If the task authorizes and performs a restart, OAuth login, possible login-metadata DML, temp-log creation, or logout, do not finish with blanket wording such as:

> no process/session/DML/artifact changes occurred.

Prefer:

> Authorized restart/login/logout/temp-artifact activity occurred as listed; no **other** repository, production, configuration, schedule, schema, or deployment mutation occurred.


## Browser stabilization and harness separation

After OAuth callback or route navigation, wait for the target request/render cycle to settle before making a final UI claim.

Prefer evidence such as:

- callback completed;
- target route is stable;
- loading indicators cleared;
- target network requests settled;
- the relevant UI/chart/diagnostics region is present in a stable state.

Treat earlier empty/loading states as **provisional**, not final. If a later stable state contradicts the provisional observation, reconcile it explicitly.

Also separate tool/harness problems from application problems:

- failed click delivery;
- browser-agent reconnect;
- `Handling browser issue`;
- automation focus problems;
- wrapper/terminal transport warnings.

These are not candidate application failures unless independent browser/runtime evidence shows the application itself failed.
