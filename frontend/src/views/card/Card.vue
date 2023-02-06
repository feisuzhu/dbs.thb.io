<template>
  <BuildNav :build="$route.params.col" :card="$route.params.sku" v-if="$route.params.colType == 'build'" />
  <EpisodeNav :episode="$route.params.col" :card="$route.params.sku" v-if="$route.params.colType == 'episode'" />
  <div class="container">
    <Character :card="$route.params.sku" v-if="$route.params.type == 'character'" />
    <Spellcard :card="$route.params.sku" v-if="$route.params.type == 'spellcard'" />
  </div>
</template>

<style lang="scss">
</style>

<script setup>
import { useQuery } from '@vue/apollo-composable'
import { RouterLink, useRoute } from 'vue-router'
import { computed } from 'vue'
import BuildNav from './BuildNav.vue'
import EpisodeNav from './EpisodeNav.vue'
import Character from './Character.vue'
import Spellcard from './Spellcard.vue'
import gql from 'graphql-tag'
import _ from 'lodash'

// { path: '/:col(build|episode)/:colsku/:typ(character|spellcard)/:sku',
</script>

<style lang="scss">
  @import "bootstrap/scss/functions";
  @import "bootstrap/scss/variables";
  @import "bootstrap/scss/mixins";

  .game-card.single {
    $image-info-gap: 2%;
    --hpad: 40%;

    aspect-ratio: unset;

    .scaler {
      position: unset;
      --factor: 1;
    }

    .h-pad { margin-right: $image-info-gap; }

    .card-image img { width: 100%; }

    .body {
      .right {
        align-items: start;
        margin-left: $image-info-gap;

        .title { display: none; }

        .title-text {
          font-size: 24px;
          font-weight: bold;
          margin: 12px 0 6px 0;
        }
        .tag {
          margin: 16px 0 6px 0;
        }
      }
    }
  }
</style>
