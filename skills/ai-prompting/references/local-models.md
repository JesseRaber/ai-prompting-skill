# Local models

Models run on Jesse's own workstation through Ollama, LM Studio, Open WebUI or similar.

Evidence base: the Local AI Model Research project (2026-08) and the multi-agent-folder-cleanup install guide.

## Writing the prompt
- Small local models follow short, explicit prompts best: one task, numbered steps, an output format, and a length cap.
- Put the skill's `SKILL.md` in the system prompt or context loader and load a reference file only when the task needs it; context windows are small.
- Do not rely on web access or tools unless the front-end provides them.
- **Model names go stale fast (P-015).** Observed 2026-08-22: a research report titled a section "The model recommendations are stale" and then recommended a model two generations old. Never hard-code a shortlist; ask for a dated check of the model library and license.
- Ask the model to declare its research date and unknowns first. Grok did this unprompted (2026-08-22) and its report was the easiest to verify.

## Installing skills on it
- No native skill loader in most front-ends: point the system prompt at `SKILL.md` and paste the instruction block from INSTALL.md.

## Open questions
- Which models are installed and tested; context sizes; tool support in the chosen front-end.
