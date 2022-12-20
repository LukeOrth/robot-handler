import { reactive } from "vue";

const state = reactive({
    projectDir: null,
    testsDir: null,

    testCategories: null,
    testSuites: null,
    testCases: null,
});

const methods = {
    setProjectDir(payload) {
        state.projectDir = payload ? payload : null;
    },
    setTestsDir(payload) {
        state.testsDir = payload ? payload : null;
    },

    setTestCategories(payload) {
        state.testCategories = payload ? payload : null;
    },
    setTestSuites(payload) {
        state.testCategories = payload ? payload : null;
    },
    setTestCases(payload) {
        state.testCategories = payload ? payload : null;
    },
}

export default {
    state,
    methods,
};