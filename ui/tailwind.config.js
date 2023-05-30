const defaultTheme = require("tailwindcss/defaultTheme")
/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx,vue}",
    ],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Source code pro', 'monospace', 'Consolas', ...defaultTheme.fontFamily.sans]
            }
        },
    },
    plugins: [],
}