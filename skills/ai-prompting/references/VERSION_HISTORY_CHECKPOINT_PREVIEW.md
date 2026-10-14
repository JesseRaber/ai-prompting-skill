# Version History Checkpoint Preview Validation

Use this reference when Manus is asked to validate an existing historical/version-history checkpoint without restoring, publishing, or creating state.

## 1. Surface-scoped authorization

If the prompt authorizes the Version History UI and its existing `Preview` control, stay on that surface.

Do not silently substitute:

- platform API endpoints;
- API-key-backed calls;
- CLI operations;
- internal configuration/connector skills;
- repository checkout;
- local dev server;
- hidden management endpoints.

A read-only backend/API method is still outside scope when only the UI was authorized.

If the UI is difficult to operate, use bounded UI retries. If it remains inaccessible, report the interface limitation rather than broadening the authorization surface.

## 2. Accepted evidence versus gates

Treat sections explicitly labeled `Current accepted evidence`, `Accepted evidence`, or equivalent as premises.

Do not re-run repository/PR/CI checks merely because they are easy to verify. Revalidate only when:

- the prompt explicitly says to verify them;
- the evidence has an explicit freshness requirement;
- new observations contradict the premise.

This keeps a checkpoint-preview task focused on the checkpoint.

## 3. Version History control preflight

Before clicking:

1. visually identify the exact target row/version;
2. record the displayed short version/checkpoint ID;
3. record timestamp/summary/status only as exposed;
4. verify the target row has an explicitly labeled `Preview` control;
5. distinguish it from adjacent `Rollback`, `Restore`, `Publish`, `Deploy`, `Save`, or other mutation controls;
6. stop if control identity or side effects are ambiguous.

Prefer visible UI evidence over HTML scraping.

## 4. Metadata source fidelity

Keep these evidence forms distinct:

- **visually displayed** — clearly readable in the rendered UI;
- **DOM-exposed** — obtained from a narrow selector/accessible text but not fully visible;
- **inferred** — derived from other context.

If the UI shows only `Sat, 9:36 AM`, do not invent a date or timezone.

If the visible summary is truncated but the full text is obtained from a narrow DOM extraction, label it as DOM-exposed full text rather than fully displayed text.

## 5. Avoid broad authenticated page capture

Do not save or grep whole authenticated HTML pages merely to locate one checkpoint/control if visible UI or a narrow DOM selector can do the job.

If capture is unavoidable:

- extract only the narrow required region;
- assume the page may contain account/project identifiers or other sensitive data;
- store only outside the repository;
- add the artifact to the action ledger;
- delete it when no longer required unless retention is explicitly necessary;
- never include raw captured content in the final report.

Tool-generated `terminal_full_output` files also count as external artifacts.

## 6. Cross-surface evidence does not auto-reconcile

If a platform/API checkpoint listing says `none` but the Version History UI visibly shows entries, do not decide one is globally correct unless object scope/identity is proven equivalent.

Report:

```text
API surface: no entries returned for scope X
UI surface: entries visible for project Y
Cross-surface equivalence: UNVERIFIED
```

When the prompt authorizes only the UI, stop using the API result entirely.

For rollback/restore identity disputes, use `ROLLBACK_ARTIFACT_IDENTITY.md`. A Live marker identifies the active entry; it does not by itself prove immutable content lineage or rule out an in-place restore.

## 7. Provenance is not readiness

After clicking Preview, separate:

### Checkpoint association
Example:

> `You are previewing an older version (9954540d)`

This can strongly establish preview-to-checkpoint provenance.

### Preview readiness
The application is not ready merely because the provenance banner is present.

A page still showing:

> Loading preview, please wait…

is `PENDING`, not `PASS`.

### Application health
Public health begins only after the target application surface actually renders and required assets/requests can be observed.

Never write “the preview loads correctly” while the preview is still preparing.

## 8. Asynchronous preview readiness protocol

Checkpoint previews may prepare asynchronously.

The prompt should provide:

- maximum wait budget;
- observation cadence;
- allowed refresh/retry behavior;
- final timeout classification.

Record:

- time Preview was clicked;
- time provenance banner first appeared;
- first loading-state observation;
- any status transition;
- final observed state;
- total wait duration.

Recommended states:

- `PROVENANCE_PASS / READINESS_PENDING`
- `READINESS_PASS`
- `READINESS_FAIL` only on explicit failure evidence
- `READINESS_TIMEOUT / UNVERIFIED` when the wait budget expires

A message such as `Download app and get notified when it's ready` indicates asynchronous readiness, not an application-artifact defect.

Absent a defined wait budget, final wording should be:

> The preview did not become ready during the observed N-second/minute window.

Do not say `never loaded`.

## 9. Browser context isolation

If a `fresh browser context` is required, prove actual isolation.

Acceptable evidence may include:

- new browser profile/context;
- new isolated tab/container documented by the tool;
- explicit fresh-session browser capability.

These are not equivalent:

- user is currently logged out;
- an old app session was not visibly exercised;
- same browser/iframe was reused.

If isolation cannot be established, report `FRESH CONTEXT: UNVERIFIED` and do not authenticate when fresh isolation is a hard prerequisite.

## 10. Dependent workstream gating

Public health must pass before authentication.

Authentication must pass before authenticated route checks.

If preview readiness times out:

```text
Public health: BLOCKED
Authentication: NOT RUN
Dashboard: NOT RUN
Knowledge Base/Data Sources/Approvals: NOT RUN
Analytics: NOT RUN
Diagnostics: NOT RUN
Logout: NOT APPLICABLE
```

Do not mark those workstreams as completed/passed simply because the run reached a terminal classification.

## 11. Progress-state integrity

Use these states for both task-progress labels and the final report:

- `PASS`
- `FAIL`
- `PENDING`
- `TIMEOUT`
- `BLOCKED`
- `NOT RUN`
- `SKIPPED`
- `UNVERIFIED`
- `NOT APPLICABLE`

If an internal checklist only supports a binary checkmark, word the item as a classification task:

> Classify authenticated-route validation after preview readiness result.

Do not use a checked item named:

> Validate authenticated routes

when no authenticated route was run.

## 12. Postcondition readback

After Preview validation, independently re-check the platform state.

Confirm through the Version History/live indicator or equivalent:

- live/published version unchanged;
- no new checkpoint/version created;
- no restore/rollback in progress;
- preview context only.

Do not infer unchanged platform state solely from “I did not click Rollback.”

## 13. Artifact versus validation-infrastructure failure

Use precise classifications:

### Verified known-good rollback candidate
All required provenance/public/authenticated checks passed.

### Rejected
A reproducible checkpoint application/runtime failure was observed with sufficient provenance.

### Unverified — preview readiness/platform limitation
Checkpoint association is proven but the platform preview did not become testable within the authorized wait window.

### Pending
Preview is still preparing and the wait budget has not expired.

Do not turn platform-preview readiness uncertainty into a checkpoint defect.

## 14. Final report requirements

When readiness blocks the task, include:

- target entry metadata and source fidelity;
- Preview-control preflight;
- preview-to-checkpoint provenance;
- fresh-context status;
- Preview click timestamp or relative timing;
- observed wait duration;
- final readiness status;
- each dependent check explicitly `BLOCKED` / `NOT RUN`;
- postcondition readback;
- external capture/artifact ledger;
- any authorization-surface deviation;
- final classification.



## Readiness state machine and stability soak

Maintain a canonical timed state ledger using `references/TIMED_OBSERVATION_AND_EMBEDDED_INTERACTION.md`.

If the landing/sign-in surface is already rendered at T+0:

- readiness is `PASS at T+0`;
- any remaining required T+ observations are a stability soak;
- do not continue describing the preview as preparing/loading.

A visible error badge/toast must be reported separately. Do not say `no errors` while an unresolved error indicator is visible.

## Timed observation accuracy

Anchor T+ checkpoints to absolute targets computed from T0 rather than chaining sleeps.

Periodic checkpoints establish state at those observations only; do not claim continuous visibility unless continuous monitoring actually occurred.

If exact UTC timestamps are required, capture them next to every checkpoint observation.

## Embedded authentication tooling

If authentication requires a fresh context, establish isolation before the first Sign in attempt.

A stale browser snapshot/index failure is a browser-harness event. Reacquire the current page and semantic locator before one bounded retry. If it still fails, classify the authenticated portion as `UNVERIFIED — VALIDATION TOOLING/INTERACTION BLOCKED`.

Do not use preview/bootstrap diagnostics that were authorized only for the `preview not ready` branch after readiness has already passed.

## Classification completeness

Checkpoint-validation prompts should include a tooling/harness-blocked unverified state in addition to preview-unavailable and application-failure states.

If the prompt's mandated taxonomy cannot represent the observed outcome, explicitly report a taxonomy gap rather than forcing the evidence into an incorrect category.


## Interaction recovery and user takeover

For embedded sign-in recovery, use `references/INTERACTION_RECOVERY_AND_MANUAL_HANDOFF.md`.

Do not jump from a stale-snapshot failure to manual fallback without accounting for every method in the ordered ladder. If the browser harness is globally unavailable, later automated methods should be marked `BLOCKED_BY_HARNESS`, not silently skipped.

Once OAuth begins, switch from the pre-auth interaction state to the OAuth-phase state machine. A classification that is valid only when OAuth never begins is no longer applicable after the account chooser appears.

If manual user action is required, distinguish MANUS/USER/PLATFORM actions and verify the resulting browser state directly after control returns.
