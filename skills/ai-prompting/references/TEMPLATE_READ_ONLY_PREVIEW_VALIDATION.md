# Manus Read-Only Preview / Rollback Validation Template

```text
Perform one strictly read-only preview and rollback-candidate validation for [project/PR].

## Current-task restatement

Before using tools, restate in one sentence the mission and allowed mutation level using only this prompt. If the restatement imports another task/phase (for example “merge-window”), re-read this prompt before acting.

## Accepted-evidence handling

If the prompt supplies `Current accepted evidence`, treat it as a task premise. Do not re-verify it unless this task explicitly requests freshness verification or new evidence contradicts it.

Do not silently convert accepted premises into an extra repository/PR/CI starting gate.

## Starting gate

- Verify exact PR/head/base/candidate state.
- Record starting `git status --short`.
- Record starting browser auth state when sessions matter.
- Stop on drift; do not reconcile or mutate.

If runtime identity is part of the gate, do not infer it from Git HEAD + clean tree + a running watcher. Prove the runtime revision independently before navigating to routes that auto-trigger protected requests.

If the only runtime discriminator is a protected candidate-specific request, authorize that one minimal probe here, define its allowed side effects/output, and stop if it indicates a stale runtime.

## Global read-only boundary

Authorize only the named inspection surfaces.

Repository workspace integrity is part of the boundary. No file writes, agent notes, formatting, branch changes, commits, pulls, syncs, resets, checkpoints, publish/restore, production writes, login/DML, schedule mutation, schema actions, or other unnamed side effects.

If secret-bearing configuration exists, do not source/dump/enumerate it merely to test one permitted variable. Use a narrow safe predicate or return UNKNOWN. Redaction rules apply to terminal/tool output and temporary captures, not only the final answer.

## Authorization versus requirement

For each narrow authorized mutation (login, logout, metadata update), say whether it is REQUIRED or merely PERMITTED.

- If a safe pre-existing session may be reused, state whether it must be preserved at the end.
- If a fresh OAuth flow is the acceptance criterion, say it is REQUIRED even if a session already exists.
- Do not create an authorized side effect merely because it is permitted.

## Interface/surface boundary

Authorization is surface-specific.

If this task authorizes a Version History UI, do not substitute API/API-key, CLI, internal configuration skills, repository checkout, or local development preview unless those surfaces are explicitly authorized.

Use bounded UI retries. If the authorized interface remains inaccessible, report the limitation rather than broadening scope.

## Preview action preflight

Classify each proposed preview action before executing it:

- SAFE READ — documented/proven side-effect-free;
- MUTATION — known to create/save/restore/publish/change state;
- UNKNOWN SIDE EFFECT — side effects not documented/proven.

Execute only SAFE READ actions. Do not “try” an UNKNOWN action to discover its behavior.

## Runtime provenance

Keep these separate:

1. source SHA;
2. runtime process/workspace provenance;
3. loaded server revision / candidate discriminator;
4. build/artifact/checkpoint identity;
5. runtime mode (workspace dev / built preview / checkpoint preview / deployed);
6. non-secret configuration identity;
7. database target identity if authorized;
8. auth/session context;
9. application startup/migration behavior versus platform wrapper behavior.

A source-head workspace dev preview is not automatically an exact running candidate or exact shipping artifact.

## Timed observation state ledger

If the task has timed checkpoints, create one canonical state ledger.

Record for each observation:

- target offset;
- exact UTC time;
- actual elapsed offset;
- provenance state;
- readiness state;
- visible warning/error indicator and ownership;
- whether public/authenticated workstreams are enabled.

Once readiness passes, label the remaining timed period a stability soak if observations must continue.

Use absolute target deadlines from T0 instead of chained fixed sleeps.

## Asynchronous readiness

For an existing checkpoint/version preview, separate:

- preview-to-checkpoint provenance;
- preview readiness;
- public application health.

A provenance banner can prove checkpoint association while the application remains `PENDING`.

Define a maximum preview wait budget and observation cadence. Record the total observed wait. Do not call a loading state healthy or failed before it resolves or the wait budget expires.

Use:
`PENDING | PASS | FAIL | TIMEOUT/UNVERIFIED`.

If no wait budget was specified, say:
`did not become ready during the observed N-second/minute window`
rather than `never loaded`.

Treat `Download app and get notified when it's ready` or equivalent as asynchronous platform-readiness evidence, not application-artifact failure.

## Health-check evidence semantics

Use only claims supported by the specific check:

- root HTTP 200 = route/shell reachable;
- source-module HTTP 200 on Vite = dev source module served;
- browser execution without fatal error requires actual browser/runtime evidence;
- production asset health requires production-build asset evidence;
- anonymous 401 = auth gate reached, not DB procedure execution;
- authenticated procedure success = only the layers actually exercised and whose provenance is proven.

Browser navigation is active: a React route may auto-fire queries. Do not open a gated route until its prerequisites are proven.

## Ordered interaction-recovery ledger

If the task provides a recovery sequence, create a method ledger before attempting it.

For each method record:
- prerequisite;
- actor;
- status;
- evidence;
- exit condition.

Do not invoke manual fallback until every earlier method is `FAIL`, `BLOCKED_BY_HARNESS`, `NOT AVAILABLE`, or `NOT APPLICABLE` according to the prompt.

If a visible warning/error must be inspected, do so before authentication/navigation can remove it.

## Human-assisted authentication mini-workflow

If user takeover is part of the task, create a human-substep ledger before handoff.

Specify:
- exact first click;
- required wait;
- allowed fallback inside the same OAuth attempt;
- whether the user should perform that fallback before returning control;
- expected success/failure state.

If password/MFA/passkey entry may appear, enter `WAITING_FOR_USER_SENSITIVE_ENTRY` and suspend browser inspection until control returns.

While waiting, do not advance post-authentication workstreams.

On return, inspect the actual browser state first. If the user's description is ambiguous and the visible state does not resolve which substep occurred, ask one concise clarification.

## Embedded sign-in recovery

If Sign in is embedded and browser automation reports a stale snapshot/index:

1. refresh the browser snapshot/DOM, not necessarily the page;
2. reacquire the button using a semantic locator;
3. retry within the bounded harness-recovery budget;
4. if still blocked, classify the auth checks as tooling/harness blocked.

Do not call the application control inherently unactionable based only on stale-reference errors.

Conditional diagnostics remain gated by their original predicate.

## Fresh-context proof

If a fresh browser context is required, prove isolation. A logged-out same browser is not automatically a fresh context.

If isolation cannot be proven, mark `FRESH CONTEXT: UNVERIFIED` and stop before authentication when fresh isolation is a hard prerequisite.

## Requested-check coverage

Return one status for every requested check:

PASS | FAIL | PARTIAL | UNVERIFIED | NOT APPLICABLE | NOT PERFORMED

Never silently collapse an untested subcheck into a parent PASS.

## Historical evidence

Label historical logs and retained evidence as historical. Do not use them to establish current runtime behavior unless time/request correlated.

Use only task/project-relevant retained context; ignore unrelated recalled user/project memory.

## Preview-dependent gating

Do not run or mark dependent workstreams complete when readiness has not passed.

If the preview remains loading and reaches timeout:

- public health: `BLOCKED` or `UNVERIFIED`;
- authentication: `NOT RUN`;
- authenticated routes: `NOT RUN`;
- Analytics: `NOT RUN`;
- Diagnostics: `NOT RUN`;
- logout: `NOT APPLICABLE`.

If task-progress tooling only has checkmarks, phrase work items as classification steps rather than implying successful execution.

## Stop and cleanup behavior

If a hard prerequisite fails:

- stop downstream Analytics/Diagnostics/other optional paths immediately;
- preserve any evidence already generated naturally;
- perform only explicitly required cleanup and ending-state proof;
- do not navigate through unrelated data routes to find logout;
- bound cleanup attempts and report CLEANUP BLOCKED if the normal control cannot be reached safely.

If logout is required, report the browser-local session change explicitly. Do not later claim that no session state changed.

## Rollback classification

Only classify a checkpoint/version as verified known-good when the required public and authenticated evidence is actually available under this authorization.

If opening a checkpoint preview has unknown side effects, do not open it. Report the platform/manual verification needed.

## Postcondition readback

After using a high-risk-adjacent `Preview` control, re-read the platform state through Version History/live indicators.

Prove:
- live/published version unchanged;
- no checkpoint/version created;
- no restore/rollback in progress.

Do not infer these solely because no mutation control was intentionally clicked.

## Ending proof

- Run `git status --short` again.
- Ending workspace must match start.
- Report any transient task-created write even if reverted.
- Also report any accidental protected-source/secret-bearing access even if no value was printed.
- Report ending browser-auth state and whether it differs from the start.

## Final action ledger

Report explicitly:

- authorized + performed;
- authorized + not performed;
- prohibited + not performed;
- incidents/accidental accesses or mutations.

## Final report

Return an explicit status for every requested field, including NOT PERFORMED / NOT APPLICABLE / UNVERIFIED. Include:

- source/repository gate;
- runtime provenance matrix;
- per-check coverage matrix;
- preview type actually tested;
- exact claims established and claims not established;
- login/session action ledger and expected DML actually incurred;
- rollback classifications;
- separate authorization/manual steps still required;
- mutations: none / authorized only / incident;
- prohibited protected reads: none / incident;
- accepted risks distinguished from technically remediated issues;
- release state.
```
