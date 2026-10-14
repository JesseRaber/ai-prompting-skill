# Read-Only Workspace Integrity

Use this reference whenever Manus is told to perform a read-only, investigation-only, audit-only, or repository-inspection task.

## Required rule

“Read-only” must include both external systems and the local repository workspace.

A strong prompt should say:

> Repository workspace integrity is part of the read-only boundary. Do not create, edit, delete, rename, format, or write to any repository file, including `todo.md`, notes, reports, scratch files, temporary artifacts, generated planning files, or agent bookkeeping files.

## Start/end proof

Require:

```text
git status --short
```

at the start and end, or an equivalent workspace-state check.

The end state must equal the starting state.

If the workspace is dirty before Manus begins:

- record the pre-existing changes;
- do not alter, stage, discard, or normalize them;
- do not use `git reset --hard`, `git clean`, blanket checkout/restore, or other destructive cleanup;
- only revert changes that Manus itself created during the task.

## Accidental task-local writes

If Manus accidentally modifies a file during a read-only task:

1. identify the exact task-created change;
2. revert only that change;
3. confirm no pre-existing user change was disturbed;
4. rerun the workspace-state check;
5. disclose the accidental write and successful cleanup in the final report.

Do not allow Manus to hide this event behind a final statement such as “repository state was unchanged.” The final state may be unchanged even though a prohibited transient write occurred.

## Why this matters

Manus may treat internal planning files such as `todo.md` as agent bookkeeping rather than user-facing repository mutation. Screen recordings have shown visible editing of such files during tasks described as read-only. The prompt must therefore name these artifacts explicitly.
