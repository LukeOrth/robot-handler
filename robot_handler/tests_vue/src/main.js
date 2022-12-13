import { createApp } from 'vue'
import App from './App.vue'
import router from './routers';
import axios from 'axios'
import VueGoodTablePlugin from 'vue-good-table-next';

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import 'vue-good-table-next/dist/vue-good-table-next.css'


axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)
app.use(router, axios, VueGoodTablePlugin)
app.mount('#app')
