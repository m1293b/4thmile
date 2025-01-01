document.addEventListener("DOMContentLoaded", (event) => {
  const themeToggle = document.getElementById("theme-toggle");
  const body = document.body;
  const themeIcon = themeToggle.querySelector("i");

  // This variable will help to serve the static files regardless which app is being used. This was the best way I found today
  // to use the theme-switcher without having to change the code in every app.
  const baseUrl = `${window.location.origin}`;

  const favicon_boys = "/static/assets/img/favicon_boys.ico";
  const favicon_girls = "/static/assets/img/favicon_girls.ico";
  const blue_logo = "/static/assets/img/blue_logo.png";
  const pink_logo = "/static/assets/img/pink_logo.png";

  const logo = document.getElementsByClassName("logo")[0];

  const favIcon = document.querySelector("link[rel*='icon']");

  // Check for saved theme preference or default to 'boys'
  const currentTheme = localStorage.getItem("theme") || "boys";
  body.classList.add(`theme-${currentTheme}`);
  updateThemeIcon(currentTheme);

  themeToggle.addEventListener("click", () => {
    if (body.classList.contains("theme-boys")) {
      body.classList.replace("theme-boys", "theme-girls");
      localStorage.setItem("theme", "girls");
      updateThemeIcon("girls");
      updateFavicon("girls");
      updateLogo("girls");
    } else {
      body.classList.replace("theme-girls", "theme-boys");
      localStorage.setItem("theme", "boys");
      updateThemeIcon("boys");
      updateFavicon("boys");
      updateLogo("boys");
    }
  });

  function updateLogo(theme) {
    if (theme === "boys") {
      logo.src = `${baseUrl}${blue_logo}`;
    } else {
      logo.src = `${baseUrl}${pink_logo}`;
    }
  }

  function updateThemeIcon(theme) {
    if (theme === "boys") {
      themeIcon.className = "fas fa-mars";
    } else {
      themeIcon.className = "fas fa-venus";
    }
  }

  function updateFavicon(theme) {
    if (theme === "boys") {
      favIcon.href = `${baseUrl}${favicon_boys}`;
    } else {
      favIcon.href = `${baseUrl}${favicon_girls}`;
    }
  }
});
