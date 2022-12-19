<template>

    <div class="modal fade" id="settingsModal" tabindex="-1" aria-labelledby="settingsModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="settingsModalLabel">Settings</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="container-fluid">
                        <ErrorDataVue v-if="error">
                            {{ alertMessage }}
                        </ErrorDataVue>
                        <NoDataVue v-else-if="noData">
                            {{ alertMessage }}
                        </NoDataVue>
                        <SuccessDataVue v-else-if="successfulUpdate">
                            Update successful
                        </SuccessDataVue>
                        <div class="row mt-2 g-2 row-cols-auto">
                            <div class="input-group mb-3">
                                <span class="input-group-text" style="width: 150px;">Project Directory</span>
                                <input v-model="projectDir" type="text" class="form-control w-50"
                                    placeholder="Project directory..." aria-label="Project directory..."
                                    aria-describedby="button-addon2">
                                <SpinnerButton :key="projectDirReload" @request.once="updateProjectDir(projectDir)" />

                            </div>
                            <div class="input-group mb-3">
                                <span class="input-group-text" style="width: 150px;">Test Directory</span>
                                <input v-model="testsDir" type="text" class="form-control w-50"
                                    placeholder="Test directory..." aria-label="Test directory..."
                                    aria-describedby="button-addon2">
                                <SpinnerButton :key="testsDirReload" @request.once="updateTestsDir(testsDir)" />
                            </div>
                            <LoadingDataVue v-if="!dataLoaded && !error && !noData" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import { ref } from "vue";
import axios from "axios";
import store from "../store/index.js"
import SpinnerButton from "./SpinnerButton.vue";
import ErrorDataVue from "./ErrorData.vue";
import LoadingDataVue from "./LoadingData.vue";
import NoDataVue from "./NoData.vue";
import SuccessDataVue from "./SuccessData.vue"

export default {
    components: {
        SpinnerButton,
        ErrorDataVue,
        LoadingDataVue,
        NoDataVue,
        SuccessDataVue,
    },
    setup() {
        const projectDirReload = ref(0);
        const testsDirReload = ref(0);

        const forceRerender = (spinner) => {
            spinner.value += 1;
        };

        const data = ref([]);
        const dataLoaded = ref(null);
        const noData = ref(null);
        const error = ref(null);
        const projectDir = ref(null);
        const testsDir = ref(null);
        const alertMessage = ref(null);
        const successfulUpdate = ref(null);

        const getData = async () => {
            try {
                data.value = null;
                dataLoaded.value = null;
                noData.value = null;
                error.value = null;
                successfulUpdate.value = null;

                const response = await axios.get('/api/v1/settings/')
                data.value = response.data;
                if (data.value.length === 0) {
                    noData.value = true;
                    alertMessage.value = "Please update the directories below..."
                } else {
                    dataLoaded.value = true;

                    const project_dir = data.value.find(o => o.name === 'robot_dir').value;
                    projectDir.value = project_dir;
                    store.methods.setProjectDir(project_dir);

                    const tests_dir = data.value.find(o => o.name === 'tests_dir').value;
                    testsDir.value = tests_dir;
                    store.methods.setTestsDir(tests_dir);
                }
            } catch (e) {
                error.value = true;
                alertMessage.value = "Error while retrieving directories..."
                console.warn(e);
            }
        };

        const updateProjectDir = async (input) => {
            const directory = { name: 'robot_dir', value: input };
            try {
                error.value = null;
                successfulUpdate.value = null;

                await axios.post('/api/v1/settings/', directory);
                forceRerender(projectDirReload);
                successfulUpdate.value = true;
            } catch (e) {
                error.value = true;
                alertMessage.value = "Error while attempting to update Project Directory"
                projectDir.value = store.state.projectDir;
                forceRerender(projectDirReload);
                console.warn(e);
            }
        }

        const updateTestsDir = async (input) => {
            const directory = { name: 'tests_dir', value: input };
            try {
                error.value = null;
                successfulUpdate.value = null;

                await axios.post('/api/v1/settings/', directory);
                forceRerender(testsDirReload);
                successfulUpdate.value = true;
            } catch (e) {
                error.value = true;
                alertMessage.value = "Error while attempting to update Tests Directory"
                testsDir.value = store.state.testsDir;
                forceRerender(testsDirReload);
                console.warn(e);
            }
        }

        getData();

        return { projectDir, testsDir, dataLoaded, noData, error, successfulUpdate, alertMessage, updateProjectDir, updateTestsDir, projectDirReload, testsDirReload };
    },
}
</script>

<style>

</style>