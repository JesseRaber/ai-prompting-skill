# Manus Controlled Release Execution Template

```text
Execute only the authorized release phases below.

## Prompt transport preflight

Before tools, confirm this packet contains no `NaN` items, empty requirement bodies, truncation, unresolved authority, or broken identities.

If malformed:
PROMPT TRANSPORT CORRUPTION — STOP WITHOUT MUTATION

## Mutation latch — initially closed

Do not merge, checkpoint, publish, restore, roll back, or mutate production until every required row is a fresh PASS.

Any dirty workspace, failed command, authentication/fatal/error output, empty or malformed identifier, timeout, stale observation, or contradiction is a hard stop. Error text is never evidence data.

After user handoff, login confirmation, material delay, workspace restart/synchronization, or external mutation, refresh all volatile rows immediately before the irreversible action.

## Authorization

- Exact authorized operations: [LIST]
- Exact objects/interfaces: [LIST]
- Prior irreversible attempts and whether they consume this authorization: [LIST]
- Current-task and cumulative attempt limits: [LIST]
- Accepted unavoidable side effects: [LIST]
- Prohibited access/actions: [LIST]

## Gate matrix

For every row record:
expected | observed | authoritative source | command/interface status | freshness | PASS/FAIL

MUTATION LATCH remains CLOSED unless every row is fresh PASS.

## Phase execution

For every phase:
- entry gate;
- exact authorized action;
- ATTEMPTED status;
- platform/command acknowledgement;
- independent readback;
- timeout and retry limit;
- stop state;
- next-action permission.

Never narrate synchronized/published/ready before independent readback.

For rollback/restore, separate the Live control-plane entry, immutable artifact lineage, serving-content identity, and route behavior. A Live marker or missing restored-from row is not content proof. If the authorized evidence cannot distinguish candidate content from an in-place fallback restore, report `ROLLBACK UNVERIFIED — PRODUCTION IDENTITY UNKNOWN` and do not spend another attempt.

## Gate-bypass rule

If an irreversible action occurs while a gate is not fresh PASS:
- freeze later mutations;
- classify the gate bypass;
- preserve current external state;
- do not repair, repeat, or hide the action;
- request a new residual-action authorization.

After merge, do not resume the original packet at a later phase. Create a new post-merge packet covering only remaining work.

## Final report

Return:
- prompt-render status;
- gate matrix;
- action/attempt ledger;
- material state transitions;
- artifacts and execution-surface incidents;
- exact final readbacks;
- rollback status;
- production identity and authorization/gate compliance as separate classifications;
- provisional conclusions that were retracted or corrected;
- Incidents and deviations;
- corrected overall classification.
```
