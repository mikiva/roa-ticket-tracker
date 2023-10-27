<script setup>
import {ref, provide, onBeforeMount, onMounted, computed} from "vue";
import CountdownTimer from "../components/CountdownTimer.vue";
import ShowList from "../components/ShowList.vue";
import HistoryGraph from "../components/HistoryGraph.vue";
import roa from "../assets/roa.png"
import splash from "../assets/roa_color_splash.png"
import ExternalMedia from "@/components/ExternalMedia.vue";
import TabButton from "@/components/TabButton.vue";
import {useRoute} from "vue-router";

const todayIs = ref(new Date());

const targetDate = ref([new Date().getTime(), "note"]);
const showsLoading = ref(false)
const showsSold = ref([]);
const historyLoading = ref(false)
const historySold = ref([]);
const externalArticlesLoading = ref(false)
const externalArticles = ref([])
const [MAIN, HISTORY, ARTICLES] = ["", "#history", "#articles"]

const view = ref(MAIN)

const route = useRoute()
provide("SHOWS", [showsSold, showsLoading])
provide("HISTORY", [historySold, historyLoading])
provide("EXTERNAL_ARTICLES", [externalArticles, externalArticlesLoading])
onMounted(() => {
  if ([MAIN, HISTORY, ARTICLES].includes(route.hash)) {
    view.value = route.hash;
  }
  showsLoading.value = true
  historyLoading.value = true
  externalArticlesLoading.value = true;
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
  fetch("/ext/articles.json").then(res => res.json()).then(result => {
    externalArticles.value = result
  }).finally(() => {
    externalArticlesLoading.value = false;
  })

})

function setView(v) {
  window.location.hash = v
  view.value = v
}

function refresh() {
  targetDate.value = getNextShowTime();
  todayIs.value = new Date()
}

const todayProvider = computed(() => {
  const d = todayIs.value
  //d.setDate(d.getDate() +1)
  //d.setSeconds(d.getSeconds() + 2)
  //d.setMinutes(d.getMinutes() + 68)
  //d.setHours(d.getHours() + 14)
  //console.log(d)
  return d.getTime()
})

onBeforeMount(() => {
  refresh()
  provide("TODAY",  todayProvider)
  provide("NEXT_SHOW", targetDate)
})


const shows = {
  "2023-10-14T15:00:00": "Premiär 14 oktober",
  "2023-10-21T15:00:00": "Nästa Premiär 21 oktober",
  "2023-10-28T15:00:00": "Nästa Premiär 28 oktober",
  "2023-11-04T15:00:00": "Nästa Premiär 4 november",
  "2023-11-11T15:00:00": "Nästa Premiär 11 nobember",
  "2023-11-18T15:00:00": "Nästa Premiär 18 november",
  "2023-11-25T15:00:00": "Nästa Premiär 25 november",
  "2023-12-02T15:00:00": "Sista Premiären 2 december",
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
    if (d >= todayProvider.value + 1000) {
      return current
    }
  }
  return [-1, "Rock of Ages"]
}

function ticked() {
    refresh()

}

</script>

<template>
  <div class="bg-black w-full min-h-full relative bg-gradient-to-b from-black from-70%  to-red-500/10 text-white p-3">
    <div class="relative m-auto max-w-xl blur-sm">
      <img :src="splash" alt="" class="absolute animate-pulse">
      <img :src="roa" alt="" class="absolute left-[50%] -translate-x-[50%]">
    </div>
    <div class="flex flex-col gap-7 " :key="targetDate[0]">
      <countdown-timer class="w-full"  @tick="ticked"/>
      <div class="flex m-auto  my-[-15px] z-10 md:gap-3 gap-1 flex-wrap">
        <tab-button :active="view ===MAIN" @click="setView(MAIN)">Idag</tab-button>
        <tab-button :active="view ===HISTORY" @click="setView(HISTORY)">Historik</tab-button>
        <tab-button :active="view ===ARTICLES" @click="setView(ARTICLES)">Artiklar</tab-button>

      </div>
      <show-list class="w-full" v-show="view === MAIN"/>
      <history-graph class="w-full overflow-hidden" v-show="view === HISTORY"></history-graph>
      <external-media v-show="view===ARTICLES"></external-media>

    </div>

  </div>
</template>

