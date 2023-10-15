import { createApp } from 'vue'
import './style.css'
import App from './App2.vue'
//import "@fontsource/source-code-pro/700.css";
import router from "@/router";
const app = createApp(App)

app.use(router)
app.mount('#app')
