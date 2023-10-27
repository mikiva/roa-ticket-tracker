<template>
  <div class="flex-col mb-2 p-1.5 border rounded " :title="show.id" :class="{'opacity-[0.5]': isPlayed}">
    <div class="flex gap-2">
      <div class="basis-[50%]">{{ startDate }}</div>
      <div class="flex-1">{{ show.sold }}</div>
      <div class="flex-[4] text-right">{{ show.today }}</div>
    </div>
    <div class="flex italic gap-2 text-sm" v-if="compare">
      <div class="basis-[50%]">2022</div>
      <div class="flex-1">{{ show.compare.sold }}</div>
      <div class="flex-[4] text-right">{{ show.compare.today }}</div>
    </div>

  </div>
</template>

<script setup>
import {computed, inject} from "vue";

const props = defineProps(["show", "isHeader", "compare"])

const {show} = props;
const todayIs = inject("TODAY")

const months = {
  10: "oktober",
  11: "november",
  12: "decemer"
}

const isPlayed = computed(() => {
  const reg = /^(\d{4})-(\d{2})-(\d{2}).*/
  if (!show.startDate.match(reg)) return;
  const start = show.startDate;
  const startDate = new Date(start).getTime();

  return startDate <= todayIs.value


})


const startDate = computed(() => {
  const reg = /^(\d{4})-(\d{2})-(\d{2}).*/
  const parts = show.startDate.match(reg)
  if (parts) {
    return `${parts[3]} ${months[parts[2]]}`
  }

  return show.startDate
});

</script>

<style scoped>


</style>