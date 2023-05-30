<template>
    <div class="flex">
        <div class="flex-[2]">{{ show.startDate }}</div>
        <div class="flex-1">{{ show.sold }}</div>
        <div class="flex-1 text-right">{{ show.today }}</div>
    </div>
</template>

<script setup>
const props = defineProps(["show"])

const { show } = props;


</script>

<style scoped></style>