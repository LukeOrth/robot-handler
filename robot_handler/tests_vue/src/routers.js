import {createRouter, createWebHistory} from 'vue-router';
import TestsHome from './components/TestsHome';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: TestsHome,
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;