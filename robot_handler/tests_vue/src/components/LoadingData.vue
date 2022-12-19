<template>

    <div class="position-absolute top-50 start-50 translate-middle">
        <div class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
            <span class="visually-hidden">
                <slot>Loading...</slot>
            </span>
        </div>
    </div>

</template>

<script>

export default {

}
</script>

<style>

</style>