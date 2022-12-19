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
                    <ConfirmationModalVue />
                    <div class="dropdown">
                        <a class="nav-link" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            <svg xmlns="http://www.w3.org/2000/svg" width="2em" height="2em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 16 16"><path fill="currentColor" fill-rule="evenodd" d="M7.429 1.525a6.593 6.593 0 0 1 1.142 0c.036.003.108.036.137.146l.289 1.105c.147.56.55.967.997 1.189c.174.086.341.183.501.29c.417.278.97.423 1.53.27l1.102-.303c.11-.03.175.016.195.046c.219.31.41.641.573.989c.014.031.022.11-.059.19l-.815.806c-.411.406-.562.957-.53 1.456a4.588 4.588 0 0 1 0 .582c-.032.499.119 1.05.53 1.456l.815.806c.08.08.073.159.059.19a6.494 6.494 0 0 1-.573.99c-.02.029-.086.074-.195.045l-1.103-.303c-.559-.153-1.112-.008-1.529.27c-.16.107-.327.204-.5.29c-.449.222-.851.628-.998 1.189l-.289 1.105c-.029.11-.101.143-.137.146a6.613 6.613 0 0 1-1.142 0c-.036-.003-.108-.037-.137-.146l-.289-1.105c-.147-.56-.55-.967-.997-1.189a4.502 4.502 0 0 1-.501-.29c-.417-.278-.97-.423-1.53-.27l-1.102.303c-.11.03-.175-.016-.195-.046a6.492 6.492 0 0 1-.573-.989c-.014-.031-.022-.11.059-.19l.815-.806c.411-.406.562-.957.53-1.456a4.587 4.587 0 0 1 0-.582c.032-.499-.119-1.05-.53-1.456l-.815-.806c-.08-.08-.073-.159-.059-.19a6.44 6.44 0 0 1 .573-.99c.02-.029.086-.075.195-.045l1.103.303c.559.153 1.112.008 1.529-.27c.16-.107.327-.204.5-.29c.449-.222.851-.628.998-1.189l.289-1.105c.029-.11.101-.143.137-.146zM8 0c-.236 0-.47.01-.701.03c-.743.065-1.29.615-1.458 1.261l-.29 1.106c-.017.066-.078.158-.211.224a5.994 5.994 0 0 0-.668.386c-.123.082-.233.09-.3.071L3.27 2.776c-.644-.177-1.392.02-1.82.63a7.977 7.977 0 0 0-.704 1.217c-.315.675-.111 1.422.363 1.891l.815.806c.05.048.098.147.088.294a6.084 6.084 0 0 0 0 .772c.01.147-.038.246-.088.294l-.815.806c-.474.469-.678 1.216-.363 1.891c.2.428.436.835.704 1.218c.428.609 1.176.806 1.82.63l1.103-.303c.066-.019.176-.011.299.071c.213.143.436.272.668.386c.133.066.194.158.212.224l.289 1.106c.169.646.715 1.196 1.458 1.26a8.094 8.094 0 0 0 1.402 0c.743-.064 1.29-.614 1.458-1.26l.29-1.106c.017-.066.078-.158.211-.224a5.98 5.98 0 0 0 .668-.386c.123-.082.233-.09.3-.071l1.102.302c.644.177 1.392-.02 1.82-.63c.268-.382.505-.789.704-1.217c.315-.675.111-1.422-.364-1.891l-.814-.806c-.05-.048-.098-.147-.088-.294a6.1 6.1 0 0 0 0-.772c-.01-.147.039-.246.088-.294l.814-.806c.475-.469.679-1.216.364-1.891a7.992 7.992 0 0 0-.704-1.218c-.428-.609-1.176-.806-1.82-.63l-1.103.303c-.066.019-.176.011-.299-.071a5.991 5.991 0 0 0-.668-.386c-.133-.066-.194-.158-.212-.224L10.16 1.29C9.99.645 9.444.095 8.701.031A8.094 8.094 0 0 0 8 0zm1.5 8a1.5 1.5 0 1 1-3 0a1.5 1.5 0 0 1 3 0zM11 8a3 3 0 1 1-6 0a3 3 0 0 1 6 0z"/></svg>
                        </a>

                        <ul class="dropdown-menu dropdown-menu-end">
                            <li>
                                <a class="dropdown-item" @click="showHideModal('settingsModal')" aria-current="page" href="#" data-bs-toggle="modal" data-bs-target="#settingsModal">
                                    Update Directories
                                </a>
                            </li>
                            <li>
                                <div class="d-grid gap-2">
                                    <button type="button" class="btn btn-danger mx-1 mt-2 btn" @click="showHideModal('confirmationModal')">Update Tests</button>
                                </div>
                            </li>
                        </ul>
                    </div>
                </li>
            </ul>
        </div>
    </div>
    </nav>

</template>

<script>
import { ref } from "vue";
import SettingsModal from './SettingsModal.vue';
import ConfirmationModalVue from "./ConfirmationModal.vue";
import * as bootstrap from "bootstrap";

export default {
    components: {
        SettingsModal,
        ConfirmationModalVue,
    },
    setup() {
        // Create data/vars
        const show = ref(false);
        
        // Define showHideModal func
        const showHideModal = (id) => {
            let modal = bootstrap.Modal.getOrCreateInstance(document.getElementById(id)) // Returns a Bootstrap modal instance

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