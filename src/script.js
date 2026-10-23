/* Quality Living: scroll-animated magazine card gallery.
   Plain JS (no libraries) so it runs inside a GoHighLevel Custom JS/HTML element.
   Scroll progress through the section drives 4 layouts:
   scatter -> line -> circle -> arc. In the arc, cards flip on hover / tap. */
(function () {
  function init(section) {
    if (section.dataset.qlReady) return;
    section.dataset.qlReady = "1";

    var stage = section.querySelector(".ql-gallery-stage");
    var cards = Array.prototype.slice.call(section.querySelectorAll(".ql-card"));
    var intro = section.querySelector(".ql-gallery-intro");
    var outro = section.querySelector(".ql-gallery-outro");
    var hint = section.querySelector(".ql-gallery-hint");
    var n = cards.length;
    var mid = (n - 1) / 2;
    var coverIndex = cards.findIndex(function (c) { return c.classList.contains("ql-card-cover"); });
    var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var unpinned = false;
    var ticking = false;

    if (reduced) section.classList.add("ql-static");

    // Fixed pseudo-random numbers so the scatter looks the same on every visit
    function rand(i, k) {
      var x = Math.sin(i * 127.1 + k * 311.7) * 43758.5453;
      return x - Math.floor(x);
    }

    function layouts() {
      var W = stage.clientWidth;
      var H = stage.clientHeight;
      var cw = cards[0].offsetWidth;
      var lineW = Math.min(W * 0.9 - cw, n * cw * 1.05);
      var R = Math.min(W * 0.4, H * 0.28);
      var arcR = Math.max(W * 1.4, 800);
      var arcW = Math.min(W * 0.92 - cw, n * cw * 0.72);
      var span = arcW / arcR;

      return cards.map(function (_, i) {
        var a = (i / n) * Math.PI * 2 - Math.PI / 2;
        var t = n > 1 ? (i - mid) / (n - 1) : 0;
        var arcA = t * span;
        var isCover = i === coverIndex;
        return {
          scatter: {
            x: (rand(i, 1) - 0.5) * W * 0.9,
            y: (rand(i, 2) * 0.5 - 0.12) * H, // keep clear of the heading at the top
            r: (rand(i, 3) - 0.5) * 60,
            s: 0.85
          },
          line: { x: t * lineW, y: 0, r: 0, s: 1 },
          circle: { x: R * Math.cos(a), y: R * Math.sin(a), r: (a * 180) / Math.PI + 90, s: 0.9 },
          arc: {
            x: arcR * Math.sin(arcA),
            y: -H * 0.04 + arcR * (1 - Math.cos(arcA)) + (isCover ? -cw * 0.12 : 0),
            r: (arcA * 180) / Math.PI,
            s: isCover ? 1.25 : 1
          }
        };
      });
    }

    var L = layouts();
    var stops = [["scatter", 0], ["line", 0.25], ["circle", 0.5], ["arc", 0.75]];

    function ease(t) { return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
    function clamp(v) { return Math.max(0, Math.min(1, v)); }
    function mix(a, b, t) { return a + (b - a) * t; }

    function progress() {
      if (reduced) return 1;
      var r = section.getBoundingClientRect();
      var vh = window.innerHeight;

      // Detect a GHL wrapper breaking position: sticky, and fall back to un-pinned mode
      if (!unpinned && r.top < -60 && r.bottom > vh + 60) {
        if (Math.abs(stage.getBoundingClientRect().top) > 8) {
          unpinned = true;
          section.classList.add("ql-unpinned");
          L = layouts();
          r = section.getBoundingClientRect();
        }
      }

      if (unpinned) {
        // Animate while the stage travels through the viewport
        return clamp((vh - r.top) / (vh + r.height) * 1.6 - 0.3);
      }
      return clamp(-r.top / (r.height - vh));
    }

    function render() {
      ticking = false;
      var p = progress();
      var k = 0;
      while (k < stops.length - 1 && p > stops[k + 1][1]) k++;
      var from = stops[k];
      var to = stops[Math.min(k + 1, stops.length - 1)];
      var t = to === from ? 1 : ease(clamp((p - from[1]) / (to[1] - from[1])));

      cards.forEach(function (card, i) {
        var A = L[i][from[0]];
        var B = L[i][to[0]];
        var x = mix(A.x, B.x, t);
        var y = mix(A.y, B.y, t);
        var r = mix(A.r, B.r, t);
        var s = mix(A.s, B.s, t);
        card.style.transform = "translate(" + x.toFixed(1) + "px," + y.toFixed(1) + "px) rotate(" + r.toFixed(2) + "deg) scale(" + s.toFixed(3) + ")";
        card.style.zIndex = i === coverIndex && p > 0.6 ? 20 : 10 - Math.round(Math.abs(i - mid));
      });

      var arc = p >= 0.75;
      section.classList.toggle("is-arc", arc);
      if (!arc) cards.forEach(function (c) { c.classList.remove("is-flipped"); });
      // Heading shows at the start and comes back above the finished arc
      intro.style.opacity = String(Math.max(clamp(1 - p / 0.12), clamp((p - 0.8) / 0.1)));
      hint.style.opacity = p > 0.05 ? "0" : "";
      outro.style.opacity = String(clamp((p - 0.78) / 0.12));
      outro.classList.toggle("is-visible", p > 0.85);
    }

    function onScroll() {
      if (!ticking) {
        ticking = true;
        window.requestAnimationFrame(render);
      }
    }

    // Tap to flip on touch screens (hover does it on desktop)
    cards.forEach(function (card) {
      card.addEventListener("click", function (e) {
        if (!section.classList.contains("is-arc")) return;
        if (e.target.closest("a")) return;
        card.classList.toggle("is-flipped");
      });
    });

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", function () { L = layouts(); onScroll(); });
    render();
  }

  function boot() {
    document.querySelectorAll("[data-ql-gallery]").forEach(init);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
