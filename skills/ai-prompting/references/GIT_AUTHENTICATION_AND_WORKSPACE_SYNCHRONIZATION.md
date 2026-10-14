# Git Authentication and Workspace Synchronization

Use this reference when Manus is authorized to repair Git transport authentication, fetch a pinned remote revision, or synchronize a managed workspace.

## Separate the state planes

Track these independently:

| Plane | Examples | Minimum proof |
|---|---|---|
| Working tree | tracked/untracked files, index-visible changes | starting and ending `git status --porcelain` |
| Git administrative state | `.git/config`, credential-helper entries, refs, `FETCH_HEAD`, branch/HEAD/index transitions | explicit before/after inventory for every authorized component |
| Remote repository | remote SHA/tree, PR/merge/CI metadata | authenticated read-only remote evidence |
| External application/control plane | published version, schedules, executions | fresh pre-action and post-action readback |

A clean working tree does not prove unchanged Git configuration or unchanged refs. After adding a repository-local credential helper, do not say `no repository state changed`; say that no working-tree file changed and report the Git-administrative mutation separately.

## Authentication layers are not interchangeable

Keep these conclusions separate:

- `gh` API/CLI authentication is usable;
- the remote host/path is the authorized target;
- Git selected the intended credential-helper chain;
- the helper produced a credential GitHub accepted;
- fetch succeeded and produced the expected remote-tracking state.

Success at one layer does not prove the next. In particular, successful `gh api` or sanitized `gh auth status` does not prove Git transport authentication.

## Pre-mutation configuration-chain gate

Before changing a helper:

1. validate the sanitized remote host and repository path;
2. inventory relevant helper entries across applicable scopes and their precedence without retrieving credentials;
3. establish whether adding one local entry appends to, overrides, or leaves an earlier helper effective;
4. record a non-secret before-state fingerprint or allowlisted configuration summary;
5. stop if the change could replace or shadow an unrelated account/method outside the authorized scope.

Do not print credential values, credential files, token-bearing URLs, or raw helper output that may contain credentials. Do not inspect secret-bearing environment files merely to make `gh` available. If the command surface auto-injects prohibited environment sourcing, use a safe interface or stop.

## Residual-state contract

Before the helper mutation, the prompt must choose one failure disposition:

- **retain** the exact authorized helper entry for later diagnosis;
- **restore** the exact pre-task helper configuration if fetch fails; or
- **stop for owner decision** with the helper state explicitly retained because cleanup was not authorized.

Cleanup is a separate mutation. Do not improvise removal, and do not leave the ending helper state implicit.

After success or failure, independently read back:

- helper scope and non-secret entry count/fingerprint;
- current branch, HEAD, tree, and working-tree status;
- any authorized ref or `FETCH_HEAD` transition;
- whether branch switching or fast-forwarding actually ran;
- fresh external-state postconditions required by the prompt.

## Fetch and synchronization gates

Treat fetch as a Git-administrative mutation even though it should not edit working-tree files. Record its exit status before interpreting any SHA/tree output. A failed fetch must not be followed by local ancestry checks that depend on newly fetched refs unless those refs are separately proven current.

Tree equality is useful evidence but is not commit identity and does not authorize bypassing an exact-SHA synchronization requirement.

For synchronization, require:

```text
verified remote SHA/tree
→ clean working tree
→ normal switch/create of the authorized branch
→ fast-forward-only update
→ independent branch/HEAD/tree/remote equality readback
```

Never convert a failed fetch, blocked branch switch, or not-run fast-forward into a completed task item. Use `FAIL`, `BLOCKED`, `NOT RUN`, or `SKIPPED` as appropriate.

## Final-report wording

Report all three outcomes separately:

```text
Working-tree files: unchanged / changed / unverified
Git administrative state: exact entries/refs changed, retained, restored, or unverified
External state: fresh post-action result, or last confirmed before [event]
```

A label such as `AUTHENTICATION REPAIR FAILED — NO RELEASE ACTION` may be correct, but it does not erase an authorized helper/configuration mutation. State the residual helper disposition in the classification or immediately beneath it.
