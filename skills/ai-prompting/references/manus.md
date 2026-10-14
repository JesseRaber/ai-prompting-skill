---
section: manus
source: manus-prompt-engineering SKILL.md (sha256 bd42b3025829e4720949d670e56617b0e46b20d9e94540749dcddaf377daccb7); body copied verbatim except the template-path edits listed in BUILD_REPORT.md
paths: All paths are relative to the skill folder. Former templates/X.md is now references/TEMPLATE_X.md and examples/X.md is now references/EXAMPLE_X.md; the Manus reference files keep their original names and bytes.
---

# Manus Prompt Engineering

## Purpose

Create Manus prompts that are operationally clear, minimally ambiguous, evidence-disciplined, and tightly bounded. Optimize for reliable execution rather than prompt length.

When reviewing a Manus run, compare three things:

1. the prompt's intended authorization and outcome;
2. Manus's visible execution behavior;
3. Manus's final claims about what it did and what the evidence proves.

Treat mismatches among those three as actionable prompt-design findings.

## Current-prompt restatement and context isolation

Before acting, Manus should reduce the **current prompt** to a one- or two-sentence mission and authorization summary using the prompt's own terminology. This is a context-isolation check, not extra prose.

If the restatement introduces a task class, phase, or action not present in the current prompt (for example, calling a preview-validation task a “merge-window” task), instruct Manus to re-read the current prompt before using tools. Do not let retained project memory, a prior task checklist, or unrelated recalled context redefine the current task.

Authorization from a previous task does not carry forward unless the current prompt explicitly incorporates it.

### Prompt transport integrity

Before using tools, verify that the authorization arrived intact. `NaN` list markers, empty numbered items, missing requirement bodies, truncation, broken identities, or unresolved safety-critical placeholders require `PROMPT TRANSPORT CORRUPTION — STOP`. Do not reconstruct missing authority from prior prompts, nearby prose, or assumed owner intent; ask for a clean rendering.

## Default architecture

For substantial engineering or release tasks, structure the prompt in this order:

1. **One-sentence mission** — state exactly what Manus is to accomplish.
2. **Starting gate** — pin repository/PR/runtime state and stop on drift.
3. **Authorization boundary** — define authorized actions and prohibited action classes once.
4. **Evidence rules** — state the evidence hierarchy and prohibited inferences.
5. **Coherent workstreams** — group related actions; avoid overlapping micro-sections.
6. **Stopping conditions** — define when each investigation branch ends.
7. **Controlled status vocabulary** — constrain ambiguous conclusions.
8. **Authorized edits / mutations** — enumerate exact resources that may change.
9. **Validation** — name exact checks, commands, and expected evidence.
10. **Expected final state** — state the end-state invariant.
11. **Required final report** — request independently auditable fields.

Prefer shorter, more structured prompts over repeated prohibitions. Repeat a prohibition locally only when it guards a high-risk adjacent action.

## Starting gates

Pin only state that materially affects the task, such as:

- repository / PR identity;
- exact head SHA;
- base/main SHA;
- branch and working-tree state;
- application candidate SHA;
- exact-head CI;
- runtime or deployment identity when relevant.

Always define failure behavior:

> Stop and report drift if any gate condition is not satisfied.

### Irreversible-action mutation latch

For merge, checkpoint, publish, deploy, restore, rollback, production-data, credential, deletion, or other hard-to-reverse actions, start with `MUTATION LATCH: CLOSED`.

Open it only after every prerequisite row is freshly and explicitly `PASS` with:

- successful command/interface status;
- non-empty shape-valid observation and exact identity/equality check;
- authorized, fresh, non-contradictory evidence.

Fatal/error text, authentication failure, timeout, empty output, ambiguous state, stale evidence, or `UNVERIFIED` keeps the latch closed. A task-list checkmark is not gate evidence.

Re-run volatile gates immediately before the irreversible action and after any user login/confirmation pause, material delay, workspace restart/synchronization, or external state change.

See `references/IRREVERSIBLE_RELEASE_GATE.md`.

For a purely read-only capability assessment, a lightweight gate may be enough. Do not require expensive release-state checks unless they affect correctness or the requested final invariant.

### Hard-gate closure before dependent actions

A gate is not satisfied because related evidence looks plausible. **Every conjunct in the gate must be proven before any action that depends on it.**

In particular, never infer a running development preview's revision solely from:

- the checkout's current Git SHA;
- a clean working tree;
- the process working directory;
- the fact that a watcher/dev server is running.

A long-lived process can be stale even while the checkout is current. When runtime identity is a prerequisite, require a runtime-specific attestation or candidate discriminator. If no safe discriminator exists, classify runtime identity `UNVERIFIED` and stop before gated browser navigation, authentication, or business-data requests.

Browser navigation is itself an action: opening a React route may automatically trigger authenticated API requests. Do not navigate to a gated route merely to discover whether the prerequisite was actually true.

If the only available runtime discriminator itself exercises a protected path, make that probe an explicit narrow exception in the gate and define its allowed side effects/output in advance.

See `references/HARD_GATES_AND_RUNTIME_ATTESTATION.md`.

For the full source/runtime/build/checkpoint/deployment evidence-axis model, use `references/RUNTIME_PROVENANCE_AND_PREVIEW_FIDELITY.md`. When validating an existing Version History checkpoint without restoring or publishing it, use `references/VERSION_HISTORY_CHECKPOINT_PREVIEW.md`.

## Authorization boundaries

Centralize global prohibitions near the top. Distinguish explicitly among:

- read-only inspection;
- repository edits;
- production reads;
- production writes;
- credential/session changes;
- schedule mutation;
- schema/migration changes;
- merge/checkpoint/publish/deploy/restore actions.

If a later section creates a narrow exception, identify it explicitly and specify the exact resource, fields/columns, action, output/redaction rules, and adjacent actions that remain prohibited.

### Authorization is a ceiling, not an obligation

Permission to perform an action does not mean Manus must perform it. Prefer the least-mutating path that fully satisfies the objective.

Examples:

- If one OAuth login is authorized but a safe pre-existing authenticated session fully satisfies the data-path objective, reuse may be preferable **unless the prompt explicitly requires a fresh-login path to be exercised**.
- If fresh authentication itself is the acceptance criterion, say `a fresh normal OAuth login is REQUIRED even if an existing session is present`.
- If pre-existing session reuse is preferred, say so explicitly and state whether that session must be preserved at the end.

Do not let an optional authorization become a checklist obligation, and do not silently substitute a different path when the prompt makes a specific path mandatory.

See `references/AUTHORIZATION_ACTION_LEDGER_AND_CLEANUP.md`.

### Read-only means workspace-read-only

For read-only tasks, explicitly prohibit creating, editing, deleting, renaming, formatting, or writing to **any repository file**, including:

- `todo.md`;
- notes;
- reports;
- scratch files;
- temporary artifacts;
- generated planning files;
- agent bookkeeping files.

Require the workspace state to be recorded at the start and end, normally with `git status --short` or equivalent. The ending state must match the starting state.

If Manus accidentally creates task-local changes, instruct it to revert **only those task-created changes**, report that this occurred, and verify that pre-existing user changes remain untouched.

See `references/READ_ONLY_WORKSPACE_INTEGRITY.md`.

## Shell-command and process-control hard gates

When a task prohibits secret-bearing environment access, enforce that at command-construction time. Do not allow shell prefixes that `source` env files merely because downstream output is redacted. If the platform automatically injects such sourcing and it cannot be disabled, stop or use a different safe interface.

For decision-bearing commands, record exit/interface status separately from output. Never accept `fatal`, `error`, `unauthorized`, timeout text, an empty substitution, or a malformed value as a branch, SHA, tree, configuration identity, or passing gate. Avoid compound commands where later success or formatting can mask an earlier failed producer.

For controlled process restarts, prove process identity beyond a PID: record start identity, PGID/SID, cwd, command, child/group membership, and actual listener ownership before signaling. Report the repository-defined application command separately from wrappers such as `nohup` or supervisors.

Fence startup and request logs with offsets/timestamps/request IDs. Do not use “latest matching line” as current-request proof when historical lines exist.

See `references/CONTROLLED_PROCESS_RESTART_AND_AUTH_VALIDATION.md` and `references/SECRET_PRESERVING_INSPECTION.md`.

For Git authentication repair or managed-workspace synchronization, separate CLI/API authentication, Git transport, working-tree state, Git administrative state, and external state. Define the helper's failure disposition before mutation and independently read back retained/restored configuration after success or failure. See `references/GIT_AUTHENTICATION_AND_WORKSPACE_SYNCHRONIZATION.md`.

## Authentication handoff and incidental read footprint

If the prompt requires user takeover for interactive confirmation, account selection, `Continue as`, consent, MFA/passkey, password, and security challenges all count as user-confirmation steps. Manus may navigate to the auth screen but must pause before identity confirmation unless explicitly authorized otherwise.

Authentication can redirect to a default route that auto-fetches unrelated data. Define that incidental read footprint before login or disclose unavoidable reads.

For expected login metadata DML, distinguish `AUTHORIZED`, `EXPECTED BY CODE`, `DIRECTLY OBSERVED`, and `UNVERIFIED`. Never close with a blanket “no DML/session change occurred” if an authorized exception may have occurred.

## Browser stabilization and harness errors

After authentication or navigation, wait for the requested UI/network cycle to stabilize before turning an intermediate loading/empty state into a final result. Reconcile provisional observations if the later stable state differs. For focused production symptom diagnosis, preserve the page's actual request/render path and use `references/PRODUCTION_DIAGNOSIS_AND_REPRODUCTION.md`.

Classify Manus/browser-tool failures separately from application/runtime failures. Failed click delivery, reconnects, focus problems, or automation transport errors do not establish a candidate application defect.

## Path evidence versus semantic evidence

Do not collapse request-path success, visual rendering, and hidden response semantics:

- HTTP/tRPC success can prove the protected request path;
- visual charts can prove visible labels/order/rendering;
- hidden fields such as `bucketId` or exact averages require direct authorized observation.

If the prompt asks for exact fields while forbidding raw response inspection, authorize a sanitized field extractor or mark those fields `UNVERIFIED`. A parent validation cannot be `PASS` if required semantic subchecks remain unobserved.

## Evidence discipline

Default evidence hierarchy for technical investigations:

1. exact trace-correlated runtime evidence;
2. direct authorized runtime/configuration inspection;
3. executed validation/test result;
4. repository/application implementation;
5. official platform documentation;
6. authenticated management-interface observations;
7. retained historical notes;
8. inference.

Do not promote a lower-confidence inference over contradictory higher-confidence evidence.

When important evidence is already known, express it as:

- **Evidence** — what was observed;
- **Establishes** — what it proves;
- **Does not establish** — what remains unknown;
- **Prohibited inference** — what Manus must not conclude.

### Negative evidence is source-specific

Do not collapse absence across evidence layers:

- absence in repository/runtime implementation may support **UNSUPPORTED AT APPLICATION LAYER**;
- absence from official docs supports **NOT DOCUMENTED**, not platform-wide unsupported;
- absence from accessible authenticated UI supports **NOT EXPOSED / UNVERIFIED**;
- never infer absence of undisclosed internal/operator tooling solely from docs/UI absence.

For platform-capability research, use official platform documentation first. Avoid unrelated vendors unless necessary only for general conceptual explanation.

See `references/EVIDENCE_AND_CAPABILITY_STATUS.md`.

## Layered capability conclusions

For application/platform questions, prefer independent layer statuses rather than one global label.

Recommended fields:

- **Application/runtime:** `SUPPORTED | UNSUPPORTED | UNKNOWN`
- **Official documentation:** `DOCUMENTED | NOT DOCUMENTED | UNKNOWN`
- **Accessible management interface:** `EXPOSED | NOT EXPOSED | UNKNOWN`
- **Internal/operator platform capability:** `KNOWN | UNKNOWN`
- **Overall operator capability:** `PROVEN AVAILABLE | NO PROVEN MECHANISM | UNVERIFIED`

A useful conclusion form is:

> Application-layer capability: UNSUPPORTED. Platform-level targeted capability: UNVERIFIED. No proven operator-accessible mechanism is currently available.

## Scope limiting

For narrow tasks, explicitly say what Manus should inspect and what it should not broaden into.

Example:

> Inspect only the target files, repository state needed for the gate, retained evidence needed for reconciliation, and validation outputs. Do not perform a general repository review.

If prior evidence is still authoritative, state that directly and prohibit rediscovery when additional access would add risk or cost:

> Existing evidence from the prior authorized review may be read and summarized. Do not perform another runtime or platform investigation.

For reconciliation-only tasks, add:

> Do not reopen solved substantive questions. Reconcile wording and evidence references only.

## Stopping conditions

Every investigation branch should have an end condition.

Examples:

- If the expected SHA does not match, stop before editing.
- After the smallest trace window and specified identifiers are exhausted, classify the cause `CONFIRMED` or `UNRESOLVED`; do not broaden into speculative refactoring.
- If environment isolation cannot be proven, do not authenticate; return the required authorization/manual test plan.
- If a capability cannot be proven from repository, official docs, or accessible UI, classify the relevant layers precisely and stop rather than speculate.

## Security-sensitive claims

Require exact source support for security-sensitive or quantitative claims used in a recommendation, including:

- token TTL;
- signing-key relationships;
- blast radius;
- reauthentication effects;
- callback-token impact;
- revocation behavior;
- credential/configuration propagation.

If the evidence supports only a possibility, use qualified language such as `may`, `at risk`, or `unverified` rather than `will`.

Never include an exposed credential in the prompt when avoidable. For an exposed token, prohibit retrieving, copying, quoting, decoding, testing, reusing, storing, logging, committing, or supplying it to an interface unless separately authorized.

Confidentiality/redaction rules apply to **visible tool output, terminal output, screenshots, temporary captures, saved full-output files, and intermediate artifacts**, not only the final response. Avoid commands that may spill prohibited values into the execution transcript even if the final answer would omit them.

Do not save/grep a whole authenticated page when a visible control, narrow selector, or allowlisted field projection answers the question. Treat accidental overlays, raw task identifiers, authenticated-looking URLs, whole-page captures, and unrelated project/task files revealed in the transcript as incidents.

See `references/EXECUTION_SURFACE_CONFIDENTIALITY.md`.

## Validation and formatting

Validation must be proportional to the task and explicit.

For each validation command, ask Manus to record:

- exact command;
- pass/fail or exit result;
- whether the command mutated files;
- whether it was rerun after correction.

For documentation-only tasks, define formatter behavior in advance:

> Running the formatter is authorized. Retain formatter changes only in explicitly authorized files. Revert any formatter-induced change to unauthorized files.

Do not treat passing application tests as proof of runtime, migration, or deployment behavior unless those paths were actually exercised.

## Candidate evidence versus documentation-head evidence

When documentation-only commits exist after an application candidate, require separate identities for:

- application candidate SHA;
- application-candidate CI;
- documentation head SHA;
- documentation-head CI.

Do not describe documentation-head CI as application runtime or deployment validation.

## Action ledger and cleanup consistency

For tasks with narrow mutations or cleanup actions, make Manus track three categories:

- **authorized and performed**;
- **authorized but not performed**;
- **prohibited and not performed**.

This prevents blanket final statements from contradicting the execution. For example, normal application logout changes browser-local session/cookie state even if it does not revoke a server-side token. A final report must say that the authorized logout occurred rather than claiming “no session state changed.”

Record the starting authentication/session state when it matters. Define the cleanup policy explicitly:

- a session created by the task should normally be logged out if safe and requested;
- a pre-existing session should normally be preserved unless the prompt explicitly authorizes terminating it;
- if the prompt requires logout regardless, acknowledge that the ending browser-session state will differ from the starting state.

After a hard stop condition fires, perform only mandatory cleanup and final-state proof. Do not continue optional validation workstreams. Bound repeated UI-cleanup attempts; if the normal cleanup control cannot be reached safely after a small number of attempts, report the cleanup as blocked rather than exploring unrelated routes or controls.

See `references/AUTHORIZATION_ACTION_LEDGER_AND_CLEANUP.md`.

## Expected final state

Always state the desired invariant when the task has operational consequences.

Examples:

- one documentation-only commit, application candidate unchanged, PR open, release blocked;
- zero workspace changes, zero production mutations, capability conclusion only;
- PR branch updated, exact-head CI green, no merge performed.

## Final report

Request facts that can be checked independently. Typical fields:

1. starting and ending SHA/state;
2. files/resources inspected;
3. files/resources changed;
4. evidence obtained or reconciled;
5. layered capability/status conclusions;
6. validation commands and results;
7. exact-head CI evidence when relevant;
8. unresolved items and required separate authorization;
9. explicit confirmation that prohibited actions did not occur;
10. workspace-integrity confirmation for read-only tasks.

Require an explicit status for **every requested report field**, including `NOT APPLICABLE`, `NOT PERFORMED`, or `UNVERIFIED`; do not allow omission by implication.

Do not ask Manus to say “nothing changed” unless the prompt also requires evidence capable of supporting that claim. Make the no-change assertion logically consistent with any authorized logout, login metadata update, temporary read-only browser state, or other permitted action.

Before returning, mechanically reconcile positive claims against the evidence matrix, negative claims against the action/artifact ledger, attempt counts against the trace, and final-state claims against fresh postcondition readback. Report material transitions such as `dirty → clean` or `claimed synchronized → SHA mismatch`; do not report only the ending state.

Task-ledger entries must preserve the prompt's required count and meaning. A failed, blocked, skipped, or not-run action is not `completed` merely because the task reached a terminal classification.

See `references/FINAL_RECONCILIATION.md`.

## Reviewing screen recordings

When the user provides a Manus screen recording, use `references/SCREEN_RECORDING_REVIEW.md` and structure the deliverable with `references/TEMPLATE_SCREEN_RECORDING_REVIEW_REPORT.md`.

Specifically look for:

- whether Manus converted the prompt into a sensible checklist;
- ordering differences between requested and actual work;
- broad inspection that was unnecessary;
- writes to `todo.md`, notes, scratch files, or generated artifacts during read-only work;
- formatter-induced changes;
- repeated searches caused by ambiguous wording;
- use of non-authoritative sources before official sources;
- actions omitted from the final response;
- final claims stronger than the visible evidence;
- useful Manus behaviors that should be reinforced in future prompts.

## Templates

Use the closest template and adapt it instead of rebuilding prompts from scratch:

- `references/TEMPLATE_ENGINEERING_TASK_PROMPT.md`
- `references/TEMPLATE_READ_ONLY_CAPABILITY_ASSESSMENT.md`
- `references/TEMPLATE_READ_ONLY_PREVIEW_VALIDATION.md`
- `references/TEMPLATE_CONTROLLED_LOCAL_PREVIEW_RESTART.md`
- `references/TEMPLATE_DOCUMENTATION_RECONCILIATION.md`
- `references/TEMPLATE_RELEASE_AUTHORIZATION_PACKET.md`
- `references/TEMPLATE_CONTROLLED_RELEASE_EXECUTION.md`
- `references/TEMPLATE_SCREEN_RECORDING_REVIEW_REPORT.md`

## Controlled platform mutations

For narrow production/control-plane mutations, use:

**pre-state attestation → mutation acknowledgement → independent post-state readback**.

For multiple objects, do not move to the next mutation until the previous object's required immediate verification passes. Preserve authorized partial success unless compensation is separately authorized.

If the prompt requires aliases instead of raw operational IDs, enforce that across terminal commands, CLI output, screenshots, tool logs, temporary artifacts, and final text. Prefer hidden variables and allowlisted output projections.

Claims such as `no invocation occurred` and `no other task changed` require before/after audit-window watermarks and population invariants. Otherwise weaken them to the exact observation actually established.

Keep direct state (`enabled=false`) separate from scheduling semantics (`will not trigger`) unless the latter is documented/proven.

See `references/CONTROLLED_PLATFORM_MUTATION.md`. For rollback/restore identity reconciliation, do not equate a Live marker, operator-authored description, or SHA-like ID with serving-content lineage; attribute attempts across tasks and use `references/ROLLBACK_ARTIFACT_IDENTITY.md`.

## Operational capability closure

For `METHOD PROVEN / METHOD NOT PROVEN` investigations, require a named-surface coverage matrix across the authorized repository, official docs, current CLI/client, and authenticated UI surfaces.

CLI `--help` proves current client syntax only. It does not prove backend credential lifecycle, UID retention, activation timing, atomicity, reversibility, or other server semantics.

Before finalizing a transition design, reconcile the capability table, mutation ledger, sequencing, and recovery plan. A later step must not assume an operation an earlier section found unavailable or unproven.

Model cross-system orphan windows explicitly, including when a newly created task becomes triggerable and what happens before DB linkage persists.

Use exact uncertainty language and prove recovery verbs separately.

See `references/OPERATIONAL_CAPABILITY_INVESTIGATION.md`.

## Release authorization packets

For non-executing release planning, distinguish **planning compliance** from **release authorization readiness**.

Classify the packet itself:

- `EXECUTABLE`
- `CONDITIONALLY EXECUTABLE`
- `NOT YET AUTHORIZABLE`

If any safety-critical mechanism or platform control remains unproven, the packet is not action-ready. A copy-paste block with `[PLATFORM_REAUTHORIZATION_METHOD]`, unknown source/task mappings, or other mechanism placeholders is a **conditional template**, not executable authorization.

Use an evidence manifest for release-critical claims and type each source: current repo/GitHub, current platform UI/config, official docs, retained evidence, generic/internal skill guidance, inference/proposal, or owner-accepted risk. Internal skills guide inspection but do not prove project/platform facts.

Keep current project configuration separate from generic platform capability. Keep callback configuration mutations separate from callback execution/business-data effects.

Quantitative retry/timeout/platform claims need exact primary-source support. Proposed monitoring thresholds must be labeled as proposed policy with rationale rather than silently presented as platform facts.

A task limited to non-secret platform information must not source secret-bearing env files.

See `references/RELEASE_AUTHORIZATION_PACKET.md` and `references/TEMPLATE_RELEASE_AUTHORIZATION_PACKET.md`.

### Executing an authorized release

Do not treat a long detailed release prompt as self-enforcing. Use the irreversible-action mutation latch before merge and before every later release mutation.

If an irreversible step occurs while its latch should be closed, classify the bypass, freeze later mutations, preserve/inventory the new external state, disclose the failed gate/action, and require a new residual-action authorization. After merge, never replay the merge or resume the old packet midstream; authorize only remaining work from current state.

Use `references/TEMPLATE_CONTROLLED_RELEASE_EXECUTION.md`.

## Quality gate before returning a Manus prompt

Confirm:

- the mission is narrow and imperative;
- exact state is pinned where necessary;
- the rendered prompt contains no `NaN`, empty requirement bodies, truncation, or unresolved authority;
- stop-on-drift behavior exists;
- every irreversible action has an initially closed mutation latch;
- command/interface status is validated separately from returned text;
- volatile gates are refreshed after user handoff, delay, restart, or external mutation;
- global authorization is centralized;
- read-only workspace integrity is explicit when applicable;
- exceptions are narrow and enumerated;
- evidence and inference are separated;
- negative evidence uses source-appropriate semantics;
- each branch has a stopping condition;
- security-sensitive claims require sources;
- unnecessary repository/platform exploration is prohibited;
- formatter behavior is defined when relevant;
- validation is proportional and explicit;
- expected final state is stated;
- final report is independently auditable;
- current-prompt restatement does not import prior-task scope;
- every hard-gate conjunct is proven before gated browser/API actions;
- optional authorization versus required execution is explicit;
- starting/ending authentication-session policy is explicit when sessions are involved;
- final no-change statements account for authorized cleanup or narrow mutations;
- dirty-to-clean, attempted-to-proven, and other material state transitions are reconciled;
- irreversible partial progress requires a new residual-action authorization;
- every required report field has an explicit status;
- repeated prohibitions add real safety value.

## Project profiles

For Cabinet Price Analyzer release-related prompts, use `references/CABINET_PRICE_ANALYZER_PROFILE.md`.
