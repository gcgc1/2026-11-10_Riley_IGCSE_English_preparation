/* ==========================================================================
   quiz.js — shared interactive components for the 0500 teaching workspace
   No dependencies. Include with <script src="../assets/quiz.js" defer></script>

   QUIZ
   ----
   <div class="quiz">
     <p class="quiz__prompt"><span class="quiz__num">Question 1</span> Prompt text</p>
     <ul class="quiz__options">
       <li><button class="quiz__option" data-correct data-why="Why this is right.">Option A</button></li>
       <li><button class="quiz__option" data-why="Why this is wrong.">Option B</button></li>
     </ul>
     <div class="quiz__feedback" hidden></div>
   </div>

   PRACTICE
   --------
   <div class="practice" data-practice data-max="120">
     <p class="practice__prompt">Prompt</p>
     <p class="practice__hint">Hint</p>
     <textarea placeholder="Write here…"></textarea>
     <div class="practice__bar">
       <span class="wordcount">0 words</span>
       <button class="btn btn--ghost" data-reveal>Show model answer</button>
     </div>
     <div class="model" hidden>
       <span class="model__label">Model answer</span>
       …
     </div>
   </div>
   ========================================================================== */

(function () {
  "use strict";

  /* ---------------- quizzes ---------------- */

  var quizzes = Array.prototype.slice.call(document.querySelectorAll(".quiz"));
  var answered = 0;
  var correct = 0;

  function scoreLine() {
    if (!quizzes.length) return;
    var el = document.getElementById("quiz-score");
    if (!el) {
      el = document.createElement("p");
      el.id = "quiz-score";
      el.className = "quiz__score";
      var last = quizzes[quizzes.length - 1];
      last.parentNode.insertBefore(el, last.nextSibling);
    }
    el.textContent = answered + " of " + quizzes.length + " answered · " + correct + " correct";
  }

  quizzes.forEach(function (quiz) {
    var options = Array.prototype.slice.call(quiz.querySelectorAll(".quiz__option"));
    var feedback = quiz.querySelector(".quiz__feedback");

    options.forEach(function (btn) {
      btn.type = "button";
      btn.addEventListener("click", function () {
        if (quiz.dataset.done === "true") return;
        quiz.dataset.done = "true";

        var isRight = btn.hasAttribute("data-correct");
        var rightBtn = options.filter(function (o) {
          return o.hasAttribute("data-correct");
        })[0];

        options.forEach(function (o) {
          o.disabled = true;
          if (o === rightBtn) o.classList.add("is-correct");
          else if (o === btn) o.classList.add("is-wrong");
          else o.classList.add("is-muted");
        });

        answered += 1;
        if (isRight) correct += 1;

        if (feedback) {
          var why = btn.getAttribute("data-why") || "";
          var rightWhy = rightBtn ? rightBtn.getAttribute("data-why") || "" : "";
          var html = "";
          if (isRight) {
            html += "<strong>Correct.</strong> " + why;
          } else {
            html += "<strong>Not quite.</strong> " + why;
            if (rightWhy) html += " <strong>The answer:</strong> " + rightWhy;
          }
          feedback.innerHTML = html;
          feedback.hidden = false;
        }

        scoreLine();
      });
    });
  });

  /* ---------------- practice boxes ---------------- */

  function countWords(text) {
    var t = text.trim();
    if (!t) return 0;
    return t.split(/\s+/).length;
  }

  /* ---------------- copy helper ---------------- */

  function currentFile() {
    var name = "";
    try {
      name = decodeURIComponent(window.location.pathname.split("/").pop() || "");
    } catch (e) {
      name = "";
    }
    return name || document.title || "lesson";
  }

  function legacyCopy(text, onDone, onFail) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.top = "-1000px";
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
      onDone();
    } catch (e) {
      onFail();
    }
    document.body.removeChild(ta);
  }

  function copyText(text, onDone, onFail) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(onDone, function () {
        legacyCopy(text, onDone, onFail);
      });
    } else {
      legacyCopy(text, onDone, onFail);
    }
  }

  /* ---------------- practice boxes ---------------- */

  var practiceBoxes = Array.prototype.slice.call(
    document.querySelectorAll("[data-practice]")
  );

  practiceBoxes.forEach(function (box, boxIndex) {
    var area = box.querySelector("textarea");
    var counter = box.querySelector(".wordcount");
    var reveal = box.querySelector("[data-reveal]");
    var model = box.querySelector(".model");
    var max = parseInt(box.getAttribute("data-max") || "0", 10);

    if (area && counter) {
      var update = function () {
        var n = countWords(area.value);
        counter.textContent = n + (n === 1 ? " word" : " words") + (max ? " / " + max + " max" : "");
        counter.classList.toggle("is-over", max > 0 && n > max);
      };
      area.addEventListener("input", update);
      update();
    }

    if (reveal && model) {
      reveal.type = "button";
      reveal.addEventListener("click", function () {
        var open = !model.hidden;
        model.hidden = open;
        reveal.textContent = open ? "Show model answer" : "Hide model answer";
      });
    }

    /* The lesson page cannot talk to the chat. The learner writes here,
       copies the text, and pastes it into the conversation. */
    if (area) {
      var bar = box.querySelector(".practice__bar");
      if (bar) {
        var copyBtn = document.createElement("button");
        copyBtn.type = "button";
        copyBtn.className = "btn btn--ghost";
        copyBtn.textContent = "Copy answer";

        copyBtn.addEventListener("click", function () {
          function done() {
            copyBtn.textContent = "Copied — paste it in the chat";
            window.setTimeout(function () {
              copyBtn.textContent = "Copy answer";
            }, 2400);
          }
          function fail() {
            copyBtn.textContent = "Copy failed — select and press Ctrl+C";
          }

          var q = box.getAttribute("data-q") || String(boxIndex + 1);
          var payload =
            currentFile() + ", Q" + q + ", " + area.value.trim();

          copyText(payload, done, fail);
        });

        if (reveal) bar.insertBefore(copyBtn, reveal);
        else bar.appendChild(copyBtn);
      }
    }
  });
})();
