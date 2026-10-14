# Manus Non-Executing Release Authorization Packet Template

```text
Prepare a planning-only release authorization packet for [PROJECT]. Do not execute release actions.

## Current-task context isolation

Use only:
- current prompt;
- named repository/project;
- explicitly accepted retained evidence;
- current authorized read-only repository/platform evidence.

Ignore unrelated recalled memories and unrelated project knowledge.

## Non-secret-only inspection boundary

Do not source/dump secret-bearing environment files or process environments.
Do not inspect secret values.
Use current non-secret UI/config evidence or mark UNKNOWN.

## Workspace integrity

Record starting and ending `git status --short`.
Ending state must match starting state.

## Evidence manifest

For every release-critical claim record:
- claim;
- exact source/file/page/UI;
- evidence type;
- freshness;
- direct vs retained;
- confidence;
- what the source does not prove.

Do not use generic/internal skill guidance as authoritative project/platform evidence.

## Critical facts

Verify/derive only the facts explicitly requested.

Separate:
VERIFIED FACT
RETAINED EVIDENCE
PROPOSED POLICY
CONDITIONAL PROCEDURE
UNRESOLVED BLOCKER
OWNER-ACCEPTED RISK

## Callback transition

Separate:
A. credential/task configuration changes
B. source/task linkage DB changes
C. task enable/pause/retire operations
D. callback execution side effects

For every proposed transition verb, prove the platform control and side effects.

If the exact fresh-credential method or required platform controls are unknown:
- classify packet `NOT YET AUTHORIZABLE`;
- do not describe the transition sequence as executable;
- provide only a conditional design.

## Platform settings and quantitative behavior

Distinguish current project setting from generic platform capability.

For retries/timeouts/auto-publish/restore semantics:
- cite exact primary source/current UI;
- otherwise mark UNVERIFIED.

## Monitoring thresholds

For each number, label:
SOURCE_DERIVED_LIMIT
BASELINE_DERIVED_THRESHOLD
PROPOSED_CONSERVATIVE_POLICY

Provide rationale.

## Packet executability classification

Choose exactly one:
EXECUTABLE
CONDITIONALLY EXECUTABLE
NOT YET AUTHORIZABLE

Explain why.

## Runbook

For each step report:
- phase;
- operator;
- authorization;
- fact/proposal status;
- prerequisite evidence;
- expected side effect;
- evidence capture;
- pass;
- stop;
- reversible?;
- recovery.

Unknown platform controls are prerequisites, not steps.

## Safety-critical placeholder manifest

For every `[PLACEHOLDER]` record:
- source;
- gate;
- validation;
- whether release may proceed if empty.

## Authorization template

If status is NOT YET AUTHORIZABLE, put directly above the block:

DO NOT EXECUTE THIS TEMPLATE YET.
Resolve the listed safety-critical blockers first.

Do not call a block with unresolved mechanism placeholders action-ready.

## Final reconciliation

Return:
- planning-task compliance;
- release authorization readiness;
- evidence manifest;
- unresolved facts;
- workspace start/end proof;
- prohibited-action confirmation.

```
