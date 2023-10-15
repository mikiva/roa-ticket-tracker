<template>
  <Panel>
    <h2 class="text-xl font-bold flex justify-between">
      <span>Artiklar</span>
    </h2>
    <template v-if="loading">
      <div class="flex items-center gap-4">

        <load-spinner></load-spinner>
        Hämtar...
      </div>
    </template>
    <template v-else>

      <div v-for="(art, idx) in articles" :key="art.title"
           class="flex-col flex relative border rounded border-slate-100/50 mb-2 p-2 ">
        <router-link :to="{name: 'ExternalView', params: {id: art.id}}" class="flex font-bold hover:underline">
          <div class="flex-[3]">
            {{ art.title }}
          </div>
        </router-link>
        <i class="text-sm opacity-70">{{ art.publisher }}</i>
        <i class="text-sm opacity-70">{{ art.date }}</i>
      </div>
    </template>
  </Panel>
</template>

<script setup>
import {inject} from "vue";
import Panel from "@/components/Panel.vue";
import {ArrowTopRightOnSquareIcon as ExtIcon} from "@heroicons/vue/24/outline";
import LoadSpinner from "@/components/LoadSpinner.vue";

const [articles, loading] = inject("EXTERNAL_ARTICLES")
</script>

<style scoped>

</style>