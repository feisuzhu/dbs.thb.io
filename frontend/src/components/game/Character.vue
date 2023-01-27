<template>
  <GameCard :card="card">
    <template #tags>
      <span style="background-color: black;" class="tag">角色卡</span>
    </template>

    <template #content>
      <SVGText class="title" :text="`「${card.title}」`" />
      <template v-for="sk in card.skills">
        <span class="tag" :class="sk.type.toLowerCase()">{{ sk.type }}：{{ sk.name }}</span>
        <p class="text resizable">{{ sk.description }}</p>
      </template>
    </template>
  </GameCard>
</template>

<script setup>
import GameCard from './GameCard.vue'
import SVGText from './SVGText.vue'
const props = defineProps({
  card: {
    type: Object,
  }
});
</script>

<style lang="scss" scoped>
  .tag {
    flex: 0 0 auto;
  }
  .game-card .text {
    text-align: left;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
</style>
