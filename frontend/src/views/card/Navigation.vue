<template>
  <nav class="sticky-top">
    <div class="container">
      <div class="row">
        <div class="col-auto">
          <a href="#" @click="$router.back()">
            <icon-delete-left />
          </a>
        </div>
        <div class="col-auto card-name">{{ card.title }}</div>
        <div class="col" style="padding: 0"></div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!prevCollectionLink">
            <icon-chevrons-left />
          </i>
          <router-link :to="prevCollectionLink" v-else>
            <icon-chevrons-left />
          </router-link>
        </div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!prevCardLink">
            <icon-chevron-left />
          </i>
          <router-link :to="prevCardLink" v-else>
            <icon-chevron-left />
          </router-link>
        </div>
        <div class="col-auto col-md-2 text-center">
          <div class="sku">{{ card.sku }}</div>
        </div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!nextCardLink">
            <icon-chevron-right />
          </i>
          <router-link :to="nextCardLink" v-else>
            <icon-chevron-right />
          </router-link>
        </div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!nextCollectionLink">
            <icon-chevrons-right />
          </i>
          <router-link :to="nextCollectionLink" v-else>
            <icon-chevrons-right />
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<style lang="scss">
  nav {
    .sku {
      transform: translate(0, -3px);
    }

    .no-more {
      color: #555;
    }

    @media (max-width: 600px) {
      .row > div {
        padding: 0 6px;
      }
    }
  }
</style>

<script setup>
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component';
import IconChevronLeft from '@/assets/chevron-left.svg?component';
import IconChevronRight from '@/assets/chevron-right.svg?component';
import IconChevronsLeft from '@/assets/chevrons-left.svg?component';
import IconChevronsRight from '@/assets/chevrons-right.svg?component';

import { useQuery } from '@vue/apollo-composable'
import { computed } from 'vue'
import gql from 'graphql-tag'
import _ from 'lodash'

const props = defineProps({
  collection: { type: String, required: true },
  card:  { type: String, required: true },
});


const navigationQuery = useQuery(gql`
  query NavigationQuery($col: String!, $card: String!) {
    collection(sku: $col) {
      class: __typename
      id
      ... on Build {
        cards {
          class: __typename
          sku
        }
      }
      ... on Episode {
      	versions {
          card {
            class: __typename
            sku
          }
        }
      }
      prev {
        sku
        firstCard {
          class: __typename
          sku
        }
      }
      next {
        sku
        firstCard {
          class: __typename
          sku
        }
      }
    }
    card(sku: $card) {
      sku
      title
    }
  }
`, () => ({ col: props.collection,
            card: props.card }));

const col = computed(() => navigationQuery.loading.value ? {} : navigationQuery.result.value.collection);
const card = computed(() => navigationQuery.loading.value ? {} : navigationQuery.result.value.card);
const cards = computed(() => !col.value?.id ? [] : [null]
                             .concat(col.value.cards?.map(v => v.sku) ?? [])
                             .concat(col.value.versions?.map(v => v.card.sku) ?? [])
                             .concat([null]));


const prevCollectionLink = computed(() => {
  if (col.value.prev == null) return null;
  let { type, sku } = col.value.prev.firstCard;
  return `/${col.value.prev.sku}/${sku}`;
});

const nextCollectionLink = computed(() => {
  if (col.value.next == null) return null;
  let { type, sku } = col.value.next.firstCard;
  return `/${col.value.next.sku}/${sku}`;
});

const prevCardLink = computed(() => {
  let idx = cards.value.findIndex(v => v == props.card);
  if(idx == -1) return null;
  if(idx <= 0) return null;
  let sku = cards.value[idx - 1];
  if(sku == null) return null;
  return `/${props.collection}/${sku}`;
});

const nextCardLink = computed(() => {
  let idx = cards.value.findIndex(v => v == props.card);
  if(idx == -1) return null;
  if(idx >= cards.value.length - 1) return null;
  let sku = cards.value[idx + 1];
  if(sku == null) return null;
  return `/${props.collection}/${sku}`;
});

</script>
