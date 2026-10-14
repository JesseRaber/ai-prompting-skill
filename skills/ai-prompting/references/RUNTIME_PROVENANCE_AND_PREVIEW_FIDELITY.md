# Runtime Provenance and Preview Fidelity

Use this reference for preview, rollback, deployment, release, and runtime-health tasks.

## Core rule

`Exact Git head` is not the same claim as `exact running artifact`.

Treat these as separate evidence axes:

1. **Source revision** — repository SHA / tree state.
2. **Runtime process origin** — process command, working directory, process lifetime, watcher behavior.
3. **Build/artifact identity** — immutable build/checkpoint/version ID if available.
4. **Runtime mode** — development server, non-production production-build preview, checkpoint preview, published/deployed.
5. **Configuration identity** — required non-secret config match, without exposing values.
6. **Database target identity** — only if authorized and proven through a non-secret identifier.
7. **Authentication context** — anonymous, existing session, fresh login, service/scheduled token.
8. **Startup/migration behavior** — application startup code versus platform wrapper/runtime behavior.

For a release, also keep distinct:

- authorized PR/head;
- remote main SHA and tree;
- exact CI run and the SHA it tested;
- local workspace branch, HEAD, tree, and dirty state;
- managed workspace identity;
- checkpoint/version identity;
- published artifact;
- public runtime.

A passing exact-main CI run does not synchronize a managed workspace. A clean workspace does not prove it is at the intended SHA.

Keep authentication layers separate: Manus/platform operator authentication, application OAuth, callback/schedule credentials, and repository/connector authentication. Seeing the application's sign-in page does not prove the operator is signed out of the management platform.

## Preview taxonomy

### Workspace development preview

Examples: Vite dev server or similar process watching the current checkout.

Can establish:
- current workspace routes/modules are reachable;
- development-mode behavior for the current files, if process/workspace provenance is established.

Does not automatically establish:
- production build succeeds;
- built JS/CSS assets are healthy;
- immutable artifact identity;
- checkpoint/published behavior;
- production runtime configuration;
- production database target.

### Non-production built preview

A production-mode build running in a non-production environment.

Potentially stronger for shipping behavior, but still requires build SHA/artifact and config/database provenance.

### Version History/checkpoint preview

An immutable historical platform artifact if the platform actually documents/proves that model. Opening it is safe only if preview side effects are documented or otherwise proven read-only.

### Published/deployed artifact

Strongest deployment evidence, but production actions/reads require their own authorization.

## Exact-shipping-path rule

Do not use `exact shipping path` merely because:
- HEAD matches;
- a dev server is running;
- the landing page returns HTTP 200.

Use it only when the specific path under evaluation is exercised through the relevant shipping layers and the required provenance axes are established.

Example for an authenticated data procedure:

```text
source SHA proven
+ appropriate build/runtime mode proven
+ server path exercised
+ authentication context proven
+ driver/database path exercised
+ target identity sufficiently proven
= shipping-path evidence for that procedure
```

Missing axes must be reported as `UNVERIFIED`.

## Startup/migration wording

Repository grep/search can support:

> No automatic migrator found in the application startup code inspected.

It cannot by itself support:

> No migration can run at startup anywhere in the platform.

To make the broader claim, inspect the actual process launch/runtime wrapper or authoritative platform behavior under the task's authorization.

## Long-lived development-server staleness

A clean current checkout does not prove that a previously started server process has reloaded the candidate server code. Treat dev-server staleness as a first-class possibility.

If candidate-specific runtime behavior visibly matches a legacy implementation, that is direct evidence against exact-runtime identity even when Git HEAD is correct. The proper conclusion is that the tested runtime is stale, misrouted, or otherwise not proven to be the candidate; do not score the candidate PASS or FAIL from that runtime.

Where repeated exact-candidate validation matters, prefer adding a future non-secret runtime revision/build endpoint or build metadata mechanism rather than relying on indirect inference.


## Version History readiness versus provenance

For immutable checkpoint previews, keep three axes separate:

1. **checkpoint association** — the preview is tied to the intended version/checkpoint;
2. **preview readiness** — the platform has finished preparing/serving the preview;
3. **application health** — the target application renders and required routes/requests succeed.

A checkpoint banner can establish (1) while (2) is still pending. Neither proves (3).

Use a bounded readiness window and report the observed duration. A preparation timeout yields `UNVERIFIED`, not checkpoint rejection, unless an application/runtime failure is actually observed.
