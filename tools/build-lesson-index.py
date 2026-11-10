"""Builds `lessons/index.html` — the course index — from `ROADMAP.md`.

ROADMAP.md is the source of truth for week numbers, dates and titles. Every parsed
date is checked against Sunday(n) = 2026-11-08 + 7(n-1), and the script refuses to
write if any week is missing or any date has drifted.

Built weeks are discovered by scanning `lessons/` and `tests/`, and their link text
comes from each page's <h1>, so the index cannot disagree with the file it points at.

Run from anywhere:

    python tools/build-lesson-index.py
"""

import html
import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "lessons"
TESTS = ROOT / "tests"

PHASES = [
    (1, 43, "Phase 0 · Foundations", "Nov 2026 – Aug 2027"),
    (44, 86, "Phase 1 · Full coverage", "Sep 2027 – Jun 2028"),
    (87, 99, "Phase 2 · Timing &amp; repair", "Jul – Sep 2028"),
    (100, 121, "Phase 3 · Exam cycle", "Oct 2028 – Feb 2029"),
]

# Weeks holding a full timed paper: Paper 1 in the first, Paper 2 in the second.
MOCK_WEEKS = {100, 101, 108, 109}


def sunday(n: int) -> date:
    return date(2026, 11, 8) + timedelta(days=7 * (n - 1))


def test_minutes(week: int) -> int:
    n = week // 4
    for limit, minutes in ((3, 15), (6, 20), (9, 25), (12, 30), (15, 35), (18, 40), (21, 45), (24, 50)):
        if n <= limit:
            return minutes
    raise ValueError(week)


# --- parse ROADMAP ---------------------------------------------------------

roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
plan = {}
for line in roadmap.splitlines():
    m = re.match(r"^\|\s*(\d{3})\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(.+?)\s*\|\s*$", line)
    if not m:
        continue
    week, ds, item = int(m.group(1)), m.group(2), m.group(3)
    is_test = bool(re.search(r"\*\*TEST \d+\*\*", item))
    item = item.replace("✅", "")
    item = re.sub(r"\*\*(L\d+|TEST \d+)\*\*", "", item)
    item = item.replace("**", "").strip()
    plan[week] = (ds, item, is_test)

missing = [w for w in range(1, 122) if w not in plan]
assert not missing, f"weeks missing from ROADMAP: {missing}"
drift = [(w, plan[w][0], sunday(w).isoformat()) for w in plan if plan[w][0] != sunday(w).isoformat()]
assert not drift, f"date drift: {drift}"

# --- read what is actually built ------------------------------------------

built = {}
for path in LESSONS.glob("*.html"):
    m = re.match(r"^(\d{3})-121-\d{4}-\d{2}-\d{2}\.html$", path.name)
    if not m:
        continue
    week = int(m.group(1))
    h1 = re.search(r"<h1>(.+?)</h1>", path.read_text(encoding="utf-8"), re.S).group(1).strip()
    built[week] = (f"{path.name}", h1, "lesson")

for path in TESTS.glob("*-test.html"):
    m = re.match(r"^(\d{3})-121-\d{4}-\d{2}-\d{2}-test\.html$", path.name)
    if not m:
        continue
    week = int(m.group(1))
    h1 = re.search(r"<h1>(.+?)</h1>", path.read_text(encoding="utf-8"), re.S).group(1).strip()
    built[week] = (f"../tests/{path.name}", h1, "test")

lesson_weeks = sorted(w for w, v in built.items() if v[2] == "lesson")
test_weeks = sorted(w for w, v in built.items() if v[2] == "test")

# --- build the tables -----------------------------------------------------

def row(week: int) -> str:
    ds, item, is_test = plan[week]
    if week in built:
        href, title, _kind = built[week]
        cell = f'<a href="{html.escape(href)}">{html.escape(title)}</a>'
    else:
        title = f"Revision test {week // 4}" if is_test else item
        cell = html.escape(title)
    if is_test:
        cell += f' · <span class="num">{test_minutes(week)} min</span>'
    elif week in MOCK_WEEKS:
        cell += ' · <span class="num">2 h</span>'
    return (
        f'      <tr><td class="num">{week:03d}</td><td class="num">{ds}</td>'
        f"<td>{cell}</td></tr>"
    )


def phase_block(start: int, end: int, name: str, span: str) -> str:
    rows = "\n".join(row(w) for w in range(start, end + 1))
    return f"""  <h3>{name}</h3>

  <div class="table-wrap">
  <table>
    <caption>Weeks {start:03d}–{end:03d} · {span}</caption>
    <thead><tr><th>Week</th><th>Due (Sunday)</th><th>Item</th></tr></thead>
    <tbody>
{rows}
    </tbody>
  </table>
  </div>"""


phases = "\n\n".join(phase_block(*p) for p in PHASES)

def upcoming_row(week: int) -> str:
    ds, item, is_test = plan[week]
    cell = html.escape(f"Revision test {week // 4}" if is_test else item)
    if is_test:
        cell += f' · <span class="num">{test_minutes(week)} min</span>'
    return f'      <tr><td class="num">{week:03d}</td><td class="num">{ds}</td><td>{cell}</td></tr>'


upcoming = "\n".join(upcoming_row(w) for w in (9, 10, 11, 12))

next_week = 9
next_due = plan[next_week][0]
built_count = len(built)

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Course index — every week of 0500</title>
<link rel="stylesheet" href="../assets/course.css">
</head>
<body>
<main class="page page--wide">

  <p class="eyebrow">Course index · 121 weeks · 2026-11-06 → 2029-02-25</p>
  <h1>The whole course, week by week</h1>
  <p class="lede">Ninety-seven lessons and twenty-four tests, in the order you meet them. Every week already written is a link. Every other week is the plan, so you always know what is coming and how far you have come.</p>

  <div class="meta">
    <span>{built_count} of 121 weeks built</span>
    <span>{len(lesson_weeks)} lessons · {len(test_weeks)} tests</span>
    <span>Next: week {next_week:03d}, due {next_due}</span>
    <span>Target: 54/80 per paper</span>
  </div>

  <div class="callout">
    <span class="callout__label">Start here</span>
    <p><strong>If you are starting today, open week 001, not the newest file.</strong> Each lesson assumes the habit the week before it built. Working backwards through the archive puts you at week eight with the skills of week one.</p>
    <p>Week {next_week:03d} is the week you are on. Everything after it stays unbuilt until it is needed — a lesson you cannot use yet is a lesson written without knowing what you got wrong.</p>
  </div>

  <h2>Next up</h2>

  <p>One lesson a week, then a test every fourth week. Weeks 009–011 teach; week 012 tests them, cumulatively.</p>

  <div class="table-wrap">
  <table>
    <caption>The next four weeks</caption>
    <thead><tr><th>Week</th><th>Due (Sunday)</th><th>Item</th></tr></thead>
    <tbody>
{upcoming}
    </tbody>
  </table>
  </div>

  <h2>The whole course</h2>

  <p>Tests fall at weeks <span class="num">004, 008, 012 … 096</span> — every fourth week, twenty-four of them, each longer and broader than the last. Phase 3 drops the four-week rule: the mock cycle is the assessment there.</p>

{phases}

  <h2>How to work through a week</h2>

  <ol>
    <li><strong>Monday — the lesson.</strong> Read it top to bottom before you write anything. If a section is unclear, ask before attempting the boxes; a misunderstood skill practised three times is three times harder to unlearn.</li>
    <li><strong>Monday — the practice boxes.</strong> Press <strong>Copy answer</strong> after each one and paste it into this chat. The page saves nothing: if it is not pasted, it is gone.</li>
    <li><strong>Tuesday — marking and repair.</strong> Read the strand-by-strand marking, then rewrite the weakest answer. The rewrite is where the mark is won.</li>
    <li><strong>Wednesday — retrieval.</strong> The quiz cold, no scrolling back, then five words from your bank, from memory. Add three more bank words to Saturday's writing, underlined.</li>
    <li><strong>Thursday — apply.</strong> One real exam question of the current type, timed.</li>
    <li><strong>Saturday — write.</strong> 350–450 words. <strong>Sunday — read</strong> the block book, 45 minutes, and bring one sentence.</li>
    <li><strong>After a test</strong>, record the score and the weakest question type in <code>REVISION-LOG.md</code>. That column, not the average, decides what the next repair lesson is.</li>
  </ol>

  <h2>Reference</h2>

  <ul>
    <li><a href="../reference/exam-map.html">The exam map</a> — every question, mark and assessment objective, on one page.</li>
    <li><a href="../reference/reading.html">Reading &amp; vocabulary</a> — the block books, the Sunday sentence task and the five-word method.</li>
    <li><a href="../vocabulary/bank.md">The vocabulary bank</a> — your cards, five a week, six kept per block.</li>
    <li><a href="../REVISION-LOG.md">The revision log</a> — every test score, and the errors that keep repeating.</li>
    <li><a href="https://github.com/gcgc1/2026-11-10_Riley_IGCSE_English_preparation">This course on GitHub</a> — the whole repository: every lesson, test, mark scheme and log in one place.</li>
  </ul>

  <div class="ask-teacher">
    <p><strong>I am your teacher — ask me anything.</strong> Paste a practice answer, a Sunday sentence or a full test script into the chat and I will mark it against the real 2027 mark scheme, strand by strand, and name the band. If you are unsure which week to start, tell me what you can already do and I will place you.</p>
  </div>

  <nav class="footer-nav no-print">
    <a href="001-121-2026-11-08.html">
      <span class="dir">Start of the course · Week 001</span>
      Say it in your own words
    </a>
    <a href="../reference/exam-map.html">
      <span class="dir">Reference</span>
      The exam map — every question, mark and objective
    </a>
  </nav>

</main>
</body>
</html>
"""

out = LESSONS / "index.html"
out.write_text(page, encoding="utf-8")
print(f"wrote {out} ({len(page.splitlines())} lines)")
print(f"built: lessons {lesson_weeks} · tests {test_weeks}")
print(f"week 009 -> {plan[9][0]}, title {plan[9][1]!r}")
