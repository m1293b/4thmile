document.addEventListener('DOMContentLoaded', (event) => {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;
    const themeIcon = themeToggle.querySelector('i');
    
    const logo = document.getElementsByClassName('logo')[0]; 
    
    const favIcon = document.querySelector("link[rel*='icon']");

    // Check for saved theme preference or default to 'boys'
    const currentTheme = localStorage.getItem('theme') || 'boys';
    body.classList.add(`theme-${currentTheme}`);
    updateThemeIcon(currentTheme);

    themeToggle.addEventListener('click', () => {
        if (body.classList.contains('theme-boys')) {
            body.classList.replace('theme-boys', 'theme-girls');
            localStorage.setItem('theme', 'girls');
            updateThemeIcon('girls');
            updateFavicon('girls');
            updateLogo('girls');
        } else {
            body.classList.replace('theme-girls', 'theme-boys');
            localStorage.setItem('theme', 'boys');
            updateThemeIcon('boys');
            updateFavicon('boys');
            updateLogo('boys');
        }
    });

    function updateLogo(theme) {
        if (theme === 'boys') {
            logo.src = 'static/assets/img/blue_logo.png';
        } else {
            logo.src = 'static/assets/img/pink_logo.png';
        }
    }

    function updateThemeIcon(theme) {
        if (theme === 'boys') {
            themeIcon.className = 'fas fa-mars';
        } else {
            themeIcon.className = 'fas fa-venus';
        }
    }

    function updateFavicon(theme) {
        if (theme === 'boys') {
            favIcon.href = "static/assets/img/favicon_boys.ico";
        } else {
            favIcon.href = "static/assets/img/favicon_girls.ico";
        }
    }
    
});

