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
  episode: { type: String, required: true },
  card:    { type: String, required: true },
});


const episodeQuery = useQuery(gql`
  query CollectionEpisodeQuery($sku: String!) {
    episode(sku: $sku) {
      id
      characterVersions { ref: character { sku } }
      spellcardVersions { ref: spellcard { sku } }
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
`, () => ({ sku: props.episode }));


const col = computed(() => episodeQuery.loading.value ? {} : episodeQuery.result.value.episode);
const cards = computed(() => !col.value?.id ? [] : [[null, null]]
                             .concat(col.value.characterVersions?.map(v => ['character', v.ref.sku]))
                             .concat(col.value.spellcardVersions?.map(v => ['spellcard', v.ref.sku]))
                             .concat([[null, null]]));


const prevCollectionLink = computed(() => {
  if (col.value.prev == null) return null;
  let { type, sku } = col.value.prev.firstEntity;
  return `/episode/${col.value.prev.sku}/${type.toLowerCase()}/${sku}`;
});

const nextCollectionLink = computed(() => {
  if (col.value.next == null) return null;
  let { type, sku } = col.value.next.firstEntity;
  return `/episode/${col.value.next.sku}/${type.toLowerCase()}/${sku}`;
});

const prevCardLink = computed(() => {
  let idx = cards.value.findIndex(v => v[1] == props.card);
  if(idx == -1) return null;
  if(idx <= 0) return null;
  let [type, sku] = cards.value[idx - 1];
  if (type == null) return null;
  return `/episode/${props.episode}/${type.toLowerCase()}/${sku}`;
});

const nextCardLink = computed(() => {
  let idx = cards.value.findIndex(v => v[1] == props.card);
  if(idx == -1) return null;
  if(idx >= cards.value.length - 1) return null;
  let [type, sku] = cards.value[idx + 1];
  if (type == null) return null;
  return `/episode/${props.episode}/${type.toLowerCase()}/${sku}`;
});

</script>
