<template>
  <div id="app">
    <NavBar />
    <router-view />
  </div>
</template>

<script>
import axios from 'axios';
import NavBar from './components/NavBar.vue';
import { ref } from "vue";

export default {
  name: 'App',
  components: {
    NavBar
  },
  setup() {
    // Create data /vars
    const appReady = ref(null);
    const data = ref([]);
    const dataLoaded = ref(null);
    const noData = ref(null);
    const error = ref(null);

    // Get data
    const getData = async () => {
      try {
        const response = await axios.get('/api/v1/test-suites/')
        data.value = response.data;
        if (data.value.length === 0) {
          noData.value = true;
        } else {
          alert('hi mom')
          dataLoaded.value = true;
          //data.value.forEach(ts => console.log(ts.test_category.name))
        }
      } catch (e) {
        error.value = true;
        console.warn(e)
      }
    };

    return { appReady, getData };
  },
}
</script>

<style>

</style>
