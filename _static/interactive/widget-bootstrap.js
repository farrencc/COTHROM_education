/* COTHROM widget bootstrap — shared by every interactive embedded via iframe.
 *
 * Makes a widget inherit the host page's light/dark theme. The widgets link
 * ../cothrom.css, which already carries dark token values under
 * html[data-theme="dark"]; all this needs to do is mirror the parent's
 * data-theme onto the widget's own <html> so those overrides activate.
 *
 * Widgets are served from the same origin as the pages, so the iframe can
 * read the parent DOM directly. Fallbacks cover standalone viewing and any
 * cross-origin embed (via postMessage).
 */
(function () {
  var docEl = document.documentElement;

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

  function apply() {
    docEl.setAttribute("data-theme", resolveTheme() === "dark" ? "dark" : "light");
  }

  apply();

  // Live-update when the parent toggles theme (same-origin only).
  try {
    if (window.parent && window.parent !== window) {
      new MutationObserver(apply).observe(
        window.parent.document.documentElement,
        { attributes: true, attributeFilter: ["data-theme"] }
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

  // Cross-origin fallback: host can post {type:"cothrom-theme", theme:"dark"}.
  window.addEventListener("message", function (ev) {
    var d = ev && ev.data;
    if (d && d.type === "cothrom-theme" && (d.theme === "dark" || d.theme === "light")) {
      docEl.setAttribute("data-theme", d.theme);
    }
  });
})();
