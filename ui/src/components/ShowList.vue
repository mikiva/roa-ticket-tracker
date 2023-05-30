<template>
    <div class="m-auto max-w-xl border-4 border-black bg-black/80 p-4 rounded-md z-10 relative">
        <show-list-item :show="{ startDate: 'Föreställning', 'sold': 'Sålda', 'today': 'Idag' }"
            class="text-xl font-bold" />

        <show-list-item :show="show" v-for="show in event.shows" />
        <show-list-item :show="event.total" class="text-xl font-bold mt-2" />
    </div>
</template>

<script setup>
import ShowListItem from './ShowListItem.vue';
import { reactive, onMounted, computed } from 'vue';
//const url = "https://www.nortic.se/api/json/event/47696"
const url = "/api/shows/sold/today"

const event = reactive({ shows: [], total: { startDate: "", sold: 0, today: 0 } })


onMounted(async () => {
    const res = await fetch(url)
    const result = await res.json();
    event.shows = result;

    let sold = 0;
    let today = 0;

    event.shows.forEach(show => {
        sold += show.sold;
        today += show.today;
    })
    event.total.startDate = "TOTAL";
    event.total.sold = sold;
    event.total.today = today;
})


</script>

<style scoped></style>