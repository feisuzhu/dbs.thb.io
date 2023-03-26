<template>
  <GameCard :card="card">
    <template #tags>
      <span style="background-color: black;" class="tag">角色卡</span>
    </template>

    <template #content>
      <SVGText class="title" :text="`「${card.title}」`" />
      <template v-for="sk in card.skills">
        <span class="tag" :class="sk.type.toLowerCase()">{{ sk.type }}：{{ sk.name }}</span>
        <p tabindex=0>{{ sk.description }}</p>
      </template>
    </template>
  </GameCard>
</template>

<script setup>
import GameCard from './GameCard.vue'
import SVGText from './SVGText.vue'
const props = defineProps({
  card: { type: Object },
});
</script>
