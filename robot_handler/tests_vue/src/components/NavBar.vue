<template>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <router-link class="navbar-brand btn" :to="{ name: 'Home' }">
            <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" viewBox="0 0 512 512"><path fill="#00ff20" d="M379.93 366.463H135.625c-34.748 0-34.748-52.75 0-52.75H379.93c35.382 0 35.382 52.75 0 52.75zm9.818-167.79l-61.073 41.245c-28.96 19.574-58.422-24.016-29.462-43.59l61.073-41.246c29.087-19.659 58.549 23.93 29.462 43.59zM459.34 395.07c0 4.978-1.98 9.756-5.504 13.285l-45.392 45.392a18.813 18.813 0 0 1-13.29 5.504H116.847a18.813 18.813 0 0 1-13.29-5.504l-45.392-45.392a18.806 18.806 0 0 1-5.504-13.285V116.945a18.77 18.77 0 0 1 5.504-13.285l45.392-45.402a18.808 18.808 0 0 1 13.29-5.5h278.306c4.988 0 9.766 1.98 13.29 5.5l45.392 45.402a18.77 18.77 0 0 1 5.504 13.285V395.07zm38.633-321.78l-59.265-59.264A47.88 47.88 0 0 0 404.851.003H107.107a47.889 47.889 0 0 0-33.87 14.038l-59.22 59.256A47.885 47.885 0 0 0 0 107.152v297.701c0 12.7 5.046 24.89 14.028 33.86l59.257 59.258a47.89 47.89 0 0 0 33.863 14.026h297.708a47.88 47.88 0 0 0 33.856-14.023l59.26-59.26A47.867 47.867 0 0 0 512 404.854V107.157a47.894 47.894 0 0 0-14.028-33.867zM250.856 218.126c0 35.206-52.66 35.206-52.66 0c0-26.512-39.797-26.512-39.797 0c0 35.206-52.66 35.206-52.66 0c5.234-96.785 140.557-95.903 145.117 0z"/></svg>
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <router-link class="nav-link" :to="{ name: 'TestTags' }">Tags</router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" :to="{ name: 'TestSuites' }">Test Suites</router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" :to="{ name: 'TestCases' }">Test Cases</router-link>
                </li>
            </ul>
            <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <SettingsModal />
                    <a class="nav-link" @click="showHideModal" aria-current="page" href="#" data-bs-toggle="modal" data-bs-target="#settingsModal">
                        <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path fill="currentColor" d="M12 8a4 4 0 0 1 4 4a4 4 0 0 1-4 4a4 4 0 0 1-4-4a4 4 0 0 1 4-4m0 2a2 2 0 0 0-2 2a2 2 0 0 0 2 2a2 2 0 0 0 2-2a2 2 0 0 0-2-2m-2 12c-.25 0-.46-.18-.5-.42l-.37-2.65c-.63-.25-1.17-.59-1.69-.99l-2.49 1.01c-.22.08-.49 0-.61-.22l-2-3.46a.493.493 0 0 1 .12-.64l2.11-1.66L4.5 12l.07-1l-2.11-1.63a.493.493 0 0 1-.12-.64l2-3.46c.12-.22.39-.31.61-.22l2.49 1c.52-.39 1.06-.73 1.69-.98l.37-2.65c.04-.24.25-.42.5-.42h4c.25 0 .46.18.5.42l.37 2.65c.63.25 1.17.59 1.69.98l2.49-1c.22-.09.49 0 .61.22l2 3.46c.13.22.07.49-.12.64L19.43 11l.07 1l-.07 1l2.11 1.63c.19.15.25.42.12.64l-2 3.46c-.12.22-.39.31-.61.22l-2.49-1c-.52.39-1.06.73-1.69.98l-.37 2.65c-.04.24-.25.42-.5.42h-4m1.25-18l-.37 2.61c-1.2.25-2.26.89-3.03 1.78L5.44 7.35l-.75 1.3L6.8 10.2a5.55 5.55 0 0 0 0 3.6l-2.12 1.56l.75 1.3l2.43-1.04c.77.88 1.82 1.52 3.01 1.76l.37 2.62h1.52l.37-2.61c1.19-.25 2.24-.89 3.01-1.77l2.43 1.04l.75-1.3l-2.12-1.55c.4-1.17.4-2.44 0-3.61l2.11-1.55l-.75-1.3l-2.41 1.04a5.42 5.42 0 0 0-3.03-1.77L12.75 4h-1.5Z"/></svg>
                    </a>
                </li>
            </ul>
        </div>
    </div>
    </nav>

</template>

<script>
import { ref } from "vue";
import SettingsModal from './SettingsModal.vue';
import * as bootstrap from "bootstrap";

export default {
    components: {
        SettingsModal
    },
    setup() {
        // Create data/vars
        const show = ref(false);
        
        // Define showHideModal func
        const showHideModal = () => {
            let modal = bootstrap.Modal.getOrCreateInstance(document.getElementById('settingsModal')) // Returns a Bootstrap modal instance

            if (show.value) {
                modal.hide();
            } else {
                modal.show();
            }
        };

        return { showHideModal };
    },
}
</script>

<style>

</style>