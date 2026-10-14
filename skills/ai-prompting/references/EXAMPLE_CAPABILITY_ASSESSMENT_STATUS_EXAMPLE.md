# Capability Assessment Status Example

Use layered conclusions instead of one vague overall answer.

```text
Application/runtime: UNSUPPORTED
Evidence: sessions are self-contained signed tokens; verification has no denylist, session record, token-version check, or per-token revocation state.

Official documentation: NOT DOCUMENTED
Evidence: official platform authentication/access-control documentation does not describe per-application-session revocation.

Accessible management interface: NOT EXPOSED
Evidence: the authenticated interface inspected does not expose a session inventory or revoke-session control.

Internal/operator platform capability: UNKNOWN
Evidence: no authoritative source establishes whether undisclosed operator tooling exists.

Overall operator capability: NO PROVEN MECHANISM
Meaning: no targeted revocation mechanism is currently proven available to the operator; this does not establish that the platform has no internal capability.
```
