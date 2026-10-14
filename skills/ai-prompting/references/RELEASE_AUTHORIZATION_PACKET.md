# Release Authorization Packet Design

Use this reference when Manus is asked to inspect evidence and produce a release, deployment, callback-transition, monitoring, or rollback authorization packet without executing it.

## 1. Packet executability state

Before writing any authorization block, classify the packet:

- `EXECUTABLE` — all safety-critical prerequisites and mechanisms are proven from fresh enough evidence.
- `CONDITIONALLY EXECUTABLE` — only clearly named release-window values remain to be filled from prescribed gates; no mechanism/safety assumption is unresolved.
- `NOT YET AUTHORIZABLE` — any safety-critical mechanism, platform control, side effect, topology, or required identity remains unknown.

Examples of safety-critical unresolved facts:

- exact callback credential issuance/reauthorization method;
- whether task UID is retained or replaced;
- availability/semantics of pause/enable/retire controls;
- current project auto-publish setting;
- current fallback availability;
- current deployment topology;
- current production identity;
- source/task mapping.

A packet with unresolved mechanism placeholders is **not** action-ready.

## 2. Non-execution barrier

When status is not `EXECUTABLE`, put this directly above any copy-paste template:

```text
DO NOT EXECUTE THIS TEMPLATE YET.
Current status: NOT YET AUTHORIZABLE.

Resolve and freshly verify:
- [BLOCKER 1]
- [BLOCKER 2]

Replace every safety-critical placeholder only from the named evidence source/gate below.
```

Do not rely on a warning several sections earlier.

## 3. Evidence-source typing

Every release-critical claim should be typed:

- `CURRENT_REPOSITORY_STATE`
- `CURRENT_PLATFORM_UI_CONFIG`
- `OFFICIAL_PLATFORM_DOCUMENTATION`
- `RETAINED_PROJECT_EVIDENCE`
- `GENERIC_INTERNAL_SKILL_GUIDANCE`
- `INFERENCE`
- `PROPOSED_POLICY`
- `OWNER_ACCEPTED_RISK`

Generic/internal Manus skills can guide what to inspect. They do not prove current project/platform facts.

Unrelated recalled user/project knowledge is excluded.

## 4. Evidence manifest

Create a compact evidence manifest for critical claims.

Recommended fields:

| Claim | Source | Type | Freshness | Direct/retained | Confidence | Does not prove |
|---|---|---|---|---|---|---|

Always include entries for:

- PR/head/base/CI;
- docs-only delta;
- current project identity;
- `VITE_APP_ID` presence/stability;
- production DB identity;
- auto-publish behavior;
- rollback/restoration control;
- callback signing inputs;
- old/new callback compatibility;
- callback transition side effects;
- callback execution side effects;
- retry/timeout platform behavior;
- retained fallback health;
- retained schema state.

If the exact source cannot be cited, downgrade the claim.

## 5. Retained evidence freshness

Historical/retained records remain historical.

Good:

> RETAINED EVIDENCE: production schema audit at 2026-08-15 showed the Phase 3A additive columns/indexes present.

Bad:

> Current production schema is confirmed.

unless a fresh current check was actually authorized and performed.

The release runbook may require a fresh gate at execution time; the planning task must not silently refresh old evidence by wording.

## 6. Non-secret inspection boundary

If the task limits inspection to non-secret platform information:

- do not `source` secret-bearing env files;
- do not dump process environments;
- do not load credentials merely to test presence;
- do not read secret configuration values.

Use narrow current UI/config presence checks when authorized. If the shell/runtime automatically sources secret-bearing files and this cannot be disabled, use another interface or report a scope constraint/incident.

## 7. Project capability versus project setting

Keep separate:

```text
PLATFORM CAPABILITY: checkpoint save may support automatic publication.
CURRENT PROJECT SETTING: auto-publish is enabled for Cabinet Price Analyzer.
```

The latter needs current project UI/config evidence or explicitly dated retained evidence.

Never infer a current setting from generic platform documentation alone.

## 8. Platform quantitative claims

Retry counts, timeouts, execution limits, API semantics, and similar operational values require exact primary-source support.

For each value record:

- exact official page/section;
- date/freshness;
- whether the behavior is a platform limit, default, or configurable;
- scope.

A generic docs homepage is insufficient.

Internal skill text is not a substitute for an authoritative platform source when the number affects production safety.

If support is unavailable:

```text
Platform retry limit: UNVERIFIED
Do not bake a numeric assumption into the release authorization.
```

## 9. Callback transition mutation model

Keep callback transition operations separate.

### Configuration transition
May include:

- issue/regenerate/reauthorize callback credential;
- create/update task;
- persist task UID;
- pause/enable task;
- retire/delete old task.

### Callback execution
May include:

- network fetch;
- AI/external calls;
- source scan metadata changes;
- pending approval creation;
- audit/business-data writes.

Do not claim that credential regeneration itself causes scan/source writes unless code/platform evidence proves that.

## 10. Transition-precondition proof

For every proposed callback-transition verb:

```text
PAUSE
CREATE
REAUTHORIZE
UPDATE UID
ENABLE
RETIRE
RUN
```

map it to:

| Verb | Proven control/API? | Source | Side effect | Reversible? |
|---|---|---|---|---|

If a control is not proven, the sequence is a **CONDITIONAL DESIGN**, not an executable runbook.

Use wording:

> If the platform is confirmed to support create/pause/enable/retire with the documented semantics, the proposed near-atomic sequence is...

Do not say a near-atomic overlap is implemented or available when those primitives remain unknown.

## 11. Fact/proposal/authorization labels

Tag operational content:

- `VERIFIED FACT`
- `RETAINED EVIDENCE`
- `PROPOSED POLICY`
- `CONDITIONAL PROCEDURE`
- `UNRESOLVED BLOCKER`
- `OWNER-ACCEPTED RISK`

A proposal does not become a fact by being placed into a table.

An inferred procedure does not become authorized by appearing in a copy-paste block.

## 12. Monitoring threshold provenance

For every numerical threshold, label its provenance:

- `SOURCE_DERIVED_LIMIT`
- `BASELINE_DERIVED_THRESHOLD`
- `PROPOSED_CONSERVATIVE_POLICY`

Include a short rationale.

Example:

```text
analytics.priceRangeDistribution:
- Proposed pass target: <=3 s
- Provenance: PROPOSED_CONSERVATIVE_POLICY
- Rationale: materially above the prior ~483 ms local observation while still catching severe regression
```

If the user has not explicitly accepted proposed thresholds yet, the release authorization template should say that copying/submitting the template constitutes acceptance, or use placeholders requiring confirmation.

## 13. Safety-critical placeholders

Every placeholder needs:

- name;
- evidence source;
- gate when it will be filled;
- validation rule;
- whether release can proceed while empty.

Example:

```text
[FINAL_MAIN_SHA]
Source: post-merge GitHub/main readback
Gate: B2
Validation: must equal synchronized workspace source
Release allowed while empty: NO
```

Safety-critical mechanism placeholders such as `[PLATFORM_REAUTHORIZATION_METHOD]` make the packet `NOT YET AUTHORIZABLE`.

## 14. Planning safety versus release safety

Use separate conclusions:

```text
Planning task compliance: PASS
Release authorization readiness: NOT YET AUTHORIZABLE
```

A clean repository/CI review can pass while production release remains blocked.

## 15. Workspace proof

Read-only release planning should record:

- starting `git status --short` / `--porcelain`;
- ending state;
- comparison.

Do not claim `no repository modification` without final proof when the task explicitly requires strict read-only integrity.

## 16. Final status before template

Immediately before the authorization template state:

```text
SAFE AUTHORIZATION STATUS: NOT YET AUTHORIZABLE

Blocking facts:
1. ...
2. ...

The block below is a conditional draft only.
```

This prevents a long detailed packet from creating false action-readiness.



## 17. Capability-ledger consistency

If a release blocker investigation produces a capability table, any later conditional runbook must obey it.

Do not:
- use `enable replacement` if creation was shown to produce an active task;
- rely on `pause replacement` as recovery unless pause semantics for that task type are proven;
- call a sequence near-atomic while activation timing or compensating deletion remains unknown.

Every transition and recovery verb must map to proven operational capability or be labeled `CONDITIONAL / UNPROVEN`.

For callback-mechanism investigations, use `references/OPERATIONAL_CAPABILITY_INVESTIGATION.md`.

## 18. Executing an approved packet

An approved packet still requires fail-closed execution gates. Before merge and every later irreversible action:

- validate command/interface status separately from output;
- reject fatal/error/empty/malformed values;
- refresh volatile gates after any user handoff or delay;
- stop on any dirty workspace when cleanliness is required;
- never let checklist completion substitute for gate evidence.

If merge occurs while a pre-merge gate failed, classify the gate bypass and freeze later release mutations. Do not describe the run only by the later synchronization stop.

After any irreversible partial progress, produce a new residual-action packet based on current state rather than resuming the original authorization midstream.

Use `IRREVERSIBLE_RELEASE_GATE.md` and `templates/CONTROLLED_RELEASE_EXECUTION.md`.
