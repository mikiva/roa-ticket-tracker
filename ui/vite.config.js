import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 8000,
    proxy: {
      "^/api": "https://roa.miiv.se"
      //"^/api": "http://localhost:8080"
    }
  }
})
