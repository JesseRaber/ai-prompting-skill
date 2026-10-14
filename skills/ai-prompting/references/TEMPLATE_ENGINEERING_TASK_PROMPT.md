# Manus Engineering Task Prompt Template

```text
Perform [one-sentence narrowly scoped mission].

## Current-task restatement

Before using tools, restate the current mission and authorization level in one sentence using only this prompt. If the restatement introduces a different phase/task, re-read this prompt before acting.

## Starting gate

Before acting:

- Verify [repository / PR].
- Verify exact head: `[SHA]`.
- Verify base/main: `[SHA]`.
- Verify [candidate/runtime identity if relevant].
- Record starting `git status --short` when workspace integrity matters.
- Stop and report drift if any required condition fails.
- Do not mark a gate complete until every conjunct is directly supported. If runtime identity is required, Git HEAD + clean tree + running process is not enough by itself.

## Authorization boundary

This task authorizes only:

- [authorized action]
- [authorized action]

Do not:

- [application/schema/config mutation not authorized]
- [production read/write not authorized]
- [credential/session action]
- [schedule action]
- [merge/checkpoint/publish/deploy/restore]

Unless explicitly stated below, this boundary applies to every workstream.

For every narrow authorized side effect, state whether it is REQUIRED or merely PERMITTED. Authorization is a ceiling, not a checklist obligation. Prefer the least-mutating path that still satisfies the objective unless a specific path is itself the acceptance criterion.

[For read-only tasks:]
Repository workspace integrity is part of the read-only boundary. Do not create, edit, delete, rename, format, or write to any repository file, including `todo.md`, scratch files, notes, reports, temporary artifacts, or agent planning files.

Inspect only [required resources]. Do not perform a general repository review.

[When some configuration is allowed but secrets are prohibited:]
Do not source, dump, enumerate, or broadly read secret-bearing environment/configuration sources merely to verify one permitted key. Use a narrow secret-preserving predicate/interface; otherwise report UNKNOWN.

## Evidence rules

Use this hierarchy:
1. [highest-quality evidence]
2. [runtime/test evidence]
3. repository implementation
4. official documentation
5. accessible management interface
6. inference

Do not promote inference over contradictory direct evidence.

Known evidence:

- Evidence: [fact]
  - Establishes: [what it proves]
  - Does not establish: [what remains unknown]
  - Prohibited inference: [what not to conclude]

## Runtime/artifact provenance [when applicable]

Report separately:
- source SHA;
- runtime process/workspace provenance;
- build/artifact/checkpoint identity;
- runtime mode;
- non-secret configuration identity;
- database target identity if authorized;
- auth/session context;
- startup/migration layer inspected.

Do not call a workspace dev preview an exact shipping artifact unless the relevant artifact/runtime axes are proven. Do not navigate to auto-querying protected routes until runtime identity prerequisites are established, unless that one request is explicitly authorized as the provenance probe.

## Workstream A — [name]

[Exact actions.]

Stop condition: [termination condition].
Allowed result: [controlled status vocabulary].

## Workstream B — [name]

[Exact actions.]

Stop condition: [termination condition].
Allowed result: [controlled status vocabulary].

## Authorized edits / mutations

Modify only:

- `[path/resource]`

Do not modify anything else.

Formatter behavior:
- [what formatter-induced edits are allowed]

## Validation

Run:

- `[command]`
- `[command]`

For each command, record pass/fail and whether it changed files.

For each requested acceptance criterion, report: PASS | FAIL | PARTIAL | UNVERIFIED | NOT APPLICABLE. Do not mark a parent criterion PASS unless every required subcheck passed.

## Commit / operational state

- [commit/push rules]
- [PR merge rule]
- [CI verification rule]

## Expected final state

[Concrete invariant.]

## Required final report

Return:

1. Starting and ending state.
2. Files/resources inspected.
3. Files/resources changed.
4. Evidence and controlled-status conclusions.
5. Validation commands and results.
6. CI/runtime evidence if relevant.
7. Explicit unresolved items.
8. Separate authorization required for any deferred action.
9. Confirmation of prohibited mutations **and prohibited reads/accesses** not performed.
10. For read-only tasks, ending `git status --short` and confirmation that it matches the starting state; disclose any accidental task-local write even if reverted.
11. Action ledger: authorized+performed, authorized+not performed, prohibited+not performed, incidents.
12. When sessions matter, starting/ending browser-auth state and explicit disclosure of any authorized logout/local-cookie change.

Give every requested report field an explicit status: PASS / FAIL / PARTIAL / UNVERIFIED / NOT PERFORMED / NOT APPLICABLE as appropriate.
```
