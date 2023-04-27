<template>
  <GameCard :card="card" back="/uploads/card/character-back.jpg">
    <template #tags>
      <span style="background-color: black;" class="tag">角色卡</span>
    </template>

    <template #content>
      <SVGText class="title" :text="`「${card.title}」`" />
      <template v-for="sk in card.skills">
        <span class="tag" :class="sk.type.toLowerCase()">{{ sk.type }}：{{ sk.name }}</span>
        <p tabindex=0 v-html="sk.description"></p>
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
