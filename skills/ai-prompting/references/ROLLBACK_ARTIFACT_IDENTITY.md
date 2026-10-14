# Rollback Artifact Identity Reconciliation

Use this reference when a rollback/restore control was acknowledged but the displayed live version, serving content, or resulting artifact identity is disputed.

## 1. Separate the evidence planes

Track these independently:

| Plane | Question | Typical evidence |
|---|---|---|
| Control-plane selection | Which entry is marked Live/current? | Fresh Version History/status readback |
| Artifact lineage | Which immutable artifact or source produced that entry? | Platform-owned source/checkpoint/restored-from fields |
| Serving content | Which artifact is actually answering production requests? | Documented immutable deployment identity or authorized content discriminator |
| Application behavior | Does the tested route render or fail? | Route/network/runtime evidence |

A `Live` marker proves the active control-plane entry only. It does not by itself prove that entry's content lineage, rule out in-place replacement, or establish which source/checkpoint bytes are serving.

Route rendering proves availability or behavior, not artifact identity, unless the route exposes a pre-authorized artifact discriminator whose semantics are independently established.

## 2. Source fidelity for provenance

Classify every provenance field before relying on it:

- **platform-owned immutable field** — eligible to prove the relationship it explicitly names;
- **documented platform semantic** — eligible only within the documented scope;
- **operator-authored description/label** — assertion, not immutable provenance;
- **identifier resemblance** — a version ID resembling a Git SHA is not Git linkage;
- **retained historical observation** — useful context, but label its time and source;
- **inference** — never upgrade it to direct proof.

Do not call a description an “immutable record” unless the interface or official documentation establishes both immutability and field semantics.

## 3. Absence does not prove rollback effect

These observations do not independently prove that a rollback failed:

- no new version row appeared;
- the same entry still has the `Live` marker;
- no `restored-from` field is displayed;
- the fallback row remains historical;
- the public landing still renders.

They establish only what the inspected surface exposed. Unless platform semantics rule out an in-place content change, both hypotheses may remain possible:

```text
H1: the candidate artifact still serves
H2: fallback content was restored without a new exposed entry/lineage field
```

If authorized evidence cannot distinguish H1 from H2, classify:

```text
ROLLBACK UNVERIFIED — PRODUCTION IDENTITY UNKNOWN
```

Use `ROLLBACK FAILED — CANDIDATE CONTENT REMAINS LIVE` only when candidate serving identity is positively proven after the attempt. Use `ROLLBACK VERIFIED — FALLBACK CONTENT LIVE` only when fallback serving identity is positively proven.

## 4. Attempt ownership and mutation budget

Create a chronological rollback-attempt ledger before deciding whether another mutation is allowed:

| Attempt | Task/time | Actor | Target | Interface | Acknowledged | Post-readback | Counts against current authorization? |
|---|---|---|---|---|---|---|---|

Distinguish:

- a prior-task attempt described in retained evidence;
- an attempt visibly performed in the current task;
- authorization for one additional attempt;
- a lifetime/cumulative one-attempt ceiling.

Do not write “the single allowed rollback was attempted” without naming which task/attempt supplied that fact. Do not mark an action item complete as though the mutation ran when the completed work was only `DECISION: NOT PERFORMED`.

If the wording does not resolve whether a prior attempt already spent the mutation budget, keep the mutation latch closed and request owner clarification.

## 5. Conditional rollback latch

Before any newly authorized rollback, require fresh `PASS` rows for:

- current prompt/task-ledger reset;
- target row and exact version identity;
- current live/control-plane state;
- documented or proven rollback-control semantics;
- current and cumulative attempt budget;
- all repository, schedule, production, and safety invariants that the prompt makes prerequisites;
- exact confirmation control and bounded post-action readback plan.

Repository drift that is merely observed does not authorize repair. If the prompt requires an exact repository state before rollback and that state differs, close the latch and report a separate gate outcome even if read-only identity reconciliation can continue.

## 6. Provisional conclusion discipline

Before the authoritative surface is inspected, use only `PROVISIONAL` or `UNKNOWN` language. Never announce rollback success/failure or promise follow-on repair while identity is unresolved.

Maintain a conclusion ledger:

```text
time | provisional conclusion | evidence | later status | explicit retraction/correction
```

If later evidence contradicts an earlier statement, retract it visibly. The final report must not silently replace one confident conclusion with its opposite.

## 7. Minimal inspection footprint

Use the management/status surface before opening the application. Avoid authenticated business routes when they cannot answer artifact identity.

For containment checks, project only allowlisted fields such as alias, present/paused state, and running-count. Do not print full task objects, task UIDs, actor IDs, callback paths, payloads, or unrelated schedule metadata.

## 8. Two-axis final classification

Report both:

1. **Production identity:** one exact allowed artifact classification, including `UNKNOWN` when evidence cannot distinguish hypotheses.
2. **Authorization/gate outcome:** compliant read-only reconciliation, rollback performed and verified, rollback not performed, gate drift, or incident/deviation.

This prevents a plausible production conclusion from hiding stale task context, a spent mutation budget, repository drift, scope expansion, or execution-surface exposure.

## 9. Required final fields

Include:

- current-task and prior-attempt ledger;
- every relevant Version History entry and source-fidelity label;
- exact meaning and limit of the Live marker;
- platform rollback semantics: `PROVEN | NOT EXPOSED | UNKNOWN`;
- post-attempt control-plane identity;
- serving-content identity and discriminator, or `UNVERIFIED`;
- provisional conclusions retracted/corrected;
- repository/schedule prerequisite results;
- authorized action performed or `NOT PERFORMED`;
- execution-surface incidents;
- production-identity classification;
- separate authorization/gate classification.
