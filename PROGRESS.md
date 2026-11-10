# Progress

State of the course. Update this at the end of every build session — it is the first thing a new session reads after `MISSION.md` and `ROADMAP.md`.

**Last updated:** 2026-11-10

## Current position

- **Week 008** built. **Week 009** is next.
- Course: 121 weeks, 2026-11-06 → 2029-02-25. **97 lessons + 24 revision tests.**
- **2026 is complete:** weeks 001–008 hold lessons 001–003 and 005–007, plus tests 1 and 2.

## Lessons built

| Week | File | Title | Status |
|---|---|---|---|
| 001 | `lessons/001-121-2026-11-08.html` | Say it in your own words | ✅ Built, not yet marked |
| 002 | `lessons/002-121-2026-11-15.html` | Marks = strands | ✅ Built, not yet marked |
| 003 | `lessons/003-121-2026-11-22.html` | Reading for the literal (R1) | ✅ Built, not yet marked |
| 005 | `lessons/005-121-2026-12-06.html` | Reading for the implied (R2) | ✅ Built, not yet marked |
| 006 | `lessons/006-121-2026-12-13.html` | Attitude: what the writer feels | ✅ Built, not yet marked |
| 007 | `lessons/007-121-2026-12-20.html` | Attitude: three details that prove it | ✅ Built, not yet marked |

## Revision tests built

| # | Week | File | Covers | Length | Status |
|---|---|---|---|---|---|
| 1 | 004 | `tests/004-121-2026-11-29-test.html` | Weeks 001–003 | 15 min / 5 marks | ✅ Built, not yet sat |
| 2 | 008 | `tests/008-121-2026-12-27-test.html` | Weeks 001–007 | 15 min / 5 marks | ✅ Built, not yet sat |

## Next up

| Week | Planned file | Title |
|---|---|---|
| 009 | `lessons/009-121-2027-01-03.html` | Word meaning in context |
| 010 | `lessons/010-121-2027-01-10.html` | Finding the word that matches |
| 011 | `lessons/011-121-2027-01-17.html` | Why the writer chose that word (R4) |
| 012 | `tests/012-121-2027-01-24-test.html` | Test 3 |

Weeks 009–011 are the next teaching block, then Test 3 at week 012.

## Waiting on the learner

- **Practice answers from lessons 001, 002, 003, 005, 006 and 007**, marked strand by strand against the 2027 specimen mark schemes as they arrive.
- **Five vocabulary cards and one Sunday sentence each week**, pasted with the practice answers.
- **Revision tests 1 and 2** are sat in weeks 004 and 008 and scored in `REVISION-LOG.md`.

## Open issues

| Issue | Impact | Status |
|---|---|---|
| March series is India-only | If the centre is outside India, target must be June 2029 | Unresolved |
| No human marker | Feedback relies on AI marking against mark schemes | Accepted |
| No 2027 examiner reports exist yet | Band descriptors are the only authority | Revisit late 2027 |

## Doc housekeeping

Inconsistencies found on 2026-11-10 and left unfixed, because each one needs a decision rather than a correction. None blocks a build.

| Gap | Where | Suggested fix |
|---|---|---|
| `RESOURCES.md` is orphaned | Not referenced from `AGENTS.md` or `BUILD.md` | Add it to the read order or to `BUILD.md` §2 |
| `BUILD.md` has no §8 | Section numbering jumps §7 → §9 | Renumber §9–§11, or insert a §8 for the weekly table rules |
| `sources/update-notice-2027.*` is undocumented | Missing from the source table in `BUILD.md` §2 | Add a row; a 2027 update notice can change exam structure |
| `GLOSSARY.md` omits the vocabulary used everywhere | No entries for `R1`–`R5`, `W1`–`W5`, "AO", "band 5/6" | Add an "Assessment" block once they are next used in a lesson |
| Two "day one" dates | `ROADMAP.md` §1 and `MISSION.md` say the course begins 2026-11-06; filenames use Sunday 2026-11-08 | State the 06 as the build start and the 08 as week 001's Sunday |
| Tests 13–15 dated "Nov–Dec 2027" | `ROADMAP.md` §8, but week 052 is 2027-10-31 | Change to "Oct–Dec 2027" |

## Reference documents

| File | Status |
|---|---|
| `reference/exam-map.html` | ✅ Built — full paper map, AOs, timings, thresholds |
| `reference/reading.html` | ✅ Built — block books, the Sunday sentence task, the five-word vocabulary method |
| `lessons/index.html` | ✅ Built — course index: all 121 weeks in order, built weeks linked, future weeks plain |
| `vocabulary/bank.md` | 🟡 Template only — learner fills it weekly |

## Assets

| File | Provides |
|---|---|
| `assets/course.css` | Full visual system + print styles |
| `assets/quiz.js` | `.quiz`, `.practice`, auto-injected **Copy answer** button |

## Planned but not built

- `reference/sentence-accuracy.html` — after week 033
- `reference/form-conventions.html` — after week 067
- `reference/language-vocabulary.html` — the literary terms (simile, sibilance, connotation), after week 019. Distinct from `reference/reading.html`, which holds the vocabulary *method*.

## Session log

| Date | What happened |
|---|---|
| 2026-11-07 | Workspace created. Syllabus + 2027 specimen mark schemes downloaded to `sources/`. Lesson 001 built and renamed to the `NNN-121` scheme. `ROADMAP.md` written. |
| 2026-11-07 | `BUILD.md` and `PROGRESS.md` created; `AGENTS.md` given a Teaching workspace entry point. Lesson 002 built. |
| 2026-11-07 | **Four-week cadence adopted:** 97 lessons + 24 revision tests. Roadmap rewritten week-by-week, phase boundaries re-mapped, lessons renumbered by week only. `tests/` and `REVISION-LOG.md` created; Test 1 built as the template. |
| 2026-11-07 | Resolved a cross-file conflict on test length. `REVISION-LOG.md` listed tests 2–3 as 20 min / 8 marks; `ROADMAP.md` §8 and the built Test 1 both say tests 1–3 are **15 min / 5 marks**. Log corrected. The eyebrow example in `ROADMAP.md` §1 now uses Test 4 (week 016), the first genuinely 20-minute test. |
| 2026-11-07 | **Reading and vocabulary added as a standing part of the week.** `reference/reading.html` built: one book per four-week block at 45 minutes a Sunday, a one-sentence analysis task marked against Table E, and a five-a-week vocabulary method with a cull, retrieval and a three-words-in-Saturday rule. `vocabulary/bank.md` created as the learner's record. Lessons 001–002 updated; `ROADMAP.md` §9, `BUILD.md` §1, §7, §9 and §10 given the rule; `AGENTS.md` entry point, Test 1's audit block and the `exam-map.html` nav updated to match. Block 1 is *Once* (pp. 1–38). |
| 2026-11-07 | **2026 built out.** Lessons 003 (literal/R1), 005 (implied/R2), 006 and 007 (attitude, split into naming and proving) and Test 2 written. All from the 2027 specimen texts and mark schemes; 003 and 005 use Text A items nothing had used yet, 006–007 use the Paper 2 Q1(a) Jaz extract, and Test 2's five items come from the mark scheme's Q4 and Q2(b) indicative content so no item repeats a lesson. Quiz option lengths equalised across all six lessons, correct-answer positions rotated, and every practice box carries a `data-q`. |
| 2026-11-10 | Built `lessons/index.html` — the course index. All 121 weeks generated from `ROADMAP.md`; every parsed date was checked against the Sunday formula `2026-11-08 + 7(n−1)` and all 121 matched. Tests carry their scheduled length (15 → 50 min), mock-paper weeks carry 2 h, built weeks are links and future weeks are plain text so the page can never point at a file that does not exist. No new CSS, no `quiz.js` (the page has no quiz or practice component). Then added the repository link (`https://github.com/gcgc1/2026-11-10_Riley_IGCSE_English_preparation`) to the page's Reference list. |
| 2026-11-10 | **Workspace wrapped for handoff.** Link audit across all 11 HTML pages found one dead link — Test 2's footer pointed at the unbuilt week 009 — now pointing at the course index. Replaced the one-line README stub with a real orientation page (status, read order, map, conventions, copyright note on `sources/`). `AGENTS.md` read order now includes `REVISION-LOG.md` and names the index. Remaining doc inconsistencies recorded under **Doc housekeeping**. |