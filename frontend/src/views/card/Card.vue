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

    .card-image img { width: 100%; }

    @include media-breakpoint-up(md) {
      .h-pad { margin-right: $image-info-gap; }

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

    @include media-breakpoint-down(md) {
      .h-pad { width: 15px; }

      .body {
        display: block;

        .left {
          width: 100%;
          flex: 0 0 auto;
          transform: none;
          img {
            padding: 10px;
            border-radius: 30px;
          }
        }
        .right {
          width: 100%;
          flex: 0 0 auto;
          padding: 0 10px;
          .title-text { display: none; }
        }
      }

      .meta {
        display: none;
      }

      .secondary-meta {
        display: flex;
        padding: 0 10px;
        align-items: start;
        text-align: left;
        p {
          font-size: 14px;
        }
      }
    }
  }
</style>
