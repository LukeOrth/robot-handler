<template>
<div class="container-fluid px-0">
    <div class="row mt-2">
        <div class="col">

            <!-- Data -->

            <table v-if="dataLoaded" summary="test_suites" class="table text-center table-striped table-hover table-sm searchable-table">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">
                            <input type="text" class="bg-dark border-0 text-light search-column" placeholder="Test Suite">
                        </th>
                        <th scope="col">
                            <input type="text" class="bg-dark border-0 text-light search-column" placeholder="Documentation">
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr 
                        v-for="test_suite in data" 
                        v-bind:key="test_suite.id"
                    >
                        <td class="dropdown">{{ test_suite.name }}</td>
                    </tr>
                </tbody>
            </table>

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

export default {
    name: 'TestSuites',
    components: {
        LoadingDataVue,
        NoDataVue,
        ErrorDataVue,
    },
    setup() {
        // Create data/vars
        const data = ref([]);
        const dataLoaded = ref(null);
        const noData = ref(null);
        const error = ref(null);

        // Get data
        const getData = async() => {
            try {
                const response = await axios.get('/api/v1/test-suites/')
                data.value = response.data;
                if (data.value.length === 0) {
                    noData.value = true;
                } else {
                    dataLoaded.value = true;
                }
            } catch(e) {
                error.value = true;
                console.warn(e)
            }
        };

        // Run data function
        getData();

        return { data, dataLoaded, noData, error };
    },
}
</script>

<style>

</style>