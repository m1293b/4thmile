/** @type {import('tailwindcss').Config} */
/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

// @ts-ignore
const motion = require('tailwindcss-motion');

module.exports = {
  content: [
    '../../node_modules/**/*.{html,js,ts}',
    "../../static/**/*.{html,js,ts,css}",
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    '../../templates/**/*.{html,js,ts}',

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    '../../templates/**/*.html',

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    '../../**/templates/**/*.html',

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    // '!../../**/node_modules',
    /* JS 2: Process all JavaScript files in the project. */
    // '../../**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  theme: {
    extend: {
      colors: {
        danger: '#FF0000',
        success: '#4BB543',
        white: 'var(--white)',
        girls: {
          light: 'var(--girls-light)',
          dark: 'var(--girls-dark)',
        },
        boys: {
          light: 'var(--boys-light)',
          dark: 'var(--boys-dark)',
        },
        'theme-primary-light': 'var(--theme-primary-light)',
        'theme-primary-dark': 'var(--theme-primary-dark)',
        'theme-secondary-light': 'var(--theme-secondary-light)',
        'theme-secondary-dark': 'var(--theme-secondary-dark)',
      },
      container: {
        center: true,
        padding: '1rem',
      },
      screens: {
        'sm': '640px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
      },
    },
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
    motion,
  ],
}
