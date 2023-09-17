<template>
  <div class="flex" :title="show.id">
    <div class="flex-[2]">{{ startDate }}</div>
    <div class="flex-1">{{ show.sold }}</div>
    <div class="flex-1 text-right">{{ show.today }}</div>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps(["show"])

const { show } = props;

const months = {
  10: "oktober",
  11: "november",
  12: "decemer"
}

const startDate = computed(() => {
  const reg = /^(\d{4})-(\d{2})-(\d{2}).*/
  const parts = show.startDate.match(reg)
  if (parts) {
    return `${parts[3]} ${months[parts[2]]}`
  }

  return show.startDate
});

</script>

<style scoped></style>