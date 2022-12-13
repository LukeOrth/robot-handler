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
            <div v-else-if="noData" class="alert alert-warning d-flex align-items-center" role="alert">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2" viewBox="0 0 16 16" role="img" aria-label="Warning:">
                    <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                </svg>
                <div>
                    No Test Suites could be found...
                </div>
            </div>
            <div v-else-if="error" class="alert alert-danger d-flex align-items-center" role="alert">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2" viewBox="0 0 16 16" role="img" aria-label="Warning:">
                    <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                </svg>
                <div>
                    Error retrieving Test Suites...
                </div>
            </div>
            <div v-else class="position-absolute top-50 start-50 translate-middle">
                <div class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import { ref } from "vue";

export default {
    name: 'TestSuites',
    components: {
    },
    setup() {
        // Create data /vars
        const data = ref([]);
        const dataLoaded = ref(null);
        const noData = ref(null);
        const error = ref(null);
        const columns = ref(null);
        const tableData = ref(null);

        // Get data
        const getData = async() => {
            try {
                const response = await axios.get('/api/v1/test-suites/')
                data.value = response.data;
                if (data.value.length === 0) {
                    noData.value = true;
                } else {
                    dataLoaded.value = true;
                    //data.value.forEach(ts => console.log(ts.test_category.name))
                    buildTable(data.value);
                }
            } catch(e) {
                error.value = true;
                console.warn(e)
            }
        };

        // Run data function
        getData();

        const buildTable = () => {
            columns.value = [
                    {
                        field: 'test_category',
                        title: "Category",
                        key: "a",
                    },
                    {
                        field: 'name',
                        category: "Test Suite",
                        key: "b",
                    },
                ];
                

                tableData.value = [
                    { test_category:"John", name:"test" },
                    { test_category:"Jane", name:"test" },
                    { test_category:"Susan", name:"test" },
                    { test_category:"Chris", name:"test" },
                    { test_category:"Dan", name:"test" },
                    { test_category:"John", name:"test" },
                ];
        }

        return { data, dataLoaded, noData, error, columns, tableData };
    },
}
</script>

<style>

</style>