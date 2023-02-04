<template>
  <Navigation :sku="card"
              :prevCollectionLink="prevCollectionLink"
              :nextCollectionLink="nextCollectionLink"
              :prevCardLink="prevCardLink"
              :nextCardLink="nextCardLink" />
</template>

<script setup>
import { useQuery } from '@vue/apollo-composable'
import { computed } from 'vue'
import gql from 'graphql-tag'
import _ from 'lodash'

import Navigation from './Navigation.vue'

const props = defineProps({
  build: { type: String, required: true },
  card:  { type: String, required: true },
});


const buildQuery = useQuery(gql`
  query CollectionBuildQuery($sku: String!) {
    build(sku: $sku) {
      id
      characters { sku }
      spellcards { sku }
      prev {
        sku
        firstEntity {
          type: __typename
          ... on Character { sku }
          ... on Spellcard { sku }
        }
      }
      next {
        sku
        firstEntity {
          type: __typename
          ... on Character { sku }
          ... on Spellcard { sku }
        }
      }
    }
  }
`, () => ({ sku: props.build }));

const col = computed(() => buildQuery.loading.value ? {} : buildQuery.result.value.build);
const cards = computed(() => !col.value?.id ? [] : [[null, null]]
                             .concat(col.value.characters?.map(v => ['character', v.sku]))
                             .concat(col.value.spellcards?.map(v => ['spellcard', v.sku]))
                             .concat([[null, null]]));


const prevCollectionLink = computed(() => {
  if (col.value.prev == null) return null;
  let { type, sku } = col.value.prev.firstEntity;
  return `/build/${col.value.prev.sku}/${type.toLowerCase()}/${sku}`;
});

const nextCollectionLink = computed(() => {
  if (col.value.next == null) return null;
  let { type, sku } = col.value.next.firstEntity;
  return `/build/${col.value.next.sku}/${type.toLowerCase()}/${sku}`;
});

const prevCardLink = computed(() => {
  let idx = cards.value.findIndex(v => v[1] == props.card);
  if(idx == -1) return null;
  if(idx <= 0) return null;
  let [type, sku] = cards.value[idx - 1];
  if (type == null) return null;
  return `/build/${props.build}/${type.toLowerCase()}/${sku}`;
});

const nextCardLink = computed(() => {
  let idx = cards.value.findIndex(v => v[1] == props.card);
  if(idx == -1) return null;
  if(idx >= cards.value.length - 1) return null;
  console.log('nextCardLink', idx, cards.value[idx], cards.value[idx + 1]);
  let [type, sku] = cards.value[idx + 1];
  if (type == null) return null;
  return `/build/${props.build}/${type.toLowerCase()}/${sku}`;
});

</script>
