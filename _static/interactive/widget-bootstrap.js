/* COTHROM widget bootstrap — shared by every interactive embedded via iframe.
 *
 * Makes a widget inherit two things from the host page: its light/dark theme
 * and its Concise/Full reading density. The widgets link ../cothrom.css,
 * which already carries the dark token values under html[data-theme="dark"]
 * and the density rules under html[data-density="concise"]; all this needs to
 * do is mirror the parent's data-theme and data-density onto the widget's own
 * <html> so those rules activate.
 *
 * Widgets are served from the same origin as the pages, so the iframe can
 * read the parent DOM directly. Fallbacks cover standalone viewing and any
 * cross-origin embed (via postMessage).
 *
 * Jupyter Book adds every .js file under _static/ to html_js_files, so this
 * script is also pulled into the lesson pages themselves, where it must do
 * nothing at all — the lesson pages own their data-theme (pydata) and
 * data-density (cothrom.js), and mirroring would clobber both. Widget
 * documents opt in with <html data-cothrom-widget>; everything else exits
 * here.
 */
(function () {
  var docEl = document.documentElement;

  if (!docEl.hasAttribute("data-cothrom-widget")) return;

  function resolveTheme() {
    // 1) Same-origin parent: mirror the theme pydata resolves onto <html>.
    try {
      if (window.parent && window.parent !== window) {
        var pt = window.parent.document.documentElement.getAttribute("data-theme");
        if (pt === "dark" || pt === "light") return pt;
      }
    } catch (e) {
      /* cross-origin — fall through to the media query */
    }
    // 2) Standalone / auto: follow the OS preference.
    return window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function resolveDensity() {
    // 1) Same-origin parent: mirror the density cothrom.js resolved onto <html>.
    try {
      if (window.parent && window.parent !== window) {
        var pd = window.parent.document.documentElement.getAttribute("data-density");
        if (pd === "concise" || pd === "full") return pd;
      }
    } catch (e) {
      /* cross-origin — fall through to the default */
    }
    // 2) Standalone / cross-origin: the same default the pages use.
    return "concise";
  }

  function apply() {
    docEl.setAttribute("data-theme", resolveTheme() === "dark" ? "dark" : "light");
    docEl.setAttribute("data-density", resolveDensity());
  }

  apply();

  // Live-update when the parent toggles theme or reading length (same-origin).
  try {
    if (window.parent && window.parent !== window) {
      new MutationObserver(apply).observe(
        window.parent.document.documentElement,
        { attributes: true, attributeFilter: ["data-theme", "data-density"] }
      );
    }
  } catch (e) {
    /* ignore */
  }

  // Live-update on OS preference change (standalone / auto).
  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    if (mq.addEventListener) mq.addEventListener("change", apply);
    else if (mq.addListener) mq.addListener(apply);
  }

  // Cross-origin fallback: the host can post {type:"cothrom-theme", theme:"dark"}
  // or {type:"cothrom-density", density:"full"}.
  window.addEventListener("message", function (ev) {
    var d = ev && ev.data;
    if (!d) return;
    if (d.type === "cothrom-theme" && (d.theme === "dark" || d.theme === "light")) {
      docEl.setAttribute("data-theme", d.theme);
    }
    if (d.type === "cothrom-density" && (d.density === "concise" || d.density === "full")) {
      docEl.setAttribute("data-density", d.density);
    }
  });

  /* --- Auto-height: report content height so the host can size the iframe.
     Skipped when standalone, or when the widget opts out with
     data-cothrom-fixed-height (e.g. the full-viewport map in ed_finder). --- */
  if (window.parent && window.parent !== window &&
      !docEl.hasAttribute("data-cothrom-fixed-height")) {
    var lastH = 0;
    function reportHeight() {
      var h = Math.max(
        document.body ? document.body.scrollHeight : 0,
        docEl.scrollHeight
      );
      // Guard against a resize/observe feedback loop: only post real changes.
      if (h && h !== lastH) {
        lastH = h;
        window.parent.postMessage({ type: "cothrom-height", height: h }, "*");
      }
    }
    function startHeightReporting() {
      reportHeight();
      // React to content that grows/shrinks (e.g. an interactive reveal).
      if (window.ResizeObserver && document.body) {
        new ResizeObserver(reportHeight).observe(document.body);
      }
    }
    window.addEventListener("resize", reportHeight);
    window.addEventListener("load", reportHeight);
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", startHeightReporting);
    } else {
      startHeightReporting();
    }
    // A late pass after fonts/async layout settle.
    setTimeout(reportHeight, 400);
  }
})();
