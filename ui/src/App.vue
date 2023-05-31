<script setup>
import CountdownTimer from "./components/CountdownTimer.vue";
import ShowList from "./components/ShowList.vue";
import roa from "./assets/roa.png"
import splash from "./assets/roa_color_splash.png"
</script>

<template>
    <div class="bg-black w-screen h-full relative bg-gradient-to-b from-black from-70%  to-orange-500/10 text-white p-3">
        <div class="relative m-auto max-w-xl blur-sm">
            <img :src="splash" alt="" class="absolute animate-pulse">
            <img :src="roa" alt="" class="absolute left-[50%] -translate-x-[50%]">
        </div>
        <countdown-timer class="mb-10" />
        <show-list />

    </div>
</template>

