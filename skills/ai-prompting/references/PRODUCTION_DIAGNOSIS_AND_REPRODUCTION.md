# Production Diagnosis and Controlled Reproduction

Use this reference for focused, read-only diagnosis of a production symptom such as a missing chart, failed request, empty state, stale asset, or intermittent route failure.

## 1. Preserve the original execution path

Define the symptom as a directly observable condition before inspecting source, logs, or the database.

For a UI symptom, record:

- route and exact target component/region;
- viewport position and whether the target is below the fold;
- selector/accessibility identity or other stable element discriminator;
- loading, error, empty, and rendered states;
- UTC observation time;
- page-issued request identity and completion state.

The controlled reproduction must exercise the same user path that allegedly failed. A manual navigation to a tRPC/API URL is a separate diagnostic probe. It does not prove:

- that the page issued the same request;
- page-request status, timing, retries, or headers;
- client consumption or rendering;
- trace correlation to the browser observation.

Label direct probes separately from page-issued Network evidence.

## 2. Visual evidence is authoritative for visible state

If the target chart/region is visibly rendered with bars or other required content, the canonical observation is `RENDERED`.

Do not narrate `missing`, `not visible`, or `rendering failure` after the recording visibly proves the component is present unless a later observation shows an explicit regression. If it regresses, record the transition with timestamps:

```text
RENDERED → MISSING
```

Scrolling past the target, looking only at the initial viewport, or confusing a neighboring empty card with the target does not establish absence.

Use a small observation ledger:

| Observation | UTC | Viewport/selector | Visual state | Page request state | Evidence |
|---|---|---|---|---|---|

## 3. Fresh-context gate

Treat `fresh browser context` as isolation, not navigation.

These do not prove freshness:

- a new tab;
- `about:blank` in the same profile;
- a hard reload;
- reuse of an already authenticated session.

Require a new browser profile/context/container or tool-provided isolated session. If isolation is required but unavailable, classify the reproduction `BLOCKED — FRESH CONTEXT UNVERIFIED`.

If the prompt allows reuse of an existing session, say so explicitly and do not also call the context fresh.

## 4. Trace-first ordering

Capture the page-issued Network request before a hard reload or direct API probe changes the evidence window.

Preferred order:

1. establish fresh-context/authentication state;
2. open the route once;
3. wait for the target region and relevant requests to stabilize;
4. capture the page-issued request timestamp, status, duration, retry count, path/envelope, and trace IDs;
5. capture the visual state;
6. only then perform a separately authorized cache-bypassing reload;
7. repeat the same page-issued request and visual observations.

If the browser tool cannot expose required Network fields, mark them `UNAVAILABLE/UNVERIFIED`. Do not replace them silently with direct endpoint navigation.

## 5. Evidence-triggered branching

Do not run every diagnostic workstream merely because it appears in the prompt. Define activation predicates.

Examples:

- `HTTP 5xx` activates exact query/EXPLAIN and exception correlation;
- `200 + malformed body` activates mapping/serialization/client-contract tracing;
- `200 + valid data + missing chart` activates client transformation/layout inspection;
- `chart rendered + valid page request` closes defect-localization branches unless the prompt explicitly requires historical reconstruction.

Once direct evidence disproves the assumed current symptom, stop speculative root-cause narration. Continue only the bounded checks needed to classify `not reproduced`, confirm the observation, and preserve final-state proof.

## 6. Causal statements require correlation

Historical or unrelated warnings are not candidate causes without time/request/trace correlation.

Do not turn repeated missing-session warnings into a possible chart cause when:

- the controlled authenticated request succeeded;
- the warnings are outside the request window;
- no trace or request identity connects them;
- the log surface lacks the controlled request.

Use:

```text
Uncorrelated warning observed — causal relevance NOT ESTABLISHED
```

Absence of the request from a bounded log sample proves only a coverage limitation.

## 7. Not reproduced is not automatically transient

Keep these conclusions distinct:

- `NOT REPRODUCED — CURRENT PATH HEALTHY`
- `TRANSIENT FAILURE — PRIOR FAILURE EVIDENCE EXISTS, TRIGGER UNKNOWN`
- `PRIOR OBSERVATION ERROR POSSIBLE`
- `UNKNOWN — REQUIRED REPRODUCTION EVIDENCE INCOMPLETE`

`Transient` asserts that a real failure occurred and later cleared. Use it only when evidence establishes the earlier failure. If the only prior claim may have resulted from a below-the-fold target, wrong component, or intermediate state, do not promote it to a proven transient.

If the prompt's taxonomy forces `TRANSIENT — NOT REPRODUCED` while the evidence also supports observation error, report a taxonomy gap and state the narrower truth.

## 8. Read-only artifact budget

Default artifact budget for a read-only diagnosis is zero unless the prompt explicitly authorizes evidence files.

Do not create or edit:

- repository notes or diagnosis reports;
- external scratch findings files;
- saved authenticated HTML;
- whole-page captures;
- downloaded raw responses or logs.

Prefer in-memory/narrow visible inspection. If an external artifact is explicitly authorized and necessary, predeclare its path, field/content limits, sensitivity, retention/deletion policy, and final ledger entry.

Never source secret-bearing environment files to make a public asset or read-only diagnostic command work. Use a command/interface that does not access secrets, or stop.

## 9. Final gate and report

Freshly re-read every required ending state. `No publication action was performed` is not a substitute for a final Version History/live-state readback.

Report:

- fresh-context status;
- controlled-observation ledger;
- page-issued Network evidence;
- direct probe evidence, separately labeled;
- activated/skipped diagnostic branches and predicates;
- source/log/database evidence actually correlated to the observation;
- every provisional conclusion retracted or corrected;
- artifact and prohibited-access incidents;
- start/end platform, schedule, repository, and session state;
- primary classification plus any taxonomy gap;
- the minimal next evidence or repair, without speculative fixes.
