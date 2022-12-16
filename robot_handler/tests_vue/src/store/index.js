import { reactive } from "vue";

const state = reactive({
    projectDir: null,
    testsDir: null,
    testSuite: null,
});

const methods = {
    setProjectDir(payload) {
        state.projectDir = payload ? payload : null;
    },
    setTestsDir(payload) {
        state.testsDir = payload ? payload : null;
    },
}

export default {
    state,
    methods,
};