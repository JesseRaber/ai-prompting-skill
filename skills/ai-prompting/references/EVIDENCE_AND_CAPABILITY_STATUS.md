# Evidence and Capability Status

## Evidence hierarchy

Use the highest-quality available evidence and keep layers separate:

1. exact trace-correlated runtime evidence;
2. direct authorized runtime/configuration inspection;
3. executed test/validation evidence;
4. repository/application implementation;
5. official platform documentation;
6. authenticated management-interface observation;
7. retained historical evidence;
8. inference.

## Negative evidence semantics

Different absence means different things.

### Repository/runtime absence

If the relevant application code and persistence model contain no mechanism for a capability, this can support:

> UNSUPPORTED AT APPLICATION LAYER

provided no external layer is known to intercept or override the behavior.

### Official documentation absence

If official docs do not describe the capability, say:

> NOT DOCUMENTED

Do not say platform-wide `UNSUPPORTED` unless authoritative platform evidence proves that.

### Accessible UI absence

If an authenticated management interface does not expose the capability, say:

> NOT EXPOSED IN THE ACCESSIBLE INTERFACE / UNVERIFIED

Do not infer that internal/operator tooling does not exist.

## Layered status model

Recommended output:

```text
Application/runtime: SUPPORTED | UNSUPPORTED | UNKNOWN
Official documentation: DOCUMENTED | NOT DOCUMENTED | UNKNOWN
Accessible management interface: EXPOSED | NOT EXPOSED | UNKNOWN
Internal/operator platform capability: KNOWN | UNKNOWN
Overall operator capability: PROVEN AVAILABLE | NO PROVEN MECHANISM | UNVERIFIED
```

## Evidence statement pattern

For important facts, use:

```text
Evidence:
Establishes:
Does not establish:
Prohibited inference:
```

This is particularly useful for production incidents and security assessments.

For a complete worked classification, use `examples/CAPABILITY_ASSESSMENT_STATUS_EXAMPLE.md`.

## Operational control surface semantics

For operational mechanisms, keep source layers distinct:

- official docs absence → `NOT DOCUMENTED`;
- CLI/help absence → `NOT EXPOSED BY CURRENT CLI`;
- inspected authenticated UI absence → `NOT EXPOSED IN INSPECTED UI`;
- repository absence → `NOT IMPLEMENTED/NOT FOUND IN APPLICATION LAYER`;
- overall platform mechanism → `UNVERIFIED` unless the relevant authorized surfaces have been exhausted.

`CLI --help` is evidence of current client syntax, not a platform semantic contract.

Use `references/OPERATIONAL_CAPABILITY_INVESTIGATION.md` for full closure and consistency rules.
