<template>

    <div class="modal fade" id="testSuiteModal" tabindex="-1" aria-labelledby="testSuiteModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="testSuiteModalLabel">{{ testSuite.name }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <table class="table table-borderless">
                        <tbody>
                            <tr>
                                <th scope="row">Category</th>
                                <td>
                                    <p>{{ testCategory }}</p>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Documentation</th>
                                <td>
                                    <pre style="white-space: pre-wrap;">{{ testSuite.documentation }}</pre>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Test Cases</th>
                                <td>
                                    <ul class="list-group">
                                        <li v-for="test_case in testSuite.test_cases" v-bind:key="test_case.id"
                                            class="list-group-item clickable-list-item" data-bs-toggle="modal"
                                            data-bs-target="#testCaseModal" @click="updateTcId(test_case.id)">
                                            <div class="ms-2 me-auto">
                                                <div>{{ test_case.name }}</div>
                                                <small v-for="tag in test_case.tags" v-bind:key="tag"
                                                    class="float-start me-2 mt-2">
                                                    <span class="badge text-bg-warning">{{ tag.name }}</span>
                                                </small>
                                            </div>
                                        </li>
                                    </ul>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Tags</th>
                                <td>
                                    <p v-for="tag in testSuite.tags" v-bind:key="tag" class="float-start me-2">
                                        <span class="badge text-bg-primary">{{ tag.name }}</span>
                                    </p>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import { ref, watch } from 'vue';
import store from "../store/index.js"

export default {
    props: {
        tsID: Number
    },
    setup(props, { emit }) {
        const testSuiteId = ref(null)
        const testSuite = ref({})
        const testCategory = ref(null)

        watch(() => props.tsID, (newVal) => {
            testSuiteId.value = newVal

            if (testSuiteId.value) {
                testSuite.value = store.methods.getTestSuite(props.tsID)
                testCategory.value = testSuite.value.test_category.name;
            }
        })

        const updateTcId = (id) => {
            emit("updateTcId", id)
        }

        return { testSuite, testCategory, updateTcId };
    },
}
</script>

<style>

</style>