<template>

    <div class="modal fade" id="confirmationModal" tabindex="-1" aria-labelledby="confirmationModalLabel"
        aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="confirmationModalLabel">Confirmation</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="container-fluid">
                        <ErrorDataVue v-if="error">
                            {{ alertMessage }}
                        </ErrorDataVue>
                        <NoDataVue v-else-if="noData">
                            <span>No test suites or test cases were found.<br>Please double check the directories in your settings.</span>
                        </NoDataVue>
                        <SuccessDataVue v-else-if="successfulUpdate">
                            <span>Updated <strong>{{ testSuites }}</strong> test suites and <strong>{{ testCases }}</strong> test cases.</span>
                        </SuccessDataVue>
                        <p class="text-center">This will erase your current tests and rebuild them using your local filesystem.<br>
                            <strong>Are you sure you wish to proceed?</strong>
                        </p>
                        <div class="container text-center">
                            <div class="row">
                                <div class="col">
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                </div>
                                <div class="col">
                                    <SpinnerButton :key="confirmationReload" @request.once="updateTests" />
                                </div>
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
import axios from "axios";
import SpinnerButton from "./SpinnerButton.vue";
import ErrorDataVue from "./ErrorData.vue";
import NoDataVue from "./NoData.vue";
import SuccessDataVue from "./SuccessData.vue"

export default {
    components: {
        SpinnerButton,
        ErrorDataVue,
        NoDataVue,
        SuccessDataVue,
    },
    setup() {
        const confirmationReload = ref(0);

        const forceRerender = (spinner) => {
            spinner.value += 1;
        };

        const noData = ref(null);
        const error = ref(null);
        const successfulUpdate = ref(null);
        const alertMessage = ref(null);
        const testSuites = ref(null);
        const testCases = ref(null);

        const updateTests = async () => {
            try {
                noData.value = null;
                error.value = null;
                successfulUpdate.value = null;

                const response = await axios.post('/api/v1/update-tests/', null);
                testSuites.value = response.data.test_suites
                testCases.value = response.data.test_cases
                if (testSuites.value === 0 && testCases.value === 0) {
                    noData.value = true;
                    forceRerender(confirmationReload);
                } else {
                    successfulUpdate.value = true;
                    forceRerender(confirmationReload);
                }
            } catch (e) {
                error.value = true;
                alertMessage.value = "Error while attempting to update the tests"
                forceRerender(confirmationReload);
                console.warn(e);
            }
        }

        return { updateTests, alertMessage, noData, error, confirmationReload, successfulUpdate, testSuites, testCases };
    },
}
</script>

<style>

</style>