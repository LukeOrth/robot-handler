import {createRouter, createWebHistory} from 'vue-router';
import TestSuites from './views/TestSuites';
import TestCases from './views/TestCases';
import TestTags from './views/TestTags';

const routes = [
    {
        path: "/",
        name: "Home",
        component: TestSuites,
    },
    {
        path: "/tags",
        name: "TestTags",
        component: TestTags,
    },
    {
        path: "/test-suites",
        name: "TestSuites",
        component: TestSuites,
    },
    {
        path: "/test-cases",
        name: "TestCases",
        component: TestCases,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;