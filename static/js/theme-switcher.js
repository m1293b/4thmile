document.addEventListener('DOMContentLoaded', (event) => {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Check for saved theme preference or default to 'boys'
    const currentTheme = localStorage.getItem('theme') || 'boys';
    body.classList.add(`theme-${currentTheme}`);

    themeToggle.addEventListener('click', () => {
        if (body.classList.contains('theme-boys')) {
            body.classList.replace('theme-boys', 'theme-girls');
            localStorage.setItem('theme', 'girls');
        } else {
            body.classList.replace('theme-girls', 'theme-boys');
            localStorage.setItem('theme', 'boys');
        }
    });
});