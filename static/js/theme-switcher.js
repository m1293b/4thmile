console.log('Theme switcher loaded');
document.addEventListener('DOMContentLoaded', (event) => {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;
    const themeIcon = themeToggle.querySelector('i');

    console.log('Initial icon class:', themeIcon.className);

    // Check for saved theme preference or default to 'boys'
    const currentTheme = localStorage.getItem('theme') || 'boys';
    body.classList.add(`theme-${currentTheme}`);
    updateThemeIcon(currentTheme);

    themeToggle.addEventListener('click', () => {
        console.log('Theme toggle clicked');
        if (body.classList.contains('theme-boys')) {
            body.classList.replace('theme-boys', 'theme-girls');
            localStorage.setItem('theme', 'girls');
            updateThemeIcon('girls');
        } else {
            body.classList.replace('theme-girls', 'theme-boys');
            localStorage.setItem('theme', 'boys');
            updateThemeIcon('boys');
        }
        const logo = document.getElementById('logo');
        if (document.body.classList.contains('theme-boys')) {
            logo.src = "{% static 'assets/img/pink_logo.png' %}";
        } else {
            logo.src = "{% static 'assets/img/blue_logo.png' %}";
        }
    });

    function updateThemeIcon(theme) {
        console.log('Updating theme icon to:', theme);
        if (theme === 'boys') {
            themeIcon.className = 'fas fa-mars';
        } else {
            themeIcon.className = 'fas fa-venus';
        }
        console.log('Updated icon class:', themeIcon.className);
    }
    
});