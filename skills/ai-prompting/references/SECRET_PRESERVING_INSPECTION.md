# Secret-Preserving Read-Only Inspection

Use this reference whenever a read-only task permits some configuration inspection while prohibiting credential/secret access.

## Key principle

`Read-only` means no mutation. It does **not** mean every readable secret-bearing source is authorized to inspect.

A task can permit:
- `VITE_APP_ID` presence/non-empty status;

while simultaneously prohibiting:
- `DATABASE_URL`;
- `JWT_SECRET`;
- OAuth secrets;
- callback tokens;
- session credentials.

Do not solve the first requirement by broadly reading a source that may contain the latter values.

## Avoid

Unless the prompt explicitly authorizes the whole source, do not:

```text
source ~/.user_env
source .env
cat .env
env
printenv
set
dump /proc/<pid>/environ
copy a secret-bearing config blob
```

merely to verify one permitted key.

Even if values are not printed in the final response, broad sourcing/enumeration may still constitute access to prohibited material.

Redaction/confidentiality boundaries apply to the **execution transcript too**: terminal output, browser devtools, screenshots, tool-generated “full output” files, temporary captures, and intermediate artifacts may all be user-visible or persist beyond the immediate command. Choose commands that avoid producing prohibited values in the first place.

The same minimization rule applies to non-secret but operationally sensitive material. Avoid raw task UIDs, actor IDs, callback paths/payloads, complete authenticated request URLs, connector URLs echoed by failed commands, and unrelated project/task files.

Prefer visible state, a narrow UI/DOM selector, or an allowlisted field projection. Do not save and grep a full authenticated page merely to locate one label or control.

## Command-policy preflight

When the prompt explicitly prohibits env-file access, treat that as a **hard command-construction rule**, not merely an output-redaction rule.

Before executing any shell command, reject it if it contains or invokes prohibited access such as:

```text
source ~/.user_env
source /opt/.../*.env
. .env
env
printenv
set
cat .env
/proc/<pid>/environ
```

This remains prohibited even when the command later pipes output through `grep`, `sed`, or redaction.

If the execution platform automatically prepends secret-bearing `source` commands and that behavior cannot be disabled, do not silently continue. Use another safe interface or stop and report the constraint.

“Secret values were not printed” does not cure prohibited source access.

## Prefer

Use the narrowest mechanism available:

- platform field metadata that returns only present/missing;
- a one-key management API/property;
- a non-printing boolean predicate for the permitted key through an already-authorized process/interface;
- an application-provided health/diagnostic field designed to expose only non-sensitive status.

If the only available method requires opening or sourcing a secret-bearing bundle, classify the result `UNKNOWN` and say what safe interface would be required.

## Final report

For restricted read-only tasks report separately:

```text
Mutations: none / describe accidental mutation
Protected reads: none / describe accidental protected-source access
Secret values exposed in output: none / describe incident
```

A final clean workspace does not erase a transient prohibited read, just as it does not erase a reverted transient write.

Use `EXECUTION_SURFACE_CONFIDENTIALITY.md` for artifact, overlay, URL, and broad-page-capture handling.
