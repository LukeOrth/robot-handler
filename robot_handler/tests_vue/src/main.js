import { createApp } from 'vue'
import App from './App.vue'
import router from './routers';
import axios from 'axios'
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

// Import Bootstrap and BootstrapVue CSS files (order is important)
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)
app.use(router, axios, BootstrapVue, IconsPlugin)
app.mount('#app')
