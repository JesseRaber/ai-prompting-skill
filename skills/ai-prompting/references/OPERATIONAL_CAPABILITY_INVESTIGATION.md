# Operational Capability Investigation

Use this reference when Manus must determine whether a safe operational mechanism exists across repository code, official platform documentation, CLI/client surfaces, and authenticated management UI.

## 1. Negative-capability closure matrix

Before concluding `METHOD NOT PROVEN`, enumerate the authorized evidence surfaces.

Recommended matrix:

| Surface | Inspected? | Scope searched | Positive finding | Negative finding | Remaining gap |
|---|---:|---|---|---|---|
| Shipped repository code | Yes/No | files/functions | ... | ... | ... |
| Official platform docs | Yes/No | exact pages/sections | ... | ... | ... |
| Current authenticated CLI/client | Yes/No | commands/help | ... | ... | ... |
| Authenticated management UI | Yes/No | settings/panels | ... | ... | ... |

A cross-surface negative conclusion is complete only when each relevant authorized surface is either:
- inspected; or
- explicitly unavailable/out of scope with the gap reported.

If an accessible UI surface may expose controls not present in the CLI, inspect it read-only before declaring the overall platform mechanism unproven.

## 2. CLI syntax is not backend semantics

`command --help` can prove:

- the installed client exposes the command;
- the client accepts particular flags/options.

It does **not** by itself prove:

- backend credential lifecycle;
- whether the server actually supports the operation for this project/task type;
- UID retention/replacement;
- activation timing;
- atomicity;
- reversibility;
- permission model;
- credential regeneration;
- retry/side-effect semantics.

Label such evidence:

`CLI_EXPOSED_CURRENT_CLIENT`

Use `DOCUMENTED_PLATFORM_BEHAVIOR` only when official docs support it.

## 3. Capability semantics matrix

For every operational verb, record:

| Operation | Surface/control exists | Read/write | CLI syntax exposed | Official semantics documented | UID behavior | Credential behavior | Activation timing | Reversible |
|---|---|---|---|---|---|---|---|---|

Allowed evidence statuses:

- `PROVEN`
- `CLI_EXPOSED_ONLY`
- `UI_EXPOSED_ONLY`
- `DOCUMENTED`
- `UNVERIFIED`
- `NOT DOCUMENTED`
- `NOT EXPOSED IN INSPECTED SURFACE`

This prevents a command's existence from becoming a false safe-procedure claim.

## 4. Exact source attribution per operation

Attribute each row to the source that actually proves it.

Example:

```text
Pause:
- CLI: `manus-heartbeat pause --help` exposes pause syntax.
- Official docs: Settings → Schedules page documents pause behavior.
- UID retention: UNVERIFIED unless docs/UI/backend evidence proves it.
```

Avoid umbrella statements such as:

> The CLI and official docs support list, create, update, pause, resume, delete...

when the evidence differs operation by operation.

## 5. Repository token-minting negative evidence

If the shipped application only verifies an incoming platform-issued token and no minting path exists in repository code, conclude:

> Token minting occurs outside the shipped application code or is otherwise not proven by the repository.

Do not infer:

- exact issuer implementation;
- complete claims;
- audience policy;
- expiry behavior;
- credential storage;
- rotation rules.

Verifier-required claims establish only what the application accepts, not the issuer's full contract.

## 6. Transition-model consistency

Before final output, reconcile:

1. capability table;
2. supported-model classification;
3. mutation ledger;
4. sequencing plan;
5. recovery plan;
6. final conclusion.

No later section may assume an operation that an earlier section found unavailable/unproven.

Example contradiction:

```text
Capability finding:
Create has no disabled-on-create option.

Mutation ledger:
Create replacement → later Enable replacement.
```

Correct treatment:

```text
Create replacement appears active immediately.
Risk window begins at creation.
No separate enable step is proven.
```

## 7. State-transition invariants

For each mutation-ledger step verify:

- the prior step actually produces the stated precondition;
- the operation is available in that state;
- the resulting state follows from evidence;
- no hidden assumption is required.

Use:

```text
State before
→ proven operation
→ state after
```

If a state transition relies on unproven platform semantics, label the entire step `CONDITIONAL / UNPROVEN`.

## 8. Cross-system orphan windows

When a platform task and application database row are updated separately, model the orphan/inconsistency window explicitly.

For a create-then-link sequence ask:

- At what point is the new task active/triggerable?
- Can it run before the DB UID is persisted?
- How does the handler behave for an unknown/unlinked task UID?
- Is compensating deletion implemented if DB persistence fails?
- Could an automatic schedule fire during the gap?
- Can the task be created paused/disabled?
- Is the timing window bounded?

If any answer is unknown, do not call the sequence safe or near-atomic.

## 9. Recovery actions need their own proof

A recovery verb is not automatically safe because the matching command exists.

For:

- pause replacement;
- resume old task;
- delete orphan;
- recreate old task;
- restore linkage;

record:

- control/API availability;
- current-state applicability;
- data/credential effects;
- reversibility;
- whether the action could trigger work.

Unknown recovery semantics must be a stop condition, not a fallback instruction.

## 10. Precise uncertainty language

Avoid:

> verifier behavior is unpredictable.

Prefer:

> The credential-minting path/signing key for a newly created platform task is unproven, so compatibility with the currently live verifier cannot be determined from available evidence.

Name the exact unknown.

## 11. Necessary production-metadata queries

When a production read is authorized only `if necessary`:

Before the query:
1. state the unanswered inventory question;
2. explain why repository/docs/platform metadata do not answer it;
3. list exact rows/IDs;
4. list exact columns;
5. confirm no business-data projection.

After the query:
- confirm the actual projection remained within the authorized fields;
- sanitize operational identifiers in the report.

## 12. Intermediate identifier sensitivity

When raw task UIDs or similar operational identifiers are needed for a read-only command:

Prefer, when tooling permits:
- shell variables;
- masked display;
- safe aliases;
- truncated suffixes.

Do not unnecessarily print full identifiers into terminal screenshots/tool output.

This is an execution-surface hygiene rule even when the identifier is not a credential.

## 13. Workspace integrity

For strict read-only investigations:

- capture starting `git status --short` / `--porcelain`;
- capture ending state;
- compare exactly.

A final statement that no repository modification occurred should be backed by that comparison.

## 14. Final capability conclusion

Recommended format:

```text
Repository/application renewal abstraction: NOT IMPLEMENTED / NOT FOUND
Official platform documentation: NOT DOCUMENTED
Current CLI surface: [commands exposed], credential rotation NOT EXPOSED
Authenticated UI: [inspected result] / NOT INSPECTED
Overall exact renewal mechanism: METHOD NOT PROVEN
```

If an authorized surface remains uninspected, say so explicitly rather than implying exhaustive platform coverage.



## 15. Controlled mutation handoff

When an investigation transitions into a separately authorized operational mutation, use `references/CONTROLLED_PLATFORM_MUTATION.md`.

In particular, alias-only identifier requirements apply to the execution transcript, not merely the final chat report. Use hidden shell variables and allowlisted CLI projections where possible.
