<template>
  <div class="m-auto max-w-xl border-4 border-black bg-black/80 p-4 rounded-md z-10 relative">
    <h2 class="text-xl font-bold flex justify-between">
      <div></div>
      <button @click="showComparison = !showComparison">
        <div class="px-1 flex gap-0.5 border rounded text-white text-sm items-center"
             :class="{'!text-black !bg-white': showComparison}">
          Jämför 2022&nbsp;
          <Scale class=" w-6 h-6" :class="{'!text-black !bg-white': showComparison}"></Scale>
        </div>
      </button>
    </h2>
    <div class="flex gap-2">
      <div class="basis-[50%]">Datum</div>
      <div class="flex-1">Sålda</div>
      <div class="flex-[4] text-right">
        Idag
      </div>
    </div>

    <template v-if="loading">
      <div class="flex items-center gap-4">

        <load-spinner></load-spinner>
        Hämtar...
      </div>
    </template>
    <template v-else>
      <show-list-item :show="show" :compare="showComparison" v-for="show in eventSold.shows"/>
      <div class="flex gap-2 text-xl font-bold mt-2 p-1.5">
        <div class="basis-[50%]">TOTAL</div>
        <div class="flex-1">{{ eventSold.total.sold }}</div>
        <div class="flex-[4] text-right">
          {{ eventSold.total.today }}
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import ShowListItem from './ShowListItem.vue';
import {ref, reactive, onMounted, computed, inject} from 'vue';
import LoadSpinner from "./LoadSpinner.vue";
import {ScaleIcon as Scale} from "@heroicons/vue/24/outline";

const event = reactive({shows: [], total: {startDate: "TOTAL", sold: 0, today: 0}})

const [result, loading] = inject("SHOWS", [[], false])

const showComparison = ref(false)

const eventSold = computed(() => {

  event.shows = result.value;

  let sold = 0;
  let today = 0;

  event.shows.forEach(show => {
    sold += show.sold;
    today += show.today;
  })
  event.total.startDate = "TOTAL";
  event.total.sold = sold;
  event.total.today = today;


  return event
})


</script>

<style scoped></style>