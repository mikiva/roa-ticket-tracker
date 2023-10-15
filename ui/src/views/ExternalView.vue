<template>
  <div class="bg-black w-full min-h-full relative bg-gradient-to-b from-black from-70%  to-red-500/10 text-white p-3">
    <div class="flex flex-col gap-7 ">

      <div class="m-auto max-w-xl border-4 border-black bg-black/80 p-4 rounded-md z-10 relative">
        <router-link to="/#articles" class="flex gap-3">
          <arrow-left-icon class="w-6 h-6"></arrow-left-icon>
          Tillbaka
        </router-link>
        <h2 class="text-2xl font-bold">{{ current.title }}</h2>
        <i class="text-sm opacity-70">{{ current.publisher }}</i> <br>
        <i class="text-sm opacity-70">{{ current.date }}</i>
        <br>
        <br>
        <template v-if="loading">
          <div class="flex items-center gap-4">

            <load-spinner></load-spinner>
            Hämtar...
          </div>
        </template>
        <template v-else>

          <b class="text-lg">{{ current.preamble }}</b>
          <br>
          <br>
          <p v-for="text in articles" class="mb-5">
            {{ text }}
          </p>
          <p><i class="opacity-70">{{ current.author }}</i></p>
          <p><i class="text-xs"><a :href="current.sourceUrl" target="_blank"
                                   class="underline">{{ current.sourceUrl }}</a></i></p>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>


import {onBeforeMount, onMounted, ref} from "vue";
import {useRoute} from "vue-router";
import LoadSpinner from "@/components/LoadSpinner.vue";
import {ArrowLeftIcon} from "@heroicons/vue/24/outline";

const route = useRoute();

const loading = ref(false);
const articles = ref([])
const current = ref({})

onMounted(async () => {
  loading.value = true;
  const articleUrl = "/ext/articles.json"
  const articlesRes = await fetch(articleUrl)
  const arts = await articlesRes.json()
  current.value = arts.find(a => a.id === route.params.id)
  try {
    document.title = current.value.title;
  } catch {
  }
  const textUrl = current.value.textUrl
  const textRes = await fetch(textUrl, {headers: {'Content-Type': "html/text"}})
  const text = await textRes.text()
  articles.value = text.split("\n")
  loading.value = false;

})

</script>

<style scoped>

</style>