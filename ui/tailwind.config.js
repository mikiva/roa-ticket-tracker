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
            },
            animation: {
                fade:  "fadeIn 200ms ease-out"
            },
            keyframes: {
                fadeIn: {
                    "0%": {opacity: 0, maxHeight: 0},
                    "100%": {opacity: 1, maxHeight: "2em"}
                }
            }

        },
    },
    plugins: [],
}