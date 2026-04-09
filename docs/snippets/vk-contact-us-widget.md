<div class="vk-contact-us-widget-wrap">

<div id="vk_contact_us"></div>

</div>

<script type="text/javascript">

(function () {

  var attempts = 0;

  var maxAttempts = 150;

  function initVkContactUs() {

    if (typeof VK !== "undefined" && VK.Widgets && VK.Widgets.ContactUs) {

      VK.Widgets.ContactUs("vk_contact_us", {text: "Напишите нам", height: 30}, -220578116);

      return;

    }

    attempts++;

    if (attempts < maxAttempts) {

      requestAnimationFrame(initVkContactUs);

    }

  }

  if (document.readyState === "loading") {

    document.addEventListener("DOMContentLoaded", initVkContactUs);

  } else {

    initVkContactUs();

  }

})();

</script>

