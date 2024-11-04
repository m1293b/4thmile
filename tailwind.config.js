/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./**/templates/**/*.{html,js}", "./**/assets/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [require('@tailwindcss/typography'), require('tailwindcss-motion')],
}

