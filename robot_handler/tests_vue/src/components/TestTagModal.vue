<template>

    <div class="modal fade" id="testTagModal" tabindex="-1" aria-labelledby="testTagModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-xl modal-dialog-scrollable">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="testTagModalLabel">{{ testTag.name }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="accordion">
                        <div v-for="test_category in testTag.test_categories" v-bind:key="test_category.name" class="accordion-item">
                            <h2 class="accordion-header">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                                    :data-bs-target="`#flush-${test_category.name.name}`" aria-expanded="false"
                                    :aria-controls="`flush-${test_category.name.name}`">
                                    {{ test_category.name.name }}
                                </button>
                            </h2>
                            <div :id="`flush-${test_category.id}`" class="accordion-collapse collapse show">
                                <div class="accordion-body">
                                    <ul v-for="test_suite in test_category.test_suites"
                                        v-bind:key="test_suite.id">
                                        <li>{{ test_suite.name }}</li>
                                        <!-- <ul v-for="test_case in test_suite.test_cases" v-bind:key="test_case.id">
                                            <li v-if="test_case.tags.findIndex(tag => tag.name === testTag.name) > -1">{{ test_case.name }}</li>
                                        </ul> -->
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
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
        ttID: String
    },
    setup(props) {
        const testTagId = ref(null)
        const testTag = ref({})

        watch(() => props.ttID, (newVal) => {
            testTagId.value = newVal

            if (testTagId.value) {
                testTag.value = store.methods.getTestTag(props.ttID)
                console.log(testTag.value)
            }
        })

        return { testTag };
    },
}
</script>

<style>

</style>