# Execution-Surface Confidentiality

Apply confidentiality and minimization to every visible or retained surface:

- typed commands and arguments;
- terminal output and scrollback;
- browser URLs, headers, overlays, downloads, and DOM output;
- task/reasoning panels;
- screenshots and recordings;
- captured HTML and raw responses;
- logs and temporary files;
- final reports.

## Access is broader than output

If the prompt prohibits secret-bearing environment/configuration files, do not read or source them. “No secret value was printed” does not cure prohibited access.

A settings page or status view that lists masked secrets is still a secret-bearing configuration surface when access to that surface is prohibited. Do not open it merely because values appear concealed.

Use a purpose-built status surface that returns only presence, expected identity, or stability. If no safe surface exists, stop.

## Allowlisted output projection

Project output before it reaches the visible transcript. Return only the fields needed for the decision.

Suppress, unless explicitly required:

- raw task/object UIDs;
- actor/user IDs;
- callback paths and payloads;
- cookies, headers, tokens, and keys;
- complete authenticated/signed/connector URLs;
- unrelated project/task metadata.

Do not print a full object and sanitize only the final chat response.

Defining human-readable aliases does not by itself create an execution-surface redaction rule. If identifiers must remain hidden, say explicitly that aliases are required in commands, output, screenshots, task panels, artifacts, and the final report, then project raw platform output before display.

If a failure echoes an authenticated-looking URL, record the exposure incident without repeating the URL.

## Authenticated UI evidence

Prefer:

```text
visible state → narrow selector → bounded text/attribute extraction
```

Do not save and grep a whole authenticated page to locate one control. Broad captures may contain unrelated files, projects, account data, hidden identifiers, or stale task material.

If a broad capture is explicitly authorized and unavoidable:

1. declare its purpose;
2. constrain page and fields;
3. store outside the repository;
4. add it to the artifact ledger;
5. review sensitivity;
6. delete it only when deletion is authorized and safe.

Accidental overlays or stale tabs exposing unrelated content are incidents. Do not expand or explore them.

## Read-only diagnostic artifacts

Do not create external scratch findings, saved authenticated HTML, whole-page captures, or downloaded raw responses merely because they are outside the repository. Read-only diagnosis should default to a zero-artifact budget unless the prompt explicitly authorizes a narrowly defined artifact and lifecycle.

If an artifact is authorized, record its exact path, purpose, content projection, sensitivity, creation time, and retained/deleted disposition. A clean Git workspace does not prove that no external artifact was created.
