<template>
    <div class="flex flex-col justify-center max-w-xl m-auto relative z-20 pt-5">
        <div class="text-white text-center bg-black/75 w-full border-black border-2 py-2 px-5">
            <div className="text-4xl uppercase">{{note}}</div>
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
import {computed, reactive, onBeforeUnmount, onBeforeMount, inject, ref} from "vue";

let countInterval = null;

const todayIs = inject("TODAY")
const [targetDate, note] = inject("NEXT_SHOW")

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
    const today = new Date().getTime();
    const difference = (targetDate - today) / 1000
    let days = Math.floor(difference / (60 * 60 * 24));
    let hours = Math.floor((difference % (60 * 60 * 24)) / (60 * 60));
    let minutes = Math.floor((difference % (60 * 60)) / 60);
    let seconds = Math.floor(difference % 60);

    return {
        days: days,
        hours: hours,
        minutes: minutes,
        seconds: seconds
    }

}


</script>

<style scoped></style>