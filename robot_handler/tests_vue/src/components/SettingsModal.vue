<template>

    <div class="modal fade" id="settingsModal" tabindex="-1" aria-labelledby="settingsModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                <h1 class="modal-title fs-5" id="settingsModalLabel">Settings</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="container-fluid">
                        <div class="row mt-2 g-2 row-cols-auto">
                            <div class="input-group mb-3">
                                <span class="input-group-text" style="width: 150px;">Project Directory</span>
                                <input type="text" class="form-control" placeholder="Project directory..." aria-label="Project directory..." aria-describedby="button-addon2" value="{{ robot_dir.value }}">
                                <button 
                                    @click="toggle" 
                                    :class="[!hideLoading ? 'd-none' : '']"
                                    type="submit" class="btn btn-outline-primary w-25" id="update_project_dir"
                                    >Update
                                </button>
                            </div>
                            <div class="input-group mb-3">
                                <span class="input-group-text" style="width: 150px;">Test Directory</span>
                                <input type="text" class="form-control" placeholder="Test directory..." aria-label="Test directory..." aria-describedby="button-addon2" value="{{ robot_dir.value }}">
                                <button 
                                    @click="toggle" 
                                    :class="[!hideLoading ? 'd-none' : '']"
                                    type="submit" class="btn btn-outline-primary w-25" id="update_tests_dir"
                                    >Update
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <form>
                        <button 
                            @click="toggle" 
                            :class="[!hideLoading ? 'd-none' : '']"
                            type="submit" class="btn btn-primary" id="refresh_tests"
                            >Refresh Tests
                        </button>
                        <button 
                            @click="toggle" 
                            :class="[hideLoading ? 'd-none' : '']" 
                            class="btn btn-primary" type="button" id="loading_tests" disabled
                            >
                            <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                            <span> Loading...</span>
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import { ref } from "vue";

export default {
    components: {

    },
    setup() {
        // Create data/vars
        const hideLoading = ref(true);
        
        // Define toggle func
        const toggle = () => {
            hideLoading.value = !hideLoading.value;
        };

        return { toggle, hideLoading };
    },
}
</script>

<style>

</style>