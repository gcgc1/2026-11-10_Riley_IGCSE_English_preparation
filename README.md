# Vocabulary building
Instruction overview:
reference/reading.html

# Cambridge IGCSE First Language English (0500) — grade A by March 2029

A self-study course for Cambridge IGCSE First Language English (0500), Papers 1 and 2, built one lesson per week. Target: **54/80 on each paper** (≈ grade A) in the **March 2029** series — 121 weeks from 2026-11-08, 97 lessons and 24 revision tests.

## Start here

| If you are… | Open |
|---|---|
| the learner | [`lessons/index.html`](lessons/index.html) — every week of the course, built and planned |
| a new session | [`AGENTS.md`](AGENTS.md), then [`BUILD.md`](BUILD.md), then [`PROGRESS.md`](PROGRESS.md) |
| asking why any of this exists | [`MISSION.md`](MISSION.md) |

## Where the course stands

**8 of 121 weeks built** — lessons 001–003 and 005–007, plus revision tests 1 and 2. **Week 009, *Word meaning in context*, is next**, followed by 010, 011 and test 3.

`PROGRESS.md` is the running record and is updated at the end of every build session. `REVISION-LOG.md` holds every test score and the errors that keep repeating; it is empty until the first test is sat.

## Two rules that override everything else

1. **Never teach from memory.** The syllabus changed for 2027 and most online material describes the old exam. `sources/` holds the syllabus, both specimen papers and both mark schemes, extracted to `.txt` so they can be searched. They are the only authority; `BUILD.md` §2 maps each question to its mark-scheme table.
2. **One skill per lesson, under ~15 minutes, ending in something the learner writes and the teacher marks.** Consistency over 121 weeks beats intensity.

## What is where

| Path | Contents |
|---|---|
| `AGENTS.md` | Entry point: read order and agent conventions |
| `BUILD.md` | The lesson contract, component API, CSS classes, quality gates |
| `MISSION.md` · `ROADMAP.md` | Why this exists · all 121 weeks and the filename formula |
| `PROGRESS.md` · `REVISION-LOG.md` | Build state and next up · every test score |
| `GLOSSARY.md` · `NOTES.md` | Canonical terms · learner preferences |
| `RESOURCES.md` | Curated sources: Cambridge primary documents, teaching material, communities |
| `lessons/` · `tests/` | The course itself, one file per week |
| `reference/` | `exam-map.html` (every question, mark, objective) · `reading.html` (block books, the Sunday sentence, the five-word vocabulary method) |
| `assets/` | `course.css` (visual system, print styles) · `quiz.js` (quiz, practice box, Copy answer button) |
| `sources/` | Cambridge documents: PDF and extracted `.txt`, plus the extraction scripts |
| `vocabulary/` · `learning-records/` | Learner-owned records |

## Conventions

- **Filenames:** `lessons/NNN-121-YYYY-MM-DD.html`, `tests/NNN-121-YYYY-MM-DD-test.html` — week number, course total, and the **Sunday** of that week. `NNN` is the only number: week 005 is week 005 whether it holds a lesson or a test.
- **Sunday(n) = 2026-11-08 + 7 × (n − 1)** days.
- **Every fourth week is a revision test** (weeks 004–096), cumulative and timed, escalating from 15 minutes / 5 marks to 50 minutes / 40 marks.
- **`lessons/index.html` is the course index.** When a week is built, link it there. It must never point at a page that does not exist.

## Copyright

`sources/` contains Cambridge documents downloaded from Cambridge International for personal study. They remain Cambridge's copyright: they are here to be read and marked against, not redistributed.
