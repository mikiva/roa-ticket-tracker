<template>
  <div class="m-auto max-w-xl border-4 border-black bg-black/80 p-4 rounded-md z-10 relative">
    <h2 class="text-xl font-bold flex justify-between">
      <span>Historik</span>
      <button @click="showComparison = !showComparison">
        <div  class="px-1 flex gap-0.5 border rounded text-white text-sm items-center" :class="{'!text-black !bg-white': showComparison}">

          Jämför
        <Scale class=" w-6 h-6" :class="{'!text-black !bg-white': showComparison}"></Scale>
        </div>
      </button>
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


      <div v-for="item in eventSold" :key="item.date" v-if="eventSold.length > 0"
           class="flex-col flex relative border rounded border-slate-100/50 mb-2 p-2 ">
        <div
            class="flex justify-between relative box-border gap-2 flex-1">
          <div class="basis-[33%]">{{ item.datef }}</div>

          <span class="flex-shrink"> {{ item.total  }}</span>
          <div class="flex-1 pr-1 box-border text-right relative ">{{ item.inc >= 0 ? '+' : '' }}{{ item.inc }}
            <span
                class="absolute right-0 top-0 bottom-0 left-auto bg-red-900/70 h-[85%]  border-l border-y  border-amber-600/20 my-auto -z-10 rounded-l-2xl transition-all duration-200"
                :class="{'!bg-yellow-400/70' : item.inc === soldDaily[0], '!bg-slate-400/70': item.inc === soldDaily[1], '!bg-amber-600/70':  item.inc === soldDaily[2]}"
                :style="{ width: getSoldWidth(item.inc) }"></span>
          </div>
        </div>
        <template v-if="showComparison">

          <div
              class="flex justify-between relative max-h-full box-border gap-2 flex-1 italic text-slate-50/60 animate-fade text-sm">
            <div class="basis-[33%]">{{ item.datef }}-22</div>
            <div class="flex-shrink">{{ item.lastYear || '-' }}</div>
            <div class="flex-[4] pr-1 box-border text-right relative">{{
                item.lastYearInc >= 0 ? '+' : ''
              }}{{ item.lastYearInc }}
              <span
                  class="absolute right-0 top-0 bottom-0 left-auto bg-red-900/70 h-[55%]  border-l border-y  border-amber-600/20 my-auto -z-10 rounded-l-2xl transition-all duration-200"
                  :class="{'!bg-yellow-400/70' : item.lastYearInc === soldDaily[0], '!bg-slate-400/70': item.lastYearInc === soldDaily[1], '!bg-amber-600/70':  item.lastYearInc === soldDaily[2]}"
                  :style="{ width: getSoldWidth(item.lastYearInc) }"></span>
            </div>
          </div>
        </template>
      </div>
    </template>
  </div>
</template>


<script setup>
import {ref, reactive, computed, inject} from 'vue';
import {ScaleIcon as Scale} from "@heroicons/vue/24/outline";
import LoadSpinner from "./LoadSpinner.vue";


const event = reactive({sold: []})
const showComparison = ref(false);
const soldDaily = ref([])


const [result, loading] = inject("HISTORY", [])
const eventSold = computed(() => {
  event.sold = result.value;

  for (let i = 0; i < result.value.length; i++) {

    const current = event.sold[i]
    if (i < result.value.length) {
    const prev = event.sold[i + 1]
    current["inc"] = (current?.total - prev?.total) || 0
    current["lastYearInc"] = (current?.lastYear - prev?.lastYear) || 0
    }

    const date = current.date.split("-")
    current["datef"] = `${date[2]}/${date[1]}`

  }

  soldDaily.value = result.value.map(r => r.inc || 0).sort((a, b) => {
    if (a > b) return -1;
    else if (a < b) return 1;
    return 0;
  })
  return event.sold
})

const maxSold = computed(() => {
  if (showComparison.value)
    return Math.max(...result.value.map(r => Math.max(r.inc || 0, r.lastYearInc || 0) || 0))

  return Math.max(...result.value.map(r => r.inc || 0))
})

function getSoldWidth(inc) {
  return (inc / maxSold.value) * 100 + "%"

}


</script>

<style scoped></style>