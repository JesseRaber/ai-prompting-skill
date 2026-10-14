# ai-agent-prompting 1.0.1 candidate

This candidate keeps the v1.0.0 combined skill and packaging, and improves prompts written for ChatGPT/Codex.

## Added

- A shared executable-handoff contract: task mode, current and desired state, exact scope, authority versus evidence, deliverable, acceptance checks, decision boundary, mutation authority and continuity.
- A preferred ChatGPT/Codex handoff block that agents can fill without repeating irrelevant fields.
- Clear wording that lets Codex continue through routine in-scope implementation while returning only consequential decisions to the owner.
- A short list of prompt patterns that slow Codex down or create ambiguity.

## Status

Candidate only. Not installed, pushed, tagged or released. Existing v1.0.0 host-upload and runtime gates still apply, and the changed ChatGPT/Codex guidance needs a representative prompt-generation test before release.
