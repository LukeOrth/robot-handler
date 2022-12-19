<template>
    <button 
        @click="toggle(); $emit('request');" 
        :class="[!hideLoading ? 'd-none' : '']"
        type="submit" class="btn btn-outline-primary"
        >
        <slot>Update</slot>
    </button>
    <button
        :class="[hideLoading ? 'd-none' : '']" 
        type="submit" class="btn btn-outline-primary" disabled
        >
        <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
        <span> Loading...</span>
    </button>

</template>

<script>
import { ref } from "vue";

export default {
    emits: ['request'],
    setup() {
        // Create data/vars
        const hideLoading = ref(true);
        
        // Define toggle func
        const toggle = () => {
            hideLoading.value = !hideLoading.value;
            return hideLoading.value
        };

        return { toggle, hideLoading };
    },
}
</script>

<style>

</style>