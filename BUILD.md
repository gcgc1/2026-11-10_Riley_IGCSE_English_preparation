# How to build a lesson in this workspace

You are building lessons for a learner working towards **grade A in Cambridge IGCSE First Language English (0500), Papers 1 and 2, March 2029.** Read this before writing anything.

## 1. Read these first, in this order

1. `MISSION.md` — why the learner is doing this
2. `ROADMAP.md` — all 121 weeks, every lesson title, the naming formula
3. `PROGRESS.md` — what is built, what is next
4. `GLOSSARY.md` — the canonical terms; use them
5. `NOTES.md` — learner preferences and working notes
6. `REVISION-LOG.md` — every test score, and the errors that keep repeating
7. `reference/reading.html` — the block book, the Sunday sentence task, the vocabulary method

## 2. Where the truth lives

Never teach from memory. The syllabus changed for 2027 and almost every online guide describes the **old** exam.

`sources/` holds the Cambridge documents, extracted to `.txt` so they can be searched:

| File | What it is |
|---|---|
| `0500-syllabus-2027-2029.txt` | The syllabus. Structure, AOs, word limits. |
| `p1-ms-2027.txt` | **Paper 1 mark scheme** — every band descriptor |
| `p2-ms-2027.txt` | **Paper 2 mark scheme** — every band descriptor |
| `p1-2027.txt`, `p1-insert-2027.txt` | Paper 1 specimen + reading texts |
| `p2-2027.txt`, `p2-insert-2027.txt` | Paper 2 specimen + reading texts |

Find a band descriptor with grep or a plain read:

```
grep -n "Table E" sources/p1-ms-2027.txt     # Q3(d), 10 marks
grep -n "Table B" sources/p2-ms-2027.txt     # P2 1(b) writing, 25 marks
grep -n "Table D" sources/p2-ms-2027.txt     # composition content, 16 marks
```

Question → mark scheme section:

| Question | Section in the mark scheme |
|---|---|
| P1 Q1 items | "Overview of items for Question 1", then the item-by-item answers |
| P1 Q2(a) | Table A (reading, 10) and Table B (writing, 5) |
| P1 Q2(b) | Table C (reading, 5) |
| P1 Q3(c) | Table D (reading, 5) |
| P1 Q3(d) | Table E (reading, 10) |
| P1 Q4 | Table F (reading, 10), Table G (writing, 10) |
| P2 Q1(a) | Table A (reading, 5) |
| P2 Q1(b) | Table B (writing, 25), Table C (reading, 10) |
| P2 Section B | Table D (content & structure, 16), Table E (style & accuracy, 24) |

If a PDF's text extraction looks broken, re-run `python sources/extract_all.py`.

## 3. File naming

```
NNN-121-YYYY-MM-DD.html
```

- `NNN` — week number, 3 digits, starting `001` on 2026-11-06
- `121` — total weeks in the course
- `YYYY-MM-DD` — the **Sunday** of that week

**Formula:** Sunday(n) = `2026-11-08 + 7 × (n − 1)` days.

**`lessons/index.html` is the course index** — every week 001–121 in one place, built weeks linked, future weeks plain. Regenerate it with `python tools/build-lesson-index.py`. That script reads `ROADMAP.md` and fails loudly if a week is missing or a date has drifted from the Sunday formula, so correct the roadmap and rebuild rather than hand-editing the table. It picks up each newly built week automatically, and it must never point at a page that does not exist. The page links `course.css` only — there is no quiz or practice component on it, so no `quiz.js`.

## 4. The lesson contract

Every lesson has these eight parts, in this order. Do not omit any.

| Part | Content | Rule |
|---|---|---|
| Eyebrow + title + lede | `Week NNN (121) · Due: YYYY-MM-DD · Lesson · Paper X` | Week number and course total, the due date (that week's Sunday — the same one in the filename), and the paper. One number only: the week. |
| Meta strip | Time, "one skill", questions unlocked | Realistic time — aim under 15 minutes |
| Why this, now | Motivation | **Quote the actual mark scheme** at least once |
| The knowledge | Only what the skill needs | Short. Difficulty is the enemy of acquisition. |
| Worked example | Show the standard | Always a real specimen or past-paper text |
| Check yourself | 3–4 quiz items | Retrieval, not recognition |
| Now do it | 2–3 practice boxes | Model answer hidden behind a reveal button |
| Close | Primary source + ask-teacher + nav | Link previous lesson ← → next lesson + one reference doc |

## 5. Component API

Link both, in this order, in `<head>`:

```html
<link rel="stylesheet" href="../assets/course.css">
<script src="../assets/quiz.js" defer></script>
```

### Quiz

```html
<div class="quiz">
  <p class="quiz__prompt"><span class="quiz__num">Question 1</span>Prompt text</p>
  <ul class="quiz__options">
    <li><button class="quiz__option" data-correct data-why="Why this is right.">Option A</button></li>
    <li><button class="quiz__option" data-why="Why this is wrong.">Option B</button></li>
  </ul>
  <div class="quiz__feedback" hidden></div>
</div>
```

Rules for quiz items:
- **Every option the same number of words** (and characters where possible)
- **Vary which position holds the correct answer** across the lesson
- **Every option needs `data-why`** — wrong options teach
- 4 options is the default

### Practice box

```html
<div class="practice" data-practice data-max="120" data-q="1">
  <p class="practice__prompt">Prompt</p>
  <p class="practice__hint">Hint</p>
  <textarea placeholder="Write here…"></textarea>
  <div class="practice__bar">
    <span class="wordcount">0 words</span>
    <button class="btn btn--ghost" data-reveal>Show model answer</button>
  </div>
  <div class="model" hidden>
    <span class="model__label">Model answer</span>
    <p>…</p>
  </div>
</div>
```

`data-max` sets the word-count limit. Always put the **mark scheme's own accepted answers** in the model, not your invention.

`quiz.js` automatically adds a **Copy answer** button to every `.practice__bar`, so the learner can lift their text into the chat. Do not add one manually. The textarea itself saves nothing — every lesson must say so, using the "Where your answers go" callout.

**Always set `data-q`** on every practice box. The copy button writes a self-labelling payload:

```
001-121-2026-11-08.html, Q1, <the learner's answer>
```

The filename is read from the page URL, so the pasted answer always says which lesson and which question it belongs to. If `data-q` is missing it falls back to the box's position on the page — do not rely on that.

## 6. CSS classes available

Layout: `.page`, `.page--wide`
Masthead: `.eyebrow`, `.lede`, `.meta`
Text: `.callout` (+ `--warn`, `--source`), `.callout__label`, `.extract` (with `<cite>`), `mark`
Tables: `.table-wrap`, `.bands` (for level-marker tables), `.num`
Components: `.quiz`, `.practice`, `.model`, `.wordcount`
Navigation: `.footer-nav` (with `.dir`), `.ask-teacher`
Utility: `.no-print`

Do not write inline styles except the occasional one-liner already used in existing lessons. If a new visual pattern is needed in two lessons, add it to `course.css` and document it here.

## 7. Content rules

- **One skill per lesson.** If the title needs an "and", split it.
- Cite the mark scheme by name in the "Why this" section.
- Use **real texts** from `sources/`. Never invent a passage.
- The answer to any "in your own words" task is the mark scheme's accepted list.
- End with a task the learner produces and the teacher marks.
- Remind the learner they can ask you questions.
- Link to **one** high-trust source, usually the relevant Cambridge specimen mark scheme page.
- **The weekly table carries the reading habit.** Its Sunday row names the block book and page range (from `reference/reading.html`), its Wednesday row adds five vocabulary-bank words, and its Saturday row demands three bank words, underlined. Link `reference/reading.html` inline in the Sunday row — never from the footer nav, which keeps its single reference doc.

## 9. Revision tests

Every **fourth week** is a revision test, not a lesson. Tests live in `tests/` and keep the week-based filename with a `-test` suffix:

```
tests/004-121-2026-11-29-test.html
```

A test has a **different anatomy** from a lesson:

| Part | Content |
|---|---|
| Eyebrow | `Revision test N (24) · Week NNN · Due: YYYY-MM-DD · MM minutes` |
| Instructions | Closed book, no dictionary, timing, "do not open the mark scheme until you finish" |
| Extract | Real text from `sources/`, with the tested words in `<strong>` |
| Questions | 5–15 items, each in a `.practice` box **without** a per-question reveal |
| Mark scheme | One `.practice` box at the end with `data-reveal` and accepted answers |
| Score guide | What the score means and what to do next |
| Log | Remind the learner to record the score in `REVISION-LOG.md` |

Rules:
- **Cumulative and interleaved** — roughly 60% older material, 40% from the last block.
- **Escalating length** — see the schedule in `ROADMAP.md` §8.
- Never reuse an item the learner has already answered in a lesson.
- Never number lessons separately from weeks.
- The Tuesday after a test adds the **five-minute vocabulary audit**: ten words from the learner's kept list, one new sentence each. Any word failed three times stays in the bank rather than counting as owned.

## 10. Quality gates

A lesson is not finished until all of these are true:

- [ ] Completes in under ~15 minutes of learner time
- [ ] Cites the mark scheme at least once
- [ ] Every quiz option is the same length
- [ ] Correct quiz answer position varies
- [ ] Every option has `data-why`
- [ ] Practice boxes have real mark scheme answers
- [ ] The Sunday row names the block book and pages; the Saturday row demands three bank words
- [ ] Links to the previous week, the next week, and a reference doc
- [ ] Added to `PROGRESS.md`
- [ ] Opened for the learner: `Start-Process ".\lessons\<file>.html"`

A test is not finished until:

- [ ] Timed, and the timing is stated in minutes
- [ ] Every item comes from a real mark scheme
- [ ] No item repeats one used in a lesson
- [ ] The mark scheme is hidden behind a single reveal
- [ ] A row exists in `REVISION-LOG.md`

## 11. Standing facts

- Grade A ≈ **107/160 ≈ 67% ≈ 54/80 per paper**
- Paper 1: 2h, 80 marks, four 20-mark questions, 80% reading
- Paper 2: 2h, 80 marks, Section A 40 + Section B 40, 80% writing
- Assessment objectives: R1–R5 (reading), W1–W5 (writing)
- Target: **March 2029**, 121 weeks. Caveat: the March series is **India only** — see `MISSION.md`