<div class="vk-group-widget-wrap">

<div id="vk_groups"></div>

</div>

<script type="text/javascript">

(function () {

  function initVkGroupWidget() {

    if (typeof VK === "undefined" || !VK.Widgets) return;

    requestAnimationFrame(function () {

      var wrap = document.querySelector(".vk-group-widget-wrap");

      var w = wrap ? Math.max(120, Math.floor(wrap.getBoundingClientRect().width)) : 400;

      VK.Widgets.Group("vk_groups", {mode: 4, no_cover: 1, width: w, height: 400, color1: "FFFFFF", color2: "000000", color3: "5181B8"}, 220578116);

    });

  }

  if (document.readyState === "loading") {

    document.addEventListener("DOMContentLoaded", initVkGroupWidget);

  } else {

    initVkGroupWidget();

  }

})();

</script>

