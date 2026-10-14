# Manus Documentation Reconciliation Template

```text
Perform one narrowly scoped documentation-reconciliation correction on [repository/PR].

## Starting gate

- Verify exact PR/repository state.
- Verify application candidate SHA separately from the current documentation head.
- Record starting `git status --short`.
- Stop and report drift if any required state differs.

## Authorization boundary

This task authorizes documentation corrections only.

Modify only:

- `[authorized documentation file(s)]`

Do not modify application code, tests, configuration, schema, migrations, dependencies, lockfiles, build configuration, production state, credentials, sessions, schedules, checkpoints, or deployment state.

Existing evidence from [prior review] may be read and summarized. Do not reopen runtime/platform investigation unless explicitly authorized.

Inspect only the target docs, retained evidence needed for reconciliation, repository state required for the gate, and validation outputs. Do not perform a general repository review.

Do not reopen solved substantive questions. Reconcile wording/evidence references only.

## Required corrections

### 1. [correction]
[Exact stale wording/evidence and required replacement.]

### 2. [correction]
[...]

## Preserve unchanged conclusions

Do not alter these substantive conclusions:

- [conclusion]
- [conclusion]

## Formatter behavior

Running the formatter is authorized. Retain formatter-induced changes only in the explicitly authorized documentation files. Revert any change to an unauthorized file.

## Validation

Run:

- [format]
- [typecheck]
- [tests]
- [build]
- [audit threshold]

Record exact results.

## Commit and CI

- Commit and push only authorized documentation files.
- Leave the PR open and unmerged.
- Verify exact-head CI.
- Keep application-candidate CI separate from documentation-head CI.

## Expected final state

One documentation-only commit; application candidate unchanged; PR open; release state unchanged/blocked unless explicitly authorized otherwise.

## Required report

Return:

- files changed;
- corrected evidence references;
- validation results;
- new documentation head SHA;
- documentation-head CI;
- application candidate SHA/CI separately;
- PR/base state;
- explicit unresolved items;
- confirmation no unauthorized action occurred.
```
