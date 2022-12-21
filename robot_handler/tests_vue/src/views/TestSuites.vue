<template>
    <div class="container-fluid px-0">
        <div class="row mt-2">
            <div class="col">

                <!-- Data -->
                <TestCaseModalVue :tcID="testCaseId" />
                <TestSuiteModalVue :tsID="testSuiteId" />

                <div v-if="dataLoaded" class="accordion accordion-flush" id="accordionFlushExample">

                    <div v-for="test_category in testCategories" v-bind:key="test_category.id" class="accordion-item">
                        <h2 class="accordion-header" id="flush-headingOne">
                            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                :data-bs-target="`#flush-${test_category.id}`" aria-expanded="false"
                                :aria-controls="`flush-${test_category.id}`">
                                {{ test_category.name }}
                            </button>
                        </h2>
                        <div :id="`flush-${test_category.id}`" class="accordion-collapse collapse show"
                            aria-labelledby="flush-headingOne">
                            <div class="accordion-body">
                                <div class="row row-cols-1 row-cols-md-3 g-4">
                                    <div v-for="test_suite in test_category.test_suites" v-bind:key="test_suite.id"
                                        class="col">
                                        <div class="card">
                                            <div @click="loadTestSuiteModal(test_suite.id)"
                                                class="card-header clickable-list-item" data-bs-toggle="modal"
                                                data-bs-target="#testSuiteModal">
                                                <span class="lh-lg">
                                                    {{ test_suite.name }}
                                                </span>
                                                <span class="actions hide">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                                        viewBox="0 0 24 24">
                                                        <path fill="#15be00" d="M8 19V5l11 7Z" />
                                                    </svg>
                                                </span>
                                            </div>
                                            <ul class="list-group list-group-flush">
                                                <li v-for="test_case in test_suite.test_cases" v-bind:key="test_case.id"
                                                    :id="test_case.id" @click="loadTestCaseModal(test_case.id)"
                                                    class="list-group-item clickable-list-item" data-bs-toggle="modal"
                                                    data-bs-target="#testCaseModal"
                                                    :data-bs-test-case="`${test_case.id}`">
                                                    <div style="width: 100%;" class="lh-lg float-start test-case-item">
                                                        {{ test_case.name }}</div>
                                                    <div class="actions hide float-start">
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                                            preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                                            <path fill="currentColor"
                                                                d="M18 12.998h-5v5a1 1 0 0 1-2 0v-5H6a1 1 0 0 1 0-2h5v-5a1 1 0 0 1 2 0v5h5a1 1 0 0 1 0 2z" />
                                                        </svg>
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em"
                                                            preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                                            <path fill="currentColor"
                                                                d="M9.525 18.025q-.5.325-1.013.037Q8 17.775 8 17.175V6.825q0-.6.512-.888q.513-.287 1.013.038l8.15 5.175q.45.3.45.85t-.45.85Z" />
                                                        </svg>
                                                    </div>
                                                    <p v-for="tag in test_case.tags" v-bind:key="tag"
                                                        class="float-start me-2 mb-1">
                                                        <span class="badge text-bg-warning">{{ tag.name }}</span>
                                                    </p>
                                                </li>
                                            </ul>
                                            <div class="card-footer">
                                                <small v-for="tag in test_suite.tags" v-bind:key="tag"
                                                    class="float-end me-2">
                                                    <span class="badge text-bg-primary">{{ tag.name }}</span>
                                                </small>
                                                <small class="float-end me-2">Tags: </small>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- No Data -->
                <NoDataVue v-else-if="noData">
                    No Test Suites could be found...
                </NoDataVue>
                <ErrorDataVue v-else-if="error">
                    Error retrieving Test Suites...
                </ErrorDataVue>
                <LoadingDataVue v-else />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { ref } from "vue";
import NoDataVue from '@/components/NoData.vue';
import LoadingDataVue from '@/components/LoadingData.vue';
import ErrorDataVue from '@/components/ErrorData.vue';
import TestCaseModalVue from '@/components/TestCaseModal.vue';
import TestSuiteModalVue from '@/components/TestSuiteModal.vue';
import store from "../store/index.js"

export default {
    name: 'TestSuites',
    components: {
        LoadingDataVue,
        NoDataVue,
        ErrorDataVue,
        TestCaseModalVue,
        TestSuiteModalVue,
    },
    setup() {
        // Create data/vars
        const dataLoaded = ref(null);
        const noData = ref(null);
        const error = ref(null);

        const testCategories = ref([]);
        const testSuites = ref([]);
        const testCases = ref([]);

        // Get data
        const getData = async () => {
            try {
                const response = await axios.get('/api/v1/test-suites/')
                if (response.data.length === 0) {
                    noData.value = true;
                } else {
                    dataLoaded.value = true;

                    response.data.forEach(test_suite => {
                        const index = testCategories.value.findIndex(cat => cat.name == test_suite.test_category.name);
                        if (index === -1) {
                            testCategories.value.push(
                                {
                                    id: test_suite.test_category.name.replace(/\s+/g, '-').toLowerCase(),
                                    name: test_suite.test_category.name,
                                    test_suites: [test_suite]
                                }
                            );
                        } else {
                            testCategories.value[index].test_suites.push(test_suite);
                        }
                        testSuites.value.push(test_suite);
                        test_suite.test_cases.forEach(test_case => testCases.value.push(test_case))
                    });
                    store.methods.setTestCategories(testCategories);
                    store.methods.setTestSuites(testSuites);
                    store.methods.setTestCases(testCases);
                }
            } catch (e) {
                error.value = true;
                console.warn(e)
            }
        };

        // Run data function
        getData();

        const testCaseId = ref(null)
        const testSuiteId = ref(null)

        const loadTestCaseModal = (id) => {
            testCaseId.value = id;
        };

        const loadTestSuiteModal = (id) => {
            testSuiteId.value = id;
        };

        return { dataLoaded, testCaseId, testSuiteId, loadTestCaseModal, loadTestSuiteModal, noData, error, testCategories, testSuites, testCases };
    },
}
</script>

<style>

</style>