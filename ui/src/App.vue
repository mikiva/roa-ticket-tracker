<script setup>
import {ref, provide, onBeforeMount, onMounted} from "vue";
import CountdownTimer from "./components/CountdownTimer.vue";
import ShowList from "./components/ShowList.vue";
import HistoryGraph from "./components/HistoryGraph.vue";
import roa from "./assets/roa.png"
import splash from "./assets/roa_color_splash.png"

const todayIs = ref(new Date());

const targetDate = ref([new Date().getTime(), "note"]);
const showsLoading = ref(false)
const showsSold = ref([]);
const historyLoading = ref(false)
const historySold = ref([]);


provide("SHOWS", [showsSold, showsLoading])
provide("HISTORY", [historySold, historyLoading])
onMounted(() => {
  showsLoading.value = true
  historyLoading.value = true
  fetch("/api/shows/sold/today").then(res => res.json()).then(result => {
    showsSold.value = result
  }).finally(() => {
    showsLoading.value = false
  })
  fetch("/api/shows/sold/history").then(res => res.json()).then(result => {
    historySold.value = result
  }).finally(() => {

    historyLoading.value = false
  })


})


onBeforeMount(() => {

  targetDate.value = getNextShowTime();
  provide("TODAY", todayIs.value.getTime())
  provide("NEXT_SHOW", targetDate.value)
})


const shows = {
  "2023-10-14T15:00:00": "Premiär 14 oktober",
  "2023-10-21T15:00:00": "Nästa Premiär 21 oktober",
  "2023-10-28T15:00:00": "Nästa Premiär 28 oktober",
  "2023-11-04T15:00:00": "Nästa Premiär 4 november",
  "2023-11-11T15:00:00": "Nästa Premiär 11 nobember",
  "2023-11-18T15:00:00": "Nästa Premiär 18 november",
  "2023-11-25T15:00:00": "Sista Premiären 25 november",
}

/**
 * For testing purposes. Not connected to "today" in countdown timer.
 * @param days how many days to progress
 * @private
 */
function _moveToday(days = 0) {
  const d = todayIs.value.getDate() + days
  todayIs.value.setDate(d)

}

function getNextShowTime() {
  let current;
  for (const [date, v] of Object.entries(shows)) {
    const d = new Date(date).getTime()
    current = [d, v];
    if (d >= todayIs.value.getTime()) {
      return current
    }
  }
  return current
}


const view = ref("main")
</script>

<template>
  <div class="bg-black w-full min-h-full relative bg-gradient-to-b from-black from-70%  to-red-500/10 text-white p-3">
    <div class="relative m-auto max-w-xl blur-sm">
      <img :src="splash" alt="" class="absolute animate-pulse">
      <img :src="roa" alt="" class="absolute left-[50%] -translate-x-[50%]">
    </div>
    <div class="flex flex-col gap-7 ">
      <countdown-timer class="w-full" :key="targetDate"/>
      <div class="m-auto  my-[-15px] z-10 border-black border-2 bg-black/80">
        <button class="px-10  border-black rounded" @click="view = 'main'"
                v-show="view !== 'main'">Tillbaka
        </button>
        <button class="px-10 border-black rounded" @click="view = 'history'" v-show="view !== 'history'">Visa
          försäljning över tid
        </button>
      </div>
      <show-list class="w-full" v-show="view === 'main'"/>
      <history-graph class="w-full overflow-hidden" v-show="view === 'history'"></history-graph>
    </div>

  </div>
</template>

