<template>
  <ApolloQuery :query="characterQuery" :variables="{ sku: card }" tag="">
    <template v-slot="{ result: { data, error }, isLoading, query }">
      <GameCard :card="data.character" class="single" v-if="!isLoading && !error" >
        <template #tags>
          <span style="background-color: black;" class="tag">角色卡</span>
        </template>

        <template #content>
          <h3 class="title-text">「{{ data.character.title }}」</h3>
          <SVGText class="title" :text="`「${data.character.title}」`" />
          <template v-for="sk in data.character.skills">
            <span class="tag" :class="sk.type.toLowerCase()">{{ sk.type }}：{{ sk.name }}</span>
            <p>{{ sk.description }}</p>
          </template>
        </template>
      </GameCard>
    </template>
  </ApolloQuery>
</template>

<script setup>
import GameCard from '@/components/game/GameCard.vue'
import SVGText from '@/components/game/SVGText.vue'
import { gql } from 'graphql-tag'
const props = defineProps({
  card: {
    type: Object,
  }
});

const characterQuery = gql`
  query CharacterQuery($sku: String!) {
    character(sku: $sku) {
      id
      sku title
      skills {
        name type description
      }
      versions {
        version
        rarity image line
        illustrator { name }
        episode { sku name }
      }
    }
  }
`;
</script>

