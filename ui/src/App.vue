<script setup>
import { ref } from "vue";
import CountdownTimer from "./components/CountdownTimer.vue";
import ShowList from "./components/ShowList.vue";
import HistoryGraph from "./components/HistoryGraph.vue";
import roa from "./assets/roa.png"
import splash from "./assets/roa_color_splash.png"


const view = ref("main")
</script>

<template>
    <div class="bg-black w-full min-h-full relative bg-gradient-to-b from-black from-70%  to-red-500/10 text-white p-3">
        <div class="relative m-auto max-w-xl blur-sm">
            <img :src="splash" alt="" class="absolute animate-pulse">
            <img :src="roa" alt="" class="absolute left-[50%] -translate-x-[50%]">
        </div>
        <div class="flex flex-col gap-7 ">
            <countdown-timer class="w-full" />
            <div class="m-auto  my-[-15px] z-10 border-black border-2 bg-black/80">
                <button class="px-10  border-black rounded" @click="view = 'main'"
                    v-show="view !== 'main'">Tillbaka</button>
                <button class="px-10 border-black rounded" @click="view = 'history'" v-show="view !== 'history'">Visa
                    försälningshistorik</button>
            </div>
            <show-list class="w-full" v-show="view === 'main'" />
            <history-graph class="w-full overflow-hidden" v-show="view === 'history'"></history-graph>
        </div>

    </div>
</template>

