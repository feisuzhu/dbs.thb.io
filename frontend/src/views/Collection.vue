<template>
  <nav class="sticky-top">
    <div class="container">
      <div class="row">
        <div class="col-auto">
          <a class="icon" href="#" @click="$router.back()">
            <icon-delete-left />
          </a>
        </div>
        <div class="col"></div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!col.prev">
            <icon-chevrons-left />
          </i>
          <router-link class="icon" :to="`/${col.prev.sku}`" @click="collectionQuery.refetch() || true" v-else>
            <icon-chevrons-left />
          </router-link>
        </div>
        <div class="col-3 text-center d-md-none">
          <div class="sku">{{ col.sku }}</div>
        </div>
        <div class="col-auto nav-collection-image text-center d-none d-md-block" style="width: 379px;">
          <img :src="col.image" :alt="col.name">
        </div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!col.next">
            <icon-chevrons-right />
          </i>
          <router-link class="icon" :to="`/${col.next.sku}`" v-else>
            <icon-chevrons-right />
          </router-link>
        </div>
      </div>
    </div>
  </nav>
  <div class="container collection-content-list" v-if="col">
    <div class="row">
      <div class="col-lg-6 twin-center" v-for="(c, i) in cards" :key="`card-${i}`">
        <Character :card="c" v-if="c.class == 'Character'" @click="navigateToDetail(c)" />
        <Spellcard :card="c" v-if="c.class == 'Spellcard'" @click="navigateToDetail(c)" />
      </div>
    </div>
  </div>
</template>

<style lang="scss">
  nav {
    .sku {
      transform: translate(0, -3px);
    }
    .no-more {
      color: #555;
    }

    .nav-collection-image {
      position: relative;

      img {
        position: absolute;
        top: 50%;
        left: 50%;
        width: auto;
        height: 96px;
        border-radius: 5px;
        transform: translate(-50%, -50%);
      }
    }
  }

  .collection-content-list {
    margin-top: 20px;
  }
</style>

<script setup>
import { RouterLink, useRoute, useRouter } from 'vue-router'
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component';
import IconChevronLeft from '@/assets/chevron-left.svg?component';
import IconChevronRight from '@/assets/chevron-right.svg?component';
import IconChevronsLeft from '@/assets/chevrons-left.svg?component';
import IconChevronsRight from '@/assets/chevrons-right.svg?component';
import Character from '@/components/game/Character.vue'
import Spellcard from '@/components/game/Spellcard.vue'
import gql from 'graphql-tag'
import { computed } from 'vue'
import { useQuery } from '@vue/apollo-composable'

const route = useRoute();
const router = useRouter();

/* `, () => ({ col: props.collection, */
/*             card: props.card })); */

const collectionQuery= useQuery(gql`
  fragment VersionFields on Version {
    version
    rarity image line
    illustrator { name }
    episodes { sku name }
  }

  fragment CardFields on Card {
    class: __typename
    id sku title
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

  query QueryCollectionContent($sku: String!) {
    collection(sku: $sku) {
      class: __typename
      id sku name image
      ... on Build {
        cards {
          ...CardFields
        }
      }
      ... on Episode {
        versions {
          card {
            ...CardFields
          }
        }
      }
      prev { sku }
      next { sku }
    }
  }
`, () => ({ sku: route.params.sku }));

const col = computed(() => collectionQuery.loading.value ? {} : collectionQuery.result.value.collection);
const cards = computed(() => !collectionQuery.loading.value ? (col.value?.cards || col.value.versions.map(v => v.card)) : []);

const navigateToDetail = (c) => {
  router.push({ name: 'card', params: { col: route.params.sku, sku: c.sku } });
}
</script>
