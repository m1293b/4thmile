/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./**/templates/**/*.{html,js,ts}", "./**/assets/**/*.{html,js,ts}"],
  theme: {
    extend: {},
  },
  plugins: [require('@tailwindcss/typography'), require('tailwindcss-motion')],
}
