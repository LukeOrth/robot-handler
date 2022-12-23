import { reactive } from "vue";

const state = reactive({
    projectDir: null,
    testsDir: null,

    testCategories: null,
    testTags: null,
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
    setTestTags(payload) {
        state.testTags = payload ? payload : null;
    },
    setTestSuites(payload) {
        state.testSuites = payload ? payload : null;
    },
    setTestCases(payload) {
        state.testCases = payload ? payload : null;
    },

    getTestCase(id) {
        return state.testCases.find(tc => tc.id === id);
    },
    getTestSuite(id) {
        return state.testSuites.find(ts => ts.id === id);
    },
    getTestTag(id) {
        return state.testTags.find(tt => tt.id === id);
    },
}

export default {
    state,
    methods,
};