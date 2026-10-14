# Timed Observation and Embedded Browser Interaction

Use this reference for long-running preview readiness checks, timed soak windows, embedded application surfaces, and browser-harness interaction failures.

## Canonical state ledger

Maintain one authoritative state machine for the target surface.

Example:

```text
PREPARING
→ READY_WITH_WARNING
→ AUTH_INTERACTION_ATTEMPTED
→ AUTH_BLOCKED_BY_HARNESS
```

Every state transition needs:

- UTC timestamp;
- elapsed time from T0;
- direct evidence;
- ownership/domain of any error;
- dependent workstreams newly enabled or blocked.

Once direct evidence proves the landing/sign-in surface rendered, do not later write `still loading` unless a later observation actually shows the preview regressed. If it regresses, record the backward transition explicitly.

Free-form progress notes must not contradict the canonical state ledger.

Keep asynchronous action states distinct:

```text
REQUESTED → ATTEMPTED → PLATFORM ACK → IN PROGRESS → READBACK VERIFIED → COMPLETE
```

Do not announce `synchronized`, `restarted`, `published`, or `ready` before the independent readback exists. If later evidence disproves an optimistic progress statement, retract it immediately and include the retraction in the final incident section.

## Readiness versus stability soak

A maximum readiness window is not the same as a mandatory pending state.

If the application becomes ready before the timeout:

1. mark readiness `PASS` immediately;
2. record the time-to-ready;
3. begin any authorized public/authenticated checks;
4. if the prompt still requires observations through T+N, treat the remaining period as a **stability soak**.

Use wording such as:

```text
Readiness: PASS at T+0
Stability soak: continuing through T+10
```

Do not keep describing a ready preview as `pending` merely because the overall timed task continues.

## Deadline-based scheduling

Anchor all observation targets to T0.

Example:

```text
T0 = 07:03:10Z
T+2 target = 07:05:10Z
T+5 target = 07:08:10Z
T+7 target = 07:10:10Z
T+10 target = 07:13:10Z
```

Before each checkpoint, compute the remaining duration to the absolute target. Do not chain fixed sleeps that accumulate browser/tool overhead.

At every sample, record:

- exact UTC timestamp;
- actual elapsed delta;
- requested target;
- timing drift.

If the prompt allows approximate observations, still preserve the actual measured offset.

## Sampling semantics

Periodic observations prove only the sampled states.

Good:

> The `9954540d` banner was visible at T+0, T+2, T+5, T+7, and T+10.

Bad:

> The banner remained continuously visible throughout the entire period.

Use continuous wording only when actual continuous-monitoring evidence exists.

## Exact timestamp requirements

If the prompt asks for exact UTC timestamps, obtain a clock reading immediately adjacent to each observation.

Do not substitute rounded minute estimates when an exact timestamp is feasible.

## Visible error indicators

A rendered surface with an error badge/toast is not `no errors`.

Classify the state as something like:

```text
READY_WITH_UNRESOLVED_WARNING
```

until the indicator is dispositioned.

Determine ownership if possible:

- embedded application;
- outer preview/platform UI;
- browser/agent harness;
- unknown.

If opening the error details is not authorized or could expose sensitive material, do not open it. Report:

```text
Error indicator present — owner/details UNVERIFIED
```

and keep the related health criterion `PARTIAL` or `UNVERIFIED`.

## Fresh browser context as a hard gate

If authentication requires a fresh browser context, prove isolation **before** clicking Sign in.

Acceptable proof may be:

- newly created browser context/profile;
- explicit isolated browser container;
- tool-provided fresh-session capability.

Not sufficient:

- same browser is currently logged out;
- old session was not visibly used;
- same embedded iframe was reused.

If isolation cannot be established, do not attempt authentication. Classify:

```text
AUTH BLOCKED — FRESH CONTEXT UNVERIFIED
```

## Stale snapshot / stale element recovery

Errors such as:

```text
Page updated since the last snapshot; index ... is unknown
```

indicate stale browser-harness state, not an application-level control failure.

Recovery ladder:

1. acquire a fresh page snapshot/DOM;
2. re-find the control using a stable semantic locator, not the stale index;
3. retry once or within the explicitly bounded browser-recovery budget;
4. if it still fails, classify `HARNESS_INTERACTION_BLOCKED`.

Do not generalize two stale-reference failures into:

> the sign-in control is not actionable through the available interface

unless broader interface incapability is proven.

## Conditional authorization activation

A permission granted under an `if` condition is inactive when that predicate is false.

Example:

```text
If the preview has not loaded by T+10, inspect sanitized bootstrap request metadata.
```

If the application has already rendered, that permission does **not** automatically authorize HTML/network/bootstrap investigation merely because OAuth interaction later fails.

Before each conditional action, explicitly record:

```text
Authorization predicate: TRUE / FALSE
```

If false, do not use the action.

## Classification taxonomy design

When writing prompts, make required classifications mutually exclusive and collectively exhaustive for foreseeable outcomes.

For checkpoint validation, useful classes include:

- `VERIFIED KNOWN-GOOD`
- `REJECTED — APPLICATION FAILURE`
- `UNVERIFIED — PREVIEW/PLATFORM UNAVAILABLE`
- `UNVERIFIED — VALIDATION TOOLING/INTERACTION BLOCKED`
- `UNVERIFIED — REQUIRED PREREQUISITE NOT PROVEN`

If a prompt mandates an incomplete classification set and the observed outcome fits none of them, report:

```text
CLASSIFICATION TAXONOMY GAP
```

Explain the mismatch rather than silently inventing a shorthand category.

## Starting-gate precedence

If the same fact appears in both:

- `Existing evidence`, and
- an explicit `Starting gate` instruction,

the starting gate wins. Re-verify the fact as requested.

Example:

```text
Existing evidence: 14e629fb is live.
Starting gate: Confirm 14e629fb remains live.
```

A prior observation cannot satisfy the explicit freshness gate.

## Postcondition readback

When the final report must confirm platform state such as the live/published version, perform an independent final readback.

Do not substitute:

> I did not click Rollback.

for:

> Version History still shows 14e629fb as Live after the task.

If final readback is unavailable, mark the postcondition `UNVERIFIED`.

## Progress-state integrity

A timed workstream cannot be marked complete before its final required deadline.

If readiness passes early but T+10 observation is still required, task progress should reflect:

```text
Readiness PASS; stability soak IN PROGRESS
```

not:

```text
Timed observation COMPLETE
```

Similarly, blocked authenticated checks should be `BLOCKED/NOT RUN`, not simply checked as completed.

If the task UI only supports binary checkmarks, name items as classification tasks such as `Classify workspace synchronization` rather than actions such as `Synchronize workspace` when the action may remain blocked.

## User-handoff freshness barrier

A login/confirmation handoff suspends execution and expires volatile mutation gates. After control returns:

1. verify the resulting state directly;
2. restate what is proven;
3. refresh every volatile prerequisite;
4. reopen an irreversible-action latch only after all rows pass again.

## Final reconciliation

Before final output:

1. compare every intermediate note against the canonical state ledger;
2. remove stale descriptions such as `still loading` after a rendered landing page was observed;
3. verify sampled-vs-continuous wording;
4. verify exact timing claims;
5. verify classification category fits the prompt taxonomy;
6. verify error ownership is not over-attributed;
7. verify fresh-context and postcondition gates are explicitly reported.



## Human action is not state evidence

When a user takes over the browser, their message proves what they attempted, not what the application/platform did afterward.

Always inspect the current page after takeover before changing the state ledger.

Keep user actions, Manus actions, and platform transitions separately attributed.

## Ephemeral warning ordering

If a warning/error toast is part of the required evidence, inspect it before starting an interaction that may remove it. If it disappears first, report the classification as `UNVERIFIED` rather than reconstructing it from later state or broad page markup.
