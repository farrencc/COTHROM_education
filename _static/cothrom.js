/* =====================================================================
   COTHROM interactive learning components.

   Knowledge-check markup (authored in content):

   <div class="cothrom-quiz" data-answer="1">
     <p class="cothrom-quiz-q">Question?</p>
     <button class="cothrom-opt" data-explain="Why this is wrong.">Option A</button>
     <button class="cothrom-opt" data-explain="Why this is right.">Option B</button>
     <button class="cothrom-opt" data-explain="Why this is wrong.">Option C</button>
   </div>

   - data-answer is the 0-based index of the correct option.
   - Each option may carry data-explain with a short explanation.
   Glossary tooltips are handled in CSS via .cothrom-term[data-def]; here we
   just make them keyboard-focusable.
   ===================================================================== */
(function () {
  "use strict";

  function initQuiz(quiz) {
    var answer = parseInt(quiz.getAttribute("data-answer"), 10);
    var options = Array.prototype.slice.call(quiz.querySelectorAll(".cothrom-opt"));

    var feedback = document.createElement("div");
    feedback.className = "cothrom-feedback";
    feedback.setAttribute("role", "status");
    quiz.appendChild(feedback);

    var tag = quiz.querySelector(".cothrom-quiz-tag");
    if (!tag) {
      tag = document.createElement("span");
      tag.className = "cothrom-quiz-tag";
      tag.textContent = "Knowledge check";
      quiz.insertBefore(tag, quiz.firstChild);
    }

    options.forEach(function (opt, index) {
      opt.setAttribute("type", "button");
      opt.addEventListener("click", function () {
        var correct = index === answer;

        options.forEach(function (o, i) {
          o.classList.remove("is-correct", "is-wrong");
          o.disabled = true;
          if (i === answer) o.classList.add("is-correct");
        });
        if (!correct) opt.classList.add("is-wrong");

        var explain = opt.getAttribute("data-explain") || "";
        feedback.className = "cothrom-feedback show " + (correct ? "correct" : "incorrect");
        feedback.innerHTML =
          "<strong>" + (correct ? "Correct. " : "Not quite. ") + "</strong>" + explain +
          (correct ? "" : " Try again, or read the highlighted answer.");

        // Allow another attempt after a wrong answer.
        if (!correct) {
          setTimeout(function () {
            options.forEach(function (o) {
              o.disabled = false;
              o.classList.remove("is-correct", "is-wrong");
            });
          }, 1800);
        }
      });
    });
  }

  function init() {
    document.querySelectorAll(".cothrom-quiz").forEach(initQuiz);
    document.querySelectorAll(".cothrom-term").forEach(function (term) {
      if (!term.hasAttribute("tabindex")) term.setAttribute("tabindex", "0");
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
