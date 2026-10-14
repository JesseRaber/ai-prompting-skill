# Controlled Platform Mutation

Use this reference when Manus is authorized to make a narrow production/control-plane mutation such as pausing, disabling, or otherwise changing a specifically identified platform object.

## 1. Three-layer mutation proof

Every authorized mutation requires three distinct evidence layers:

1. **Pre-state attestation**
   - exact authorized object/alias;
   - stable identity;
   - current enabled/paused state;
   - schedule/config fields relevant to the gate;
   - current running/in-flight state;
   - history/last-execution watermark;
   - population count / neighboring objects when needed.

2. **Mutation acknowledgement**
   - exact authorized operation;
   - sanitized UTC timestamp;
   - command/UI acknowledgement;
   - no unrelated mutation fields.

3. **Independent post-state readback**
   - same object identity remains;
   - intended field/state changed;
   - prohibited fields/configuration unchanged;
   - no in-flight execution;
   - population/object count unchanged unless authorized;
   - history watermark unchanged if claiming no invocation;
   - documented semantic consequence only if supported.

A successful command response alone is not a completed verification.

## 2. Sequential batch ledger

For multiple authorized objects, use a ledger:

| Alias | Precondition | Mutation time | ACK | Immediate readback | Result | Proceed to next? |
|---|---|---|---|---|---|---|

Do not mutate object B until object A's required immediate verification passes.

## 3. Partial-success discipline

If the first mutation succeeds and the second fails:

- preserve object A's new state;
- do not compensate automatically unless explicitly authorized;
- do not retry more than the prompt permits;
- stop and report the exact mixed state.

Classify using the prompt's terminal states, such as:

- `ALL_SUCCEEDED`
- `PARTIAL_SUCCESS`
- `NO_CHANGE_PRECONDITION_FAILED`

## 4. Mutation audit-window watermark

Before the first mutation, record a sanitized watermark sufficient to detect object replacement or execution during the task.

Useful fields:

- stable alias → hidden/raw identity mapping;
- enabled/paused state;
- cron/schedule;
- next-run time when relevant;
- last-executed timestamp;
- most-recent run/history marker or count;
- current `running` result;
- total object count.

After all mutations, capture the same fields.

Strong claim:

> No invocation occurred during this task.

requires a watermark that would necessarily change on invocation, or direct history comparison.

If only current-running state and `last_executed_at` were checked, prefer:

> No invocation was observed during the task window; no running execution was present at the sampled checks and the last-executed timestamp remained unchanged.

unless platform semantics make those checks conclusive.

## 5. Population invariants

To claim:

> No additional task changed.

prove:

- same total task count before/after;
- same identities/aliases;
- only intended target fields changed;
- for any non-target objects, relevant state fields remained unchanged.

If there are uninspected objects, weaken the claim:

> No other change was observed in the inspected inventory.

## 6. Identity aliasing across the entire execution surface

When the prompt requires alias-only handling, apply it to:

- terminal commands;
- CLI JSON output;
- screenshots;
- tool logs;
- temporary files;
- notes;
- final chat.

Prefer:

```bash
# Pseudocode pattern
RAW_LIST="$(platform list ...)"
SOURCE_A_UID="$(extract matching source safely from RAW_LIST)"
SOURCE_B_UID="$(extract matching source safely from RAW_LIST)"

platform pause --task-uid "$SOURCE_A_UID" | jq '{ok, enable}'
```

Do not echo the raw variables.

If the CLI returns raw identifiers, project the output through an allowlist such as:

```text
ok
enabled/paused
cron
last_executed_at
next_execution_at
running_count
```

Omit, unless explicitly necessary:

- raw task UID;
- actor/user ID;
- callback path;
- callback payload;
- headers;
- credential-related fields.

If the tool cannot avoid rendering the identifier and the prompt forbids exposure, report the interface limitation before executing the mutation.

## 7. Operational-output minimization

Do not print the full object if the decision only needs:

- alias mapping;
- enabled flag;
- cron;
- next-run;
- last-run;
- running state.

Use an allowlisted projection.

Execution transcript confidentiality matters just as much as the final response.

## 8. Recalled-context quarantine

A task-ledger reset has two layers:

### Active ledger reset
Every current checklist item maps to the current prompt only.

### Context quarantine
Prior conversation and auto-recalled memories may still exist in the UI, but must not enter the evidence chain.

Do not expand irrelevant `Knowledge recalled` panels.

If unrelated content appears:

```text
CONTEXT_QUARANTINED — not relevant to current task; excluded from reasoning/evidence.
```

Do not reuse prior-task conclusions as current active steps unless the current prompt explicitly makes them accepted evidence.

## 9. Operation name versus state mutation

Be precise in negative closure.

After two authorized pause operations, avoid:

> No task update occurred.

because the task state was updated.

Prefer:

> No task operation occurred other than the two authorized pauses. No cron/path/payload/create/delete/resume/run mutation occurred.

## 10. Semantic consequence proof

Direct state:

```text
enabled = false
```

can establish the stored paused/disabled state.

A stronger statement:

```text
the task is no longer eligible for a scheduled trigger
```

requires documented platform semantics or proven direct behavior.

Do not infer backend scheduling semantics solely from a field name.

## 11. Mutation timestamps

For each production/control-plane mutation, record when feasible:

- mutation UTC timestamp;
- immediate verification UTC timestamp.

If the prompt requests sanitized timestamps, include them in the final report.

## 12. Final mutation reconciliation

Before final output reconcile:

- authorized mutations performed;
- exact pre→post deltas;
- partial-success status;
- task/object invocation activity during the window;
- non-target object invariants;
- repository start/end proof;
- unauthorized mutation classes;
- identifier/confidentiality incidents;
- external artifacts if any.

A successful operational result does not erase a confidentiality or authorization incident.
