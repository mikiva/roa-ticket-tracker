<template>
  <div class="m-auto max-w-xl border-4 border-black bg-black/80 p-4 rounded-md z-10 relative">
    <h2 class="text-lg font-bold">Försäljningen över tid</h2>
    <template v-if="loading">
      <div class="flex items-center gap-4">

        <load-spinner></load-spinner>
        Hämtar...
      </div>
    </template>
    <template v-else>
      <show-list-item :show="{ startDate: 'Datum', 'sold': 'Sålda', 'today': 'Förändring' }"></show-list-item>
      <div v-for="item in event.sold" class="flex justify-between">
        <span class="flex-[2]">{{ item.date }}</span> <span class="flex-1"> {{ item.total }}</span> <span
          class="flex-1 text-right"> {{ item.inc >= 0 ? '+' : '' }}{{ item.inc }}</span>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue';
import LoadSpinner from "./LoadSpinner.vue";
import ShowListItem from './ShowListItem.vue';
const url = "/api/shows/sold/history"

const loading = ref(false);
const event = reactive({ sold: [] })


onMounted(async () => {
  loading.value = true;
  const res = await fetch(url)
  const result = await res.json();
  event.sold = result;

  for (let i = 0; i < result.length-1; i++) {
    const current = event.sold[i]
    const prev = event.sold[i + 1]
    current["inc"] = current.total - prev.total
  }

  loading.value = false;
})


</script>

<style scoped></style>