$(document).ready(function () {
  const navLinks = $(".nav-links");
  const navMid = $(".nav-mid");

  if (window.innerWidth < 768) {
    navLinks.addClass("nav-links-up");
    navMid.addClass("nav-mid-up");
  }

  $(".message-container").hover(function () {
    $(this).addClass("hidden");
    $(this).removeClass("message-container");
  });
}),
  // Hamburger menu script

  $("#hamburger-menu").on("click", function () {
    this.classList.toggle("active");

    const navLinks = $(".nav-links");
    const navMid = $(".nav-mid");

    $(".fa-bars").is(":visible")
      ? $(".fa-bars").slideUp(100)
      : $(".fa-bars").slideDown(100);
    $(".fa-chevron-down").is(":visible")
      ? $(".fa-chevron-down").slideUp(100)
      : $(".fa-chevron-down").slideDown(100);

    //

    if (navLinks.hasClass("nav-links-down")) {
      navLinks.removeClass("nav-links-down").addClass("nav-links-up");
      navMid.removeClass("nav-mid-down").addClass("nav-mid-up");
    } else {
      navLinks.removeClass("nav-links-up").addClass("nav-links-down");
      navMid.removeClass("nav-mid-up").addClass("nav-mid-down");
    }
  });

$(window).on("resize", function () {
  const win = $(this);
  const navLinks = $(".nav-links");
  const navMid = $(".nav-mid");

  if (win.width() >= 768) {
    navLinks
      .removeClass("nav-links-up")
      .removeClass("nav-links-down")
      .removeClass("display-none");
    navMid
      .removeClass("nav-mid-up")
      .removeClass("nav-mid-down")
      .removeClass("display-none");
  } else if (win.width() < 768) {
    navLinks.addClass("nav-links-up");
    navMid.addClass("nav-mid-up");
  }
});

$("#toggle-search-btn").on("click", function () {
  const searchForm = document.querySelector(".search-form");
  if (searchForm.classList.contains("hidden")) {
    searchForm.classList.remove("hidden");
    searchForm.classList.add("grid");
  } else {
    searchForm.classList.add("hidden");
    searchForm.classList.remove("grid");
  }
});
