<template>
  <div class="m-auto max-w-xl border-4 border-black bg-black/80 p-4 rounded-md z-10 relative">

    <show-list-item :show="{ startDate: 'Föreställning', 'sold': 'Sålda', 'today': 'Idag' }" class="font-bold" />

    <template v-if="loading">
      <div class="flex items-center gap-4">

        <load-spinner></load-spinner>
        Hämtar...
      </div>
    </template>
    <template v-else>
      <show-list-item :show="show" v-for="show in event.shows" />
      <show-list-item :show="event.total" class="text-xl font-bold mt-2" />
    </template>
  </div>
</template>

<script setup>
import ShowListItem from './ShowListItem.vue';
import {ref, reactive, onMounted, computed, inject} from 'vue';
import LoadSpinner from "./LoadSpinner.vue";
const url = "/api/shows/sold/today"

const loading = ref(false);
const event = reactive({ shows: [], total: { startDate: "TOTAL", sold: 0, today: 0 } })

onMounted(async () => {
  loading.value = true;
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

  loading.value = false;
})


</script>

<style scoped></style>