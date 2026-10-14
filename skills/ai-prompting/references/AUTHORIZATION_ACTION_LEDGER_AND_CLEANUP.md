# Authorization, Action Ledger, Session State, and Cleanup

Use this reference whenever a task authorizes narrow side effects such as one login, logout, metadata write, schedule action, commit, or cleanup step.

## Authorization is a maximum boundary

An authorized action is permitted, not automatically required. Prefer the least-mutating path that still satisfies the objective.

If the user cares that a particular path is exercised, make it explicitly mandatory.

Badly ambiguous:

> One OAuth login is authorized.

Clear alternatives:

> A fresh normal OAuth login is REQUIRED even if an existing session is present, because this task validates the login path.

or

> Reuse an already-valid safe session if available. Do not initiate OAuth unless authentication is otherwise unavailable.

## Action ledger

Track:

| Class | Examples | Final-report treatment |
|---|---|---|
| Authorized + performed | OAuth login, `lastSignedIn` update, normal logout | State exactly what happened |
| Authorized + not performed | OAuth allowed but existing session reused | State `NOT PERFORMED` and why |
| Prohibited + not performed | deploy, schema mutation | Confirm not performed |
| Accidental/incident | unexpected write/read/session change | Disclose; do not hide behind clean final state |

Include sensitive reads and evidence artifacts, not only mutations. Sourcing a prohibited environment file, exporting authenticated HTML, printing an operational identifier, or exposing an authenticated-looking URL belongs in the ledger even when no durable platform state changes.

When the prompt supplies an exact task-ledger list, preserve its item count, meaning, and order. Do not retain a prior-task item, collapse a required diagnostic into a mutation step, or mark a blocked/not-run operation complete merely because the overall task has ended.

Record each attempt separately. A parse-rejected read-only query followed by a successful retry is two attempts, not “one query.”

Useful deviation classes:

- `GATE_BYPASS`
- `UNAUTHORIZED_SURFACE_SUBSTITUTION`
- `PROHIBITED_ACCESS`
- `SCOPE_EXPANSION`
- `EXECUTION_SURFACE_EXPOSURE`
- `EVIDENCE_OVERSTATEMENT`
- `PROGRESS_MISCLASSIFICATION`

## Session-state baseline

When sessions are involved, record the meaningful starting state:

- authenticated via pre-existing session;
- unauthenticated;
- fresh task-created session;
- unknown.

Then define the desired ending state.

### Fresh task-created session

If the task initiates authentication, normal logout is usually a sensible cleanup if authorized. Report both the login-side metadata write and the browser-local logout.

### Pre-existing session

Do not automatically destroy a pre-existing session merely because the task has a generic “log out at completion” instruction. Prefer preserving pre-task state unless the prompt explicitly says the existing session may be terminated.

If the user explicitly requires logout even for a pre-existing session, say in advance that browser-local session/cookie state will change.

## Logout semantics

Normal application logout may clear a cookie/local session state without revoking the token server-side. Therefore avoid contradictory language such as:

> Logged out successfully ... no session state changed.

Prefer:

> Authorized browser-local logout cleared the preview session cookie. No server-side session revocation, signing-key change, or other session invalidation was performed.

## Interactive confirmation boundary

When the prompt says interactive credentials or confirmation require user takeover, define confirmation broadly. Account selection, `Continue as ...`, consent, MFA/passkey, password entry, and identity/security challenges all count.

Manus may navigate to the authentication screen if authorized, but should pause before selecting or confirming the user's identity unless the prompt explicitly authorizes agent completion.

## Side-effect epistemic status

Do not confuse an authorized expected side effect with an observed one.

For each permitted write, record:

```text
Authorization: authorized / prohibited
Expected by implementation: yes / no / unknown
Directly observed: yes / no
Conclusion: observed / expected-not-observed / unverified
```

Example:

```text
users.lastSignedIn:
- authorized: yes
- expected by reviewed login implementation: yes
- directly observed: no (direct DB inspection prohibited)
- status: EXPECTED, NOT DIRECTLY VERIFIED
```

## Exception-aware closure

If an authorized exception occurred, scope the final negative confirmation around it.

Bad:

> No DML or session change occurred.

Better:

> The authorized normal login may have produced the expected authentication-metadata update, and the authorized logout cleared the browser-local preview session. No **other** DML, session invalidation, configuration, schedule, schema, repository, or deployment mutation occurred.

## Cleanup after a stop condition

Once a hard prerequisite fails:

1. stop all optional validation branches;
2. perform only required cleanup and final-state proof;
3. avoid opening unrelated routes to reach cleanup controls;
4. use a small bounded number of safe UI attempts;
5. if cleanup remains inaccessible, report `CLEANUP BLOCKED` rather than escalating into broader exploration.

Do not let cleanup consume the majority of a narrowly scoped investigation unless security risk justifies it.

For configuration changes such as credential-helper installation, define the failure disposition before mutation: retain, restore the exact pre-task state, or stop with the residual change explicitly disclosed. Cleanup authority does not arise automatically from repair authority.

## Irreversible partial progress

An irreversible action changes the remaining authorization topology. If a merge succeeds but synchronization/publication does not:

- preserve the merged remote state;
- do not re-run the merge;
- do not continue later phases under the old pre-merge authorization;
- inventory the exact remaining work and incidents;
- obtain a new residual-action authorization.

A later correct hard stop does not erase an earlier gate bypass.

## Final report coverage

Every requested field gets an explicit status. If an authorized login was not performed, write:

```text
OAuth login: NOT PERFORMED — existing safe authenticated session was reused.
Expected auth-metadata DML: NONE in this run.
```

Do not omit a field because the condition did not occur.


## Sequential production/control-plane mutations

For multiple narrow authorized mutations, maintain a per-object ledger with:

- precondition;
- mutation attempt/time;
- command/UI acknowledgement;
- independent immediate readback;
- resulting state;
- permission to proceed to the next object.

Do not treat a mutation acknowledgement as the postcondition proof.

If a later object fails after an earlier mutation succeeded, preserve the successful authorized state unless compensation was explicitly authorized.

Use exception-aware closure:

> The two authorized pauses changed task enabled state. No other task operation or repository/database/configuration mutation occurred.

rather than:

> No task update occurred.
