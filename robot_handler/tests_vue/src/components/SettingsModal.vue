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
                        <div class="row mt-2 g-2 row-cols-auto">
                            <div class="input-group mb-3">
                                <span class="input-group-text" style="width: 150px;">Project Directory</span>
                                <input v-model="projectDir" type="text" class="form-control w-50" placeholder="Project directory..." aria-label="Project directory..." aria-describedby="button-addon2">
                                <SpinnerButton :key="projectDirReload" @request.once="updateProjectDir(projectDir)" />

                            </div>
                            <div class="input-group mb-3">
                                <span class="input-group-text" style="width: 150px;">Test Directory</span>
                                <input v-model="testsDir" type="text" class="form-control w-50" placeholder="Test directory..." aria-label="Test directory..." aria-describedby="button-addon2">
                                <SpinnerButton :key="testsDirReload" @request.once="updateTestsDir(testsDir)" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import { ref } from "vue";
import SpinnerButton from "./SpinnerButton.vue";
import store from "../store/index";

export default {
    components: {
        SpinnerButton,
    },
    setup() {
        const projectDir = ref(store.state.projectDir);
        const testsDir = ref(store.state.testsDir);
        const projectDirReload = ref(0);
        const testsDirReload = ref(0);

        const forceRerender = (spinner) => {
            spinner.value += 1;
        };

        const delay = ms => new Promise(res => setTimeout(res, ms));

        const updateProjectDir = async(input) => {
            console.log(input)
            store.methods.setProjectDir(input)
            await delay(5000);
            forceRerender(projectDirReload);
        }

        const updateTestsDir = async(input) => {
            console.log(input)
            store.methods.setTestsDir(input)
            await delay(5000);
            forceRerender(testsDirReload);
        }

        return { projectDir, testsDir, updateProjectDir, updateTestsDir, projectDirReload, testsDirReload };
    },
}
</script>

<style>

</style>