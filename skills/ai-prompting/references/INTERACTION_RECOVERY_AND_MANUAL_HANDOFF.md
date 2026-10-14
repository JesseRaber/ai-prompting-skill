# Interaction Recovery and Manual Handoff

Use this reference when Manus must recover from browser/embedded-preview interaction failures and may hand control to the user.

## 1. Recovery-ladder ledger

When a prompt specifies an ordered fallback sequence, track every method explicitly.

Recommended ledger:

| Method | Prerequisite | Actor | Status | Evidence / exit condition |
|---|---|---|---|---|
| Fresh semantic snapshot | Browser bridge can read current DOM | MANUS | ATTEMPTED / PASS / FAIL / BLOCKED | ... |
| Keyboard activation | Focus can enter embedded app | MANUS | ... | ... |
| Current-coordinate click | Current screenshot + coordinate action available | MANUS | ... | ... |
| Safe pop-out | Explicit non-mutating pop-out control exists | MANUS | ... | ... |
| Manual intervention | Prior methods exhausted or globally blocked | USER | ... | ... |

Allowed statuses:

- `PASS`
- `FAIL`
- `BLOCKED_BY_HARNESS`
- `NOT AVAILABLE`
- `NOT ATTEMPTED`
- `SKIPPED`
- `NOT APPLICABLE`

Do not omit methods because the run ended early.

## 2. Method prerequisite versus failure

Do not call a method `FAIL` unless it actually ran.

Examples:

- Browser bridge returns 504 before a coordinate click is delivered → `BLOCKED_BY_HARNESS`, not `FAIL`.
- No explicitly labeled preview pop-out exists → `NOT AVAILABLE`, not `FAIL`.
- OAuth already begins at Method 2 → Methods 3/4 become `NOT APPLICABLE`.

A prompt should explicitly authorize manual fallback if the remaining automated methods are globally blocked by the same harness outage.

## 3. Actor attribution

For every meaningful action/state change, record the actor:

- `MANUS`
- `USER`
- `PLATFORM`

Examples:

```text
MANUS: reacquired DOM snapshot
MANUS: attempted keyboard activation
USER: clicked Sign in to continue
PLATFORM: opened OAuth account chooser
USER: clicked Jesse Raber account row
PLATFORM: chooser remained unchanged
```

Never write `I manually clicked` for a user action.

## 4. Manual-handoff protocol

Before takeover, give exactly one requested action.

Include:

1. the exact visible safe target;
2. one click/activation only;
3. prohibited adjacent controls;
4. the expected next visible state;
5. how long to wait;
6. when to return control.

Example:

> Click the `Jesse Raber` account row once. Do not click `Use another account`, `View latest`, or `Rollback to this Version`. Wait up to 5 seconds. If the chooser disappears or the Cabinet Price Analyzer page returns, give control back. If the chooser stays unchanged, give control back without clicking again.

Avoid vague instructions like:

> Try signing in.

## 5. Post-handoff verification

A user message describes attempted action, not resulting state.

Bad transition:

```text
User: "tried to sign in"
→ assume OAuth callback pending
```

Correct workflow:

```text
User: "tried to sign in"
→ inspect current browser
→ chooser still visible
→ state remains OAUTH_CHOOSER
```

Do not advance state until the result is directly observed.

## 6. Authentication state machine

Track authentication explicitly:

```text
LANDING
→ SIGN_IN_ACTIVATED
→ OAUTH_CHOOSER
→ ACCOUNT_SELECTION_ATTEMPTED
→ CALLBACK_PENDING
→ RETURNED_TO_SAME_CHECKPOINT
→ AUTHENTICATED_SHELL
```

Terminal non-application states may include:

```text
PRE_AUTH_HARNESS_BLOCKED
OAUTH_CHOOSER_INTERACTION_BLOCKED
OAUTH_CALLBACK_PROVENANCE_UNVERIFIED
USER_INTERACTION_STALLED
```

Every transition requires direct evidence.

## 7. Bounded manual retries

Do not repeatedly ask the user to click the same unchanged control.

Recommended:

- first precise manual action;
- observe result;
- if unchanged, one clarified retry at most;
- if still unchanged, stop manual repetition and classify the current interaction state.

This avoids accidental double activation and user confusion.

## 8. Ephemeral diagnostic evidence

If a visible warning/error indicator must be inspected, do it before navigation/authentication that may remove it.

Use ordering:

```text
starting gate
→ inspect/classify ephemeral warning
→ begin interaction recovery
```

If the warning disappears before inspection:

```text
Indicator was visible before authentication
Indicator details were not inspected
Later state no longer showed it
Classification: UNVERIFIED / MISSED EVIDENCE
```

Do not use later absence as a substitute for the requested classification.

## 9. Named UI diagnostic versus broad markup

If the prompt authorizes:

> open the red `1 error` indicator once

use that exact UI diagnostic when safely available.

Do not silently substitute:

- whole-page HTML capture;
- broad DOM dump;
- grep of authenticated markup;
- hidden developer surfaces.

If a narrow UI diagnostic cannot be opened because the harness is unavailable, mark the diagnostic `BLOCKED`, not “classified.”

## 10. Error ownership / transport domain

Label every status/error by layer:

- `APPLICATION`
- `OAUTH/IDENTITY PLATFORM`
- `MANUS PREVIEW PLATFORM`
- `BROWSER AUTOMATION HARNESS`
- `UNKNOWN`

Example:

> HTTP 504 — BROWSER AUTOMATION HARNESS timeout; not an application response.

Do not mix browser-extension transport errors into application-health results.

## 11. Classification coverage by auth phase

Checkpoint/auth prompts should cover terminal states after each major transition.

Recommended conservative classes include:

- `VERIFIED KNOWN-GOOD`
- `REJECTED — APPLICATION FAILURE`
- `UNVERIFIED — PRE-AUTH INTERACTION BLOCKED`
- `UNVERIFIED — OAUTH CHOOSER/COMPLETION BLOCKED`
- `UNVERIFIED — CALLBACK/PROVENANCE LOST`
- `UNVERIFIED — AUTHENTICATED VALIDATION BLOCKED`

When writing a prompt, test the taxonomy against every state-machine node:

> If execution stops here, which classification applies?

If no answer exists, the taxonomy is incomplete.

## 12. Waiting-for-user progress state

Manual intervention suspends execution.

While waiting:

```text
Task state: WAITING_FOR_USER
Post-handoff verification: PENDING
Final classification: PENDING
```

Do not show the task as 4/4 complete while user action is still required.

## 13. Side-effect epistemics after incomplete OAuth

No observed OAuth completion does not automatically equal direct proof of zero DML.

Prefer:

> No OAuth callback/completion was observed. Under the reviewed implementation, the authorized auth-metadata update was therefore not expected to have been reached. Direct database DML was not inspected.

Use a stronger zero-DML statement only when the evidence actually proves it.

## 14. Final postcondition readback

After manual intervention, independently read back any required platform postcondition:

- checkpoint banner;
- live/published version;
- no restore/rollback in progress.

`No Rollback click was made` is an action-ledger statement, not a full platform-state readback.



## 15. Failure-domain localization confidence

Use evidence to narrow the failure layer, but do not over-localize beyond what is proven.

Example evidence progression:

```text
MANUS browser automation cannot activate Sign in
→ browser/harness interaction problem remains possible

USER manually activates Sign in and OAuth chooser appears
→ Cabinet Price Analyzer Sign in control is demonstrated functional

USER manually clicks existing account row and chooser remains unchanged
→ failure is now more plausibly in OAuth/identity-platform or embedded-preview handoff
→ exact platform sub-layer remains UNVERIFIED unless directly isolated
```

Prefer:

> OAuth/embedded-preview interaction stalled; exact platform sub-layer unverified.

Avoid:

> The outer Manus OAuth layer is definitely broken.

unless direct evidence proves that component.

## 16. Visible absence is not proof of absence

Use evidence-bounded wording.

Good:

> No visible non-sensitive application runtime failure was observed before authentication stalled.

Bad:

> No application runtime failure occurred.

The latter is too strong when authenticated execution never happened.

## 17. Complete blocked-run reporting

Even when authentication or user interaction blocks the run, explicitly report every requested field.

Use:

```text
Method 1: ...
Method 2: ...
Method 3: BLOCKED / NOT ATTEMPTED
Method 4: NOT AVAILABLE / NOT ATTEMPTED
Red error indicator: MISSED / UNVERIFIED
OAuth began: YES
OAuth completed: NO
OAuth returned to same checkpoint: NOT OBSERVED
Dashboard: NOT RUN
Knowledge Base: NOT RUN
Data Sources: NOT RUN
Approvals: NOT RUN
Analytics: NOT RUN
Diagnostics: NOT RUN
Live-version readback: PASS / UNVERIFIED
```

Omission is not a substitute for `NOT RUN`.

## 18. OAuth-metadata DML wording

If OAuth does not complete and direct DB inspection is prohibited, prefer:

> No OAuth callback/completion was observed. Under the reviewed authentication flow, the authorized authentication-metadata update was therefore not expected to have been reached. Direct DML was not inspected.

Use a categorical statement such as `lastSignedIn was not invoked` only when implementation evidence proves that the write cannot occur before the observed stopping point.

## 19. Taxonomy fidelity

The final classification must use one of the prompt's exact labels.

If none applies, report:

```text
CLASSIFICATION TAXONOMY GAP
Closest conservative evidence state: ...
```

Do not silently invent a new classification label to patch the prompt during execution.


## 20. Human-assisted OAuth sub-workflow ledger

Treat the human branch as a structured mini-workflow, not a single event.

Recommended table:

| Actor | Human substep | Status | Resulting observed state |
|---|---|---|---|
| USER | Existing account selected once | ATTEMPTED / NOT ATTEMPTED | chooser advanced / unchanged / unverified |
| PLATFORM | Wait interval elapsed | PASS | callback / unchanged chooser |
| USER | `Use another account` fallback | ATTEMPTED / DECLINED / NOT NEEDED / NOT ATTEMPTED | credential flow / unchanged |
| USER | Password/MFA/passkey | ENTERED PRIVATELY / NOT REACHED | OAuth continuation / failure |
| PLATFORM | OAuth callback | OBSERVED / NOT OBSERVED | ... |
| MANUS | Post-handoff state verification | PASS | exact visible state |

Do not summarize the branch as `human login failed` without accounting for the authorized substeps.

## 21. Handoff completion criteria

Before the user takes control, make the completion rule explicit.

If the same authorized OAuth attempt permits a fallback such as:

1. click existing account once;
2. wait ~15 seconds;
3. if unchanged, optionally use `Use another account`;

state whether the user should perform the fallback before returning control or whether they may return after the first unchanged step.

When control returns, do not claim the entire assisted procedure was exhausted unless all required/selected substeps are accounted for.

Use `NOT ATTEMPTED`, `DECLINED`, `NOT NEEDED`, or `UNVERIFIED` for missing human substeps.

## 22. Protected credential-entry phase

If the human branch may display or accept:

- password;
- MFA code;
- passkey/security-key prompt;
- recovery code;
- secret OAuth material;

enter a protected manual phase:

```text
Task state: WAITING_FOR_USER_SENSITIVE_ENTRY
Browser automation: PAUSED
Browser snapshots/inspection: PAUSED
Credential-screen screenshots: PROHIBITED
```

Resume browser observation only after the user explicitly returns control and says the sensitive phase is complete or failed.

Do not inspect, transcribe, or retain credential-entry screens.

## 23. Hard pause barrier

While the task is `WAITING_FOR_USER` or `WAITING_FOR_USER_SENSITIVE_ENTRY`:

- post-auth provenance: `PENDING`
- route validation: `BLOCKED`
- Analytics/Diagnostics: `BLOCKED`
- logout: `NOT APPLICABLE YET`
- final classification: `PENDING`

Do not mark dependent workstreams `IN PROGRESS` or complete before control returns and the resulting browser state is directly verified.

## 24. Ambiguous user-return descriptions

A user statement such as:

> I clicked the sign in tab and it is not responding

may not identify which visible OAuth control was used.

First inspect the current browser state.

If the visible state resolves the ambiguity, report only what is proven.

If the ambiguity materially affects whether an authorized fallback remains, ask one concise clarification.

Do not infer:

- existing account selected;
- `Use another account` selected;
- OAuth callback started;
- authentication completed;

from ambiguous user wording alone.

## 25. One OAuth attempt versus human substeps

One explicitly authorized OAuth attempt may include multiple defined substeps.

Do not count:

- existing-account selection;
- `Use another account`;
- password/MFA completion;

as separate OAuth attempts when the prompt defines them as one normal attempt.

Conversely, repeated clicks on an unchanged chooser row are not automatically authorized simply because they occur inside one attempt.

## 26. Avoid vacuous application-health conclusions

If OAuth never returns to an authenticated application:

```text
Authenticated application health: NOT EVALUATED
Reason: OAuth did not complete
```

Prefer this over:

> No application-level failure was observed while an authenticated artifact was proven active.

when no authenticated artifact was actually reached.

## 27. Required assisted-auth report table

For human-assisted authentication, final reports should explicitly include:

- MANUS handoff action;
- USER existing-account selection status;
- required wait outcome;
- `Use another account` fallback status;
- sensitive credential-entry phase reached? yes/no;
- OAuth callback observed? yes/no;
- returned-to-checkpoint provenance observed? yes/no;
- authenticated shell reached? yes/no;
- exact terminal auth state.

This table is required even when all route checks are blocked.
