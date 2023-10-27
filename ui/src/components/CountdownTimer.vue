<template>
    <div class="flex flex-col justify-center max-w-xl m-auto relative z-20 pt-5">
        <div class="text-white text-center bg-black/75 w-full border-black border-2 py-2 px-5">
            <div class="text-4xl uppercase">{{note}}</div>
            <div class="flex gap-2 text-white text-lg  flex-nowrap justify-around leading-none">
                <div class="text-center" v-for="part in timeParts">
                    <div class="text-4xl">{{ part[0] }}</div>
                    <div class="text-sm text-orange-500">{{ part[1] }}</div>
                </div>
            </div>
        </div>

    </div>
</template>

<script setup>
import {computed, reactive, onBeforeUnmount, onBeforeMount, inject, ref, watch} from "vue";

let countInterval = null;

const emit = defineEmits(["tick"])

const todayIs = inject("TODAY")
const nextShow= inject("NEXT_SHOW")
const targetDate = computed(() => {
  return nextShow.value[0]
})
const note = computed(() => {
  return nextShow.value[1]
})

const current = reactive({ count: getCount() })

const timeParts = computed(() => {
    const { count } = current;
    const {
        days,
        hours,
        minutes,
        seconds
    } = count
    const DAY = days === 1 ? "dag" : "dagar";
    const HOUR = hours === 1 ? "timme" : "timmar";
    const MINUTE = minutes === 1 ? "minut" : "minuter";
    const SECOND = seconds === 1 ? "sekund" : "sekunder";


    return [
      [String(days).padStart(2, "0"), DAY],
      [String(hours).padStart(2, "0"), HOUR],
      [String(minutes).padStart(2, "0"), MINUTE],
      [String(seconds).padStart(2, "0"), SECOND]
  ]

})



function countDown() {
    current.count = getCount()
}

onBeforeMount(() => {
    countInterval = setInterval(countDown, 1000)
})
onBeforeUnmount(() => {
    clearInterval(countInterval)
})


function getCount() {
  if (targetDate.value === -1) {
     return {
        days: 0,
        hours: 0,
        minutes: 0,
        seconds: 0
    }
  }
    const today = new Date().getTime();
    const difference = (targetDate.value - today) / 1000
    let days = Math.floor(difference / (60 * 60 * 24));
    let hours = Math.floor((difference % (60 * 60 * 24)) / (60 * 60));
    let minutes = Math.floor((difference % (60 * 60)) / 60);
    let seconds = Math.floor(difference % 60);

    const togo = {
        days: days,
        hours: hours,
        minutes: minutes,
        seconds: seconds
    }
    try {
      emit("tick", togo)
    }finally {}
  return togo
}


</script>

<style scoped></style>