<template>
  <Navigation :collection="$route.params.col" :card="$route.params.sku" />
  <div class="container" v-if="!cardQuery.loading.value">
    <Character :card="card" v-if="card.class == 'Character'" @click="deactivate" />
    <Spellcard :card="card" v-if="card.class == 'Spellcard'" @click="deactivate" />
    <div class="faq">
      <div class="header">FAQ 与 轶事</div>
      <div class="body">
        {{ card.faq || "这张卡片暂不涉及特别的结算规则。" }}
      </div>
    </div>
  </div>
</template>

<style lang="scss">
</style>

<script setup>
import { useQuery } from '@vue/apollo-composable'
import { RouterLink, useRoute } from 'vue-router'
import { computed } from 'vue'
import Navigation from './Navigation.vue'
import Character from './Character.vue'
import Spellcard from './Spellcard.vue'
import gql from 'graphql-tag'
import { activeCard } from '@/components/game/pokemon-css/helpers.js'

// HACK
const deactivate = () => {
  activeCard.value = null;
}

const route = useRoute();

const cardQuery = useQuery(gql`
  fragment VersionFields on Version {
    version
    rarity image line
    illustrator { name }
    episode { sku name }
  }

  query SpellcardQuery($sku: String!) {
    card(sku: $sku) {
      class: __typename
      id sku title faq
      ... on Character {
        skills {
          name type description
        }
        versions {
          ...VersionFields
        }
      }
      ... on Spellcard {
        gorgeousness cost intensity
        type {
          name description bgcolor isAttack
        }
        traits {
          name description bgcolor
        }
        effect
        basicConstraint
        extendedConstraints {
          type effect
        }
        build { sku name }
        versions {
          ...VersionFields
        }
      }
    }
  }
`, () => ({ sku: route.params.sku }));

const card = computed(() => cardQuery.result?.value.card);

</script>

<style lang="scss">
  @import "bootstrap/scss/functions";
  @import "bootstrap/scss/variables";
  @import "bootstrap/scss/mixins";

  .game-card.single {
    $image-info-gap: 2%;
    --hpad: 40%;

    aspect-ratio: unset;

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
          margin: 0;
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

  .faq {
    --img-offs-x: 10px;
    --img-offs-y: 25px;
    --header-height: 48px;
    --r: 15px;

    display: block;
    margin: 15px 0px;
    width: 100%;

    .header {
      height: var(--header-height);
      margin: 45px 0px 0px var(--img-offs-x);
      padding: 0 0 0 20px;
      background-color: #4e4e4e;
      border-radius: var(--r) var(--r) 0 0;
      color: white;
      font-size: 20px;
      line-height: var(--header-height);
    }

    .body {
      display: block;
      width: calc(100% - var(--img-offs-x));
      min-height: 300px;
      box-shadow: 2px 2px 8px #ccc;
      border-radius: 0 0 var(--r) var(--r);
      margin: 0px 0px 0px var(--img-offs-x);
      box-shadow: 2px 2px 8px #ccc;
      background-color: #f7f7f7;
      padding: 20px;
    }
  }
</style>
