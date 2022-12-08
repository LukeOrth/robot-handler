<template>
  <div id="app">
    <TestsNavbar/>
    <router-view/>
  </div>
</template>

<script>
import TestsNavbar from './components/TestsNavbar.vue'

export default {
  name: 'App',
  components: {
    TestsNavbar
  }
}
</script>

<style>

</style>
