<template>
<div class="container-fluid px-0">
    <div class="row mt-2">
        <div class="col">
            <table summary="test_suites" class="table text-center table-striped table-hover table-sm searchable-table">
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
                        v-for="test_suite in testSuites" 
                        v-bind:key="test_suite.id"
                    >
                        <td class="dropdown">{{ test_suite.name }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
//import { VueGoodTable } from 'vue-good-table-next';

export default {
    name: 'TestSuites',
    data() {
        return {
            testSuites: []
        }
    },
    components: {
    },
    mounted() {
        this.getTestSuites()
    },
    methods: {
        getTestSuites() {
            axios
                .get('/api/v1/test-suites/')
                .then(response => {
                    this.testSuites = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>

<style>

</style>