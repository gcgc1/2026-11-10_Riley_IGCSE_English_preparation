`.AI_ignore_material/` is off-limits: never read, search, list, or edit it.

## Teaching workspace

This is a **teaching workspace** for Cambridge IGCSE First Language English (0500), aiming at grade A in March 2029. Lessons are built one per week and live in `lessons/`.

**On any session that touches lessons, read these first, in order:**

1. `BUILD.md` — how to build a lesson here (contract, components, quality gates)
2. `MISSION.md` — why the learner is doing this
3. `ROADMAP.md` — all 121 weeks and the file naming formula
4. `PROGRESS.md` — what is built and what is next
5. `GLOSSARY.md` — canonical terms
6. `NOTES.md` — learner preferences
7. `REVISION-LOG.md` — every test score, and the errors that keep repeating
8. `reference/reading.html` — the block book and the vocabulary rule every lesson's weekly table carries

`lessons/index.html` is the course index: every week, built and planned. Keep it current when a week is built — it must never link a page that does not exist.

Never teach from parametric memory: the syllabus changed for 2027 and most online guides describe the old exam. Use `sources/`.

Update `PROGRESS.md` at the end of every build session.

## Agent skills

### Issue tracker

Local markdown under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Default five-role vocabulary (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context (`GLOSSARY.md` + `docs/adr/` at the root). See `docs/agents/domain.md`.
