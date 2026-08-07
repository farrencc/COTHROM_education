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

   Reading density: lessons author paired blocks

   :::{div} cothrom-concise
   :::{div} cothrom-full

   and everything structural (headings, quizzes, widgets, sources) sits
   outside both. This file restores the reader's choice onto
   <html data-density> before first paint, injects the switch, and mirrors
   the choice into embedded widgets.
   ===================================================================== */
(function () {
  "use strict";

  /* ---------------- Reading density ---------------- */

  var DENSITY_KEY = "cothrom-density";
  var DEFAULT_DENSITY = "concise";
  var WORDS_PER_MINUTE = 200;

  function storedDensity() {
    try {
      var v = window.localStorage.getItem(DENSITY_KEY);
      return v === "concise" || v === "full" ? v : null;
    } catch (err) {
      // Private browsing or blocked storage: fall back to the default.
      return null;
    }
  }

  function rememberDensity(density) {
    try {
      window.localStorage.setItem(DENSITY_KEY, density);
    } catch (err) {
      /* Not being able to remember the choice is not worth failing over. */
    }
  }

  // Runs while the document is still parsing (this script is in <head>), so
  // the attribute is set before first paint and there is no flash of the
  // wrong density. With JS off the attribute is never set and the CSS
  // default — the full lesson — stands.
  function applyDensity(density) {
    document.documentElement.setAttribute("data-density", density);
  }
  applyDensity(storedDensity() || DEFAULT_DENSITY);

  function currentDensity() {
    return document.documentElement.getAttribute("data-density") === "full"
      ? "full"
      : "concise";
  }

  // Tell embedded widgets which density to render. Same-origin widgets read
  // the parent attribute directly; this message is the fallback path and the
  // live-update signal (see interactive/widget-bootstrap.js).
  function broadcastDensity(density) {
    var iframes = document.getElementsByTagName("iframe");
    for (var i = 0; i < iframes.length; i++) {
      if (!iframes[i].contentWindow) continue;
      try {
        iframes[i].contentWindow.postMessage(
          { type: "cothrom-density", density: density },
          "*"
        );
      } catch (err) {
        /* A widget that has not loaded yet will pick the density up itself. */
      }
    }
  }

  // Words a reader actually meets on each path: everything shared, plus the
  // blocks for that density only. Counting at runtime keeps the estimate
  // honest as the prose changes, with no figure to maintain by hand.
  function readingMinutes(article, density) {
    var hidden = density === "concise" ? ".cothrom-full" : ".cothrom-concise";
    var clone = article.cloneNode(true);
    // textContent would otherwise swallow the inline <style>/<script> of the
    // in-page calculator, which is not prose anyone reads.
    clone
      .querySelectorAll(hidden + ", script, style, iframe")
      .forEach(function (el) {
        el.parentNode.removeChild(el);
      });
    var words = (clone.textContent || "").trim().split(/\s+/).length;
    return Math.max(1, Math.round(words / WORDS_PER_MINUTE));
  }

  function initDensity() {
    // Only on pages that actually carry both densities.
    if (!document.querySelector(".cothrom-concise")) return;

    var article =
      document.querySelector(".bd-article") ||
      document.querySelector("article") ||
      document.querySelector("main");
    if (!article) return;

    var control = document.createElement("div");
    control.className = "cothrom-density";
    control.setAttribute("role", "group");
    control.setAttribute("aria-label", "Reading length");

    var label = document.createElement("span");
    label.className = "cothrom-density-label";
    label.textContent = "Reading length";
    control.appendChild(label);

    var group = document.createElement("div");
    group.className = "cothrom-density-group";
    control.appendChild(group);

    var hint = document.createElement("p");
    hint.className = "cothrom-density-hint";
    control.appendChild(hint);

    var status = document.createElement("div");
    status.className = "cothrom-density-status";
    status.setAttribute("role", "status");
    // Announced to assistive tech only; the visible hint carries the same text.
    status.style.position = "absolute";
    status.style.width = "1px";
    status.style.height = "1px";
    status.style.overflow = "hidden";
    status.style.clip = "rect(0 0 0 0)";
    status.style.whiteSpace = "nowrap";
    control.appendChild(status);

    var HINTS = {
      concise:
        "The concise version — every fact, figure and source from the full " +
        "lesson, in about half the words.",
      full:
        "The full version — each idea built up from a worked example, with " +
        "the reasoning spelled out.",
    };

    var buttons = ["concise", "full"].map(function (density) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "cothrom-density-btn";
      btn.setAttribute("data-density-choice", density);

      var name = density === "concise" ? "Concise" : "Full";
      var time = document.createElement("span");
      time.className = "cothrom-density-time";
      time.textContent = " · about " + readingMinutes(article, density) + " min";
      btn.appendChild(document.createTextNode(name));
      btn.appendChild(time);

      btn.addEventListener("click", function () {
        if (currentDensity() === density) return;
        applyDensity(density);
        rememberDensity(density);
        broadcastDensity(density);
        sync();
        status.textContent = name + " version shown.";
      });

      group.appendChild(btn);
      return btn;
    });

    function sync() {
      var density = currentDensity();
      buttons.forEach(function (btn) {
        var mine = btn.getAttribute("data-density-choice") === density;
        btn.setAttribute("aria-pressed", mine ? "true" : "false");
      });
      hint.textContent = HINTS[density];
    }
    sync();

    article.insertBefore(control, article.firstChild);

    // Widgets that finish loading after the toggle was set still need telling.
    window.addEventListener("load", function () {
      broadcastDensity(currentDensity());
    });
  }

  /* ---------------- Embedded widgets ---------------- */

  // Resize an embedded widget iframe to the content height it reports
  // (see widget-bootstrap.js). Registered immediately so it catches
  // height messages that arrive before DOMContentLoaded.
  window.addEventListener("message", function (e) {
    var d = e && e.data;
    if (!d || d.type !== "cothrom-height" || typeof d.height !== "number") return;
    var iframes = document.getElementsByTagName("iframe");
    for (var i = 0; i < iframes.length; i++) {
      if (iframes[i].contentWindow === e.source) {
        iframes[i].style.height = Math.ceil(d.height) + "px";
        iframes[i].setAttribute("scrolling", "no");
        break;
      }
    }
  });

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
    initDensity();
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
