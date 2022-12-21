<template>

    <div class="modal fade" id="testCaseModal" tabindex="-1" aria-labelledby="testCaseModalLabel"
        aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="testCaseModalLabel">{{ testCase.name }}</h1>
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
                                <td><pre style="white-space: pre-wrap;">{{ testCase.documentation }}</pre></td>
                            </tr>
                            <tr>
                                <th scope="row">Included In</th>
                                <td>
                                    <ul class="list-group">
                                        <li class="list-group-item">
                                            <div class="ms-2 me-auto">
                                                <div>{{ testSuiteName }}</div>
                                                <small v-for="tag in testSuiteTags" v-bind:key="tag"
                                                    class="float-start me-2 mt-2">
                                                    <span class="badge text-bg-primary">{{ tag.name }}</span>
                                                </small>
                                            </div>
                                        </li>
                                    </ul>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row">Tags</th>
                                <td>
                                    <p v-for="tag in testCase.tags" v-bind:key="tag" class="float-start me-2">
                                        <span class="badge text-bg-warning">{{ tag.name }}</span>
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
        tcID: Number
    },
    setup(props) {
        const testCaseId = ref(null)
        const testCase = ref({})
        const testCategory = ref(null)
        const testSuiteName = ref(null)
        const testSuiteTags = ref(null)

        watch(() => props.tcID, (newVal) => {
            testCaseId.value = newVal

            if (testCaseId.value) {
                testCase.value = store.methods.getTestCase(props.tcID)

                const { name, test_category, tags } = store.methods.getTestSuite(testCase.value.test_suite)
                testCategory.value = test_category.name
                testSuiteName.value = name
                testSuiteTags.value = tags
            }
        })

        return { testCase, testCategory, testSuiteName, testSuiteTags };
    },
}
</script>

<style>

</style>