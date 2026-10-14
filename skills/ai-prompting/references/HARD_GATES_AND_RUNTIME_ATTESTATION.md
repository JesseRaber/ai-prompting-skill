# Hard Gates and Runtime Attestation

Use this reference when a downstream browser/API/runtime test is valid only if an exact candidate, environment, artifact, or authentication prerequisite is already established.

## Gate closure rule

A gate containing `A + B + C` is not PASS until A, B, and C each have direct evidence. Do not check off the parent gate based on inference from adjacent facts.

Downstream actions must wait. If a gated action can itself trigger API requests, database reads, authentication, or other side effects, it is not an acceptable way to discover retroactively whether the gate was true unless the prompt explicitly authorizes that probe as part of the gate.

## Irreversible-action latch

Before an irreversible action, use a table with these independent fields:

| Gate | Expected | Observed | Source | Command/interface status | Freshness | Result |
|---|---|---|---|---|---|---|

The latch remains closed unless every row is a fresh `PASS`.

Do not let a formatter, pipeline, command substitution, or later command turn a failed producer into apparently usable data. Treat error text, empty output, malformed identifiers, authentication failure, timeouts, and ambiguous state as `FAIL`, never as observation values.

After a user handoff, long wait, restart, synchronization attempt, or external mutation, volatile gate rows expire and must be re-read immediately before the action.

See `IRREVERSIBLE_RELEASE_GATE.md` for release-specific failure and recovery rules.

## Required-clean starting state

If cleanliness is a prerequisite, any working-tree entry is an immediate stop. Preserve and report the paths/statuses; do not reset, stash, restart, synchronize, or otherwise make them disappear without separate preservation/recovery authority.

If a later state is clean, report an unexplained `dirty → clean` transition until its mechanism is proven. Never say the workspace “remained clean.”

## Source checkout is not running-server identity

For a workspace development server, these facts are useful but insufficient alone:

```text
git HEAD = candidate
working tree clean
server process cwd = repository
watch/dev process exists
```

A long-lived process can have stale server modules, stale environment, stale child processes, or route/backend indirection.

## Candidate/runtime attestation options

Prefer, in order, when available and authorized:

1. immutable build/version/checkpoint ID tied to the candidate SHA;
2. non-secret runtime `/version` or build-info endpoint carrying the source/build revision;
3. process launch/reload evidence explicitly correlated to the candidate revision plus a candidate-specific server fingerprint;
4. a narrow candidate-discriminating behavior whose request/side effects are explicitly authorized as a provenance probe.

Client-source evidence can attest the client half but not automatically the server half. A Vite source module or source map matching the candidate does not prove the server procedure implementation is current.

If none of these can prove the relevant runtime axis, return `UNVERIFIED`.

## Candidate discriminators

When a candidate changes a specific response contract, SQL shape, stable identifier, version string, or other non-secret behavior, the prompt may define that as a discriminator. State exactly what old and new behavior would mean.

Example:

```text
Candidate discriminator: the server response uses stable bucket IDs from shared/priceRanges.ts.
Legacy display-label grouping is evidence that the server path is not the candidate implementation.
```

If observing that discriminator requires authenticated business-data access, authorize the minimal aggregate-only probe explicitly and do not broaden it into full validation until the discriminator passes.

## Browser navigation is active

Opening a React route can automatically fire queries. Therefore:

> Do not navigate to `/analytics` until the exact-runtime prerequisite is proven, unless `/analytics` itself is the explicitly authorized provenance probe.

This ordering prevents an invalid runtime from generating unnecessary reads or misleading validation evidence.
