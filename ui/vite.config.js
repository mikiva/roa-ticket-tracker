import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import {fileURLToPath, URL} from "url";
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: [
      {find: '@', replacement: fileURLToPath(new URL('./src', import.meta.url))}
    ],
  },
  server: {
    port: 8000,
    proxy: {
      //"^/api": "https://roa.miiv.se",
      "^/api": "http://localhost:8080",
      "^/ext/": "https://roa.miiv.se"
    }
  }
})
