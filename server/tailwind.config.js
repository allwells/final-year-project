/** @type {import('tailwindcss').Config} */
const colors = require("tailwindcss/colors");
const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  content: ["./app/templates/**/*.html"],
  theme: {
    screens: {
      xs: "475px",
      ...defaultTheme.screens,
    },
    colors: {
      primary: "#FF4B4B",
      ...colors,
    },
    extend: {},
  },
  plugins: [],
};
