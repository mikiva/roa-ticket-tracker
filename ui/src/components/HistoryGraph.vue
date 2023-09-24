<template>
  <div class="m-auto max-w-xl border-4 border-black bg-black/80 p-4 rounded-md z-10 relative">
    <h2 class="text-lg font-bold flex justify-between">
      <span>Försäljningen över tid</span>
    </h2>
    <template v-if="loading">
      <div class="flex items-center gap-4">

        <load-spinner></load-spinner>
        Hämtar...
      </div>
    </template>
    <template v-else>

      <div class="flex gap-2">
        <div class="basis-[33%]">Datum</div>
        <div class="flex-1">Sålda</div>
        <div class="flex-[4] text-right">
          Förändring
        </div>
      </div>


      <div v-for="item in event.sold" class="flex justify-between relative box-border gap-2">
        <span class="basis-[33%]">{{ item.date.substring(2) }}</span>
        <span class="flex-1"> {{ item.total }}</span>
        <span class="flex-[4] pr-1 box-border text-right relative">{{ item.inc >= 0 ? '+' : '' }}{{ item.inc }}
        <span
            class="absolute right-0 top-0 bottom-0 left-auto bg-red-900/70 h-[85%]  border-l border-y  border-amber-600/20 my-auto -z-10 rounded-l-2xl transition-all duration-200"
            :class="{'!bg-yellow-400/70' : item.inc === soldDaily[0], '!bg-slate-400/70': item.inc === soldDaily[1], '!bg-amber-600/70':  item.inc === soldDaily[2]}"
            :style="{ width: getSoldWidth(item.inc) }"></span>
        </span>
      </div>
    </template>
  </div>
</template>

<script setup>
import {ref, reactive, onMounted, computed} from 'vue';
import LoadSpinner from "./LoadSpinner.vue";
import ShowListItem from './ShowListItem.vue';

const url = "/api/shows/sold/history"

const loading = ref(false);
const event = reactive({sold: []})
const maxSold = ref(0);
const soldDaily = ref([])

onMounted(async () => {
  loading.value = true;
  const res = await fetch(url)
  const result = await res.json();
  event.sold = result;

  for (let i = 0; i < result.length - 1; i++) {
    const current = event.sold[i]
    const prev = event.sold[i + 1]
    current["inc"] = current.total - prev.total

  }

    soldDaily.value = result.map(r => r.inc || 0).sort((a,b) => {
      if (a > b) return -1;
      else if (a < b) return 1;
      return 0;
    })
    maxSold.value = Math.max(...result.map(r => r.inc || 0))
    loading.value = false;
})

function getSoldWidth(inc) {
  return (inc / maxSold.value) * 100 + "%"

}


</script>

<style scoped></style>