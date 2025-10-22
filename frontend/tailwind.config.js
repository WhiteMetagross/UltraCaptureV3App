/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        purple: {
          500: '#8B5CF6',
          600: '#A78BFA',
        },
        blue: {
          500: '#3B82F6',
          600: '#60A5FA',
        },
        red: {
          500: '#EF4444',
          600: '#F87171',
        },
      },
    },
  },
  plugins: [],
}

