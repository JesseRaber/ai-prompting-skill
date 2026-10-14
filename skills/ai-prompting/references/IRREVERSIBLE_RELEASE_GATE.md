# Irreversible Release Gate

Use this reference for merge, checkpoint, automatic publication, deploy, restore, rollback, production-data, credential, deletion, and other hard-to-reverse actions.

## Mutation latch

Start each irreversible phase with:

```text
MUTATION LATCH: CLOSED
```

Use this evidence table:

| Gate | Expected | Observed | Authoritative source | Command/interface status | Freshness | Result |
|---|---|---|---|---|---|---|

Open the latch only when every row is a fresh explicit `PASS`. `UNKNOWN`, `UNVERIFIED`, `PARTIAL`, blank, malformed, stale, or contradictory evidence keeps it closed.

## Fail-closed command discipline

- Run one logical decision check at a time or use a wrapper whose overall failure cannot be masked.
- Record the producer's exit/interface status separately from its output.
- Validate identifiers against expected shape before comparison.
- Treat `fatal`, `error`, unauthorized/authentication failure, timeout, and empty output as failure—not as a SHA, tree, branch, identity, or configuration value.
- Reject unresolved substitutions and error text captured into variables.
- Do not let a pipeline, formatter, or later successful command convert a failed producer into a passing gate.
- Do not open the latch because a task item was checked complete.

## Required-clean workspace

Any working-tree entry is an immediate stop when cleanliness is required.

- Preserve and report sanitized paths/statuses.
- Do not clean, reset, stash, restart, synchronize, or otherwise make the state disappear without separate preservation/recovery authority.
- If a later state is clean, report `dirty → clean` as an unexplained transition until the mechanism is proven.
- Never say the workspace “remained clean” when the recording shows otherwise.

## Freshness barrier

Immediately before the irreversible action, refresh every volatile row. Earlier observations expire after:

- user login/confirmation handoff;
- material delay;
- browser/workspace restart;
- synchronization attempt;
- remote refresh or external mutation;
- contradictory evidence.

## Cross-system identity

Prove separately:

1. authorized PR/head;
2. remote main SHA/tree;
3. exact CI run and tested SHA;
4. local workspace branch/HEAD/tree/clean state;
5. managed workspace identity;
6. checkpoint identity;
7. published version;
8. public runtime.

Do not infer synchronization from exact-main CI. Do not infer exact SHA from a clean workspace.

## Gate-bypass incident

If an irreversible action occurs while the latch should be closed:

1. classify `UNAUTHORIZED GATE BYPASS`;
2. stop further mutations unless separate emergency authority clearly applies;
3. preserve the new external state;
4. record the failed gate and action;
5. do not repair, hide, or replay the transition;
6. request a new residual-action decision.

The later safe stop does not erase the earlier incident. A truthful classification may be:

```text
MERGE OCCURRED AFTER FAILED PRE-MERGE GATE — RELEASE THEN STOPPED BEFORE PUBLICATION
```

## Post-merge authorization topology

Once merge occurs, the original pre-merge authorization is spent. If synchronization/publication is blocked:

- do not “restart from workspace synchronization” under the old packet;
- inventory merged remote state, exact CI, local state, current live version, schedules, and artifacts;
- reconcile dirty files that disappeared or credential checks that failed;
- obtain a new post-merge residual-action authorization covering only remaining work;
- never re-merge or create extra checkpoints.
