<template>
  <button class="md:px-10 px-1 bg-black/80 border-black border-2 rounded" :class="{'!bg-black text-orange-500': active}"

  ><slot></slot>
  </button>
</template>

<script setup>
defineProps(["active"])
</script>

<style scoped>

</style>