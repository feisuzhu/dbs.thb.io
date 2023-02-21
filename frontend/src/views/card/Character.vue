<template>
  <GameCard :card="card" class="single">
    <template #tags>
      <span style="background-color: black;" class="tag">角色卡</span>
    </template>

    <template #content>
      <h3 class="title-text">「{{ card.title }}」</h3>
      <SVGText class="title" :text="`「${card.title}」`" />
      <template v-for="sk in card.skills">
        <span class="tag" :class="sk.type.toLowerCase()">{{ sk.type }}：{{ sk.name }}</span>
        <p>{{ sk.description }}</p>
      </template>
    </template>
  </GameCard>
</template>

<script setup>
import GameCard from '@/components/game/GameCard.vue'
import SVGText from '@/components/game/SVGText.vue'
import { gql } from 'graphql-tag'
const props = defineProps({
  card: { type: Object }
});
</script>

