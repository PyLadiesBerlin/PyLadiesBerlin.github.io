function toggleNavbarBgOnScroll() {
  var $nav = $("#mainNavbar");
  var $navHeight = $nav.height();
  var className = "scrolled";

  $(document).on("scroll", function() {
    $nav.toggleClass(className, $(this).scrollTop() > $navHeight);
  });
}

$(document).ready(function() {
  toggleNavbarBgOnScroll();
});
