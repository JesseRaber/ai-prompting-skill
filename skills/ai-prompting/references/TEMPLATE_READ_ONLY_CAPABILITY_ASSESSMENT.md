# Manus Read-Only Capability Assessment Template

```text
Perform one read-only capability assessment concerning [capability/problem].

## Starting and workspace gate

- Confirm the exact repository/application context being inspected.
- Record `git status --short` before investigation.
- Do not modify the workspace.

## Authorization boundary

Investigation only.

Do not:

- retrieve, copy, quote, decode, test, reuse, or store exposed credentials;
- create, edit, delete, rename, format, or write to any repository file, including `todo.md`, notes, reports, scratch files, temporary artifacts, or agent planning files;
- alter sessions, keys, secrets, configuration, schedules, production data, schema, migrations, repository state, checkpoints, or deployment state;
- perform actions outside the exact read-only sources authorized below.

Inspect only the repository areas, official documentation, and authenticated management surfaces necessary to answer this capability question. Do not perform a general repository review.

Do not source, dump, enumerate, or broadly read secret-bearing environment/configuration sources unless the whole source is explicitly authorized. If one permitted non-secret field must be checked, use a narrow one-key predicate/interface; otherwise report UNKNOWN.

## Required investigation

Assess these layers separately:

1. Application/runtime capability.
2. Official platform documentation.
3. Accessible authenticated management interface.
4. Internal/operator platform capability, only if directly evidenced; otherwise mark UNKNOWN.

Use these statuses:

- Application/runtime: SUPPORTED | UNSUPPORTED | UNKNOWN
- Official docs: DOCUMENTED | NOT DOCUMENTED | UNKNOWN
- Accessible UI: EXPOSED | NOT EXPOSED | UNKNOWN
- Overall operator capability: PROVEN AVAILABLE | NO PROVEN MECHANISM | UNVERIFIED

Negative-evidence rules:

- repository absence may support unsupported-at-application-layer;
- docs absence means not documented;
- UI absence means not exposed/unverified;
- do not infer absence of internal/operator tooling.

Search official platform documentation first. Do not spend time on unrelated vendor implementations unless needed only for conceptual explanation.

For every quantitative or security-sensitive claim used in the recommendation, cite the exact repository or official-documentation evidence.

If the capability cannot be proven after these sources are exhausted, stop and classify it precisely. Do not speculate or broaden the investigation.

## Alternatives / blast radius

If the desired targeted capability is unavailable or unverified, describe non-executed alternatives only.

For each alternative, distinguish:

- expected effect;
- proven versus possible blast radius;
- user/session impact;
- scheduled callback impact;
- monitoring needs;
- security-sensitive rollback considerations;
- separate authorization required.

Do not execute any alternative.

## Ending workspace proof

Run `git status --short` again.

The ending state must match the starting state. If Manus accidentally created a task-local change, revert only that change, preserve all pre-existing changes, and disclose the incident.

## Final report

Return:

- application/runtime status;
- official-documentation status;
- accessible-management-interface status;
- overall operator capability;
- evidence/source for each conclusion;
- alternatives and qualified blast radius;
- information requiring platform support;
- starting and ending workspace state;
- confirmation that prohibited mutations and prohibited reads/accesses did not occur;
- disclosure of any accidental task-local write even if reverted.
```
