document.addEventListener("DOMContentLoaded", (event) => {
  const themeToggle = document.getElementById("theme-toggle");
  const body = document.body;
  const themeIcon = themeToggle.querySelector("i");

  const favicon_boys = STATIC_URLS.favicon_boys;
  const favicon_girls = STATIC_URLS.favicon_girls;
  const blue_logo = STATIC_URLS.blue_logo;
  const pink_logo = STATIC_URLS.pink_logo;

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
      logo.src = blue_logo;
    } else {
      logo.src = pink_logo;
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
      favIcon.href = favicon_boys;
    } else {
      favIcon.href = favicon_girls;
    }
  }
});
