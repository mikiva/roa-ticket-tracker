<template>
    <div class="flex flex-col justify-center max-w-xl m-auto relative z-20 pt-5">
        <div class="text-white text-center bg-black/75 w-full border-black border-2 py-2 px-5">
            <div className="text-4xl ">PREMIÄR 14 OKTOBER</div>
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
import { computed, reactive, onBeforeUnmount, onBeforeMount } from "vue";

let countInterval = null;
const targetDate = new Date("2023-10-14T15:00:00").getTime()

const current = reactive({ count: getCount() })


const timeParts = computed(() => {
    const { count } = current;
    const {
        days,
        hours,
        minutes,
        seconds
    } = count
    const day = days === 1 ? "dag" : "dagar";
    const hour = hours === 1 ? "timme" : "timmar";
    const minute = minutes === 1 ? "minut" : "minuter";
    const second = seconds === 1 ? "sekund" : "sekunder";

    return [[days, day], [hours, hour], [minutes, minute], [seconds, second]]

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
    const now = new Date().getTime()
    const difference = (targetDate - now) / 1000

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