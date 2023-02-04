<template>
  <BuildNav :build="$route.params.col" :card="$route.params.sku" v-if="$route.params.colType == 'build'" />
  <EpisodeNav :episode="$route.params.col" :card="$route.params.sku" v-if="$route.params.colType == 'episode'" />
</template>

<style lang="scss">
</style>

<script setup>
import { useQuery } from '@vue/apollo-composable'
import { RouterLink, useRoute } from 'vue-router'
import { computed } from 'vue'
import BuildNav from './BuildNav.vue'
import EpisodeNav from './EpisodeNav.vue'
import gql from 'graphql-tag'
import _ from 'lodash'

// { path: '/:col(build|episode)/:colsku/:typ(character|spellcard)/:sku',


/* const characterQuery = useQuery(gql` */
/*   query CharacterQuery($sku: String!) { */
/*     character(sku: $sku) { */
/*       id */
/*       sku title */
/*       skills { */
/*         name type description */
/*       } */
/*       versions { */
/*         version */
/*         rarity image line */
/*         illustrator { name } */
/*         episode { sku name } */
/*       } */
/*     } */
/*   } */
/* `, () => ({ */
/*   enabled: p.type == 'character', */
/*   variables: { sku: p.sku }, */
/* })); */

/* const spellcardQuery = useQuery(gql` */
/*   query SpellcardQuery($sku: String!) { */
/*     spellcard(sku: $sku) { */
/*       id */
/*       sku title */
/*       gorgeousness cost intensity */
/*       type { */
/*         name description bgcolor isAttack */
/*       } */
/*       traits { */
/*         name description bgcolor */
/*       } */
/*       effect */
/*       faq */
/*       basicConstraint */
/*       extendedConstraints { */
/*         type effect */
/*       } */
/*       build { sku name } */
/*       versions { */
/*         version */
/*         rarity image line */
/*         illustrator { name } */
/*         episode { sku name } */
/*       } */
/*     } */
/*   } */
/* `, () => ({ */
/*   enabled: p.type == 'spellcard', */
/*   variables: { sku: p.sku }, */
/* })); */
/* const collectionConfig = { */
/*   build: { */
/*     gql: buildGraphQL, */
/*     filter: v => v, */
/*     entityList: (col) => col.characters.map(v => ['character', v.sku]) */
/*                          .concat(col.spellcards.map(v => ['spellcard', v.sku])), */
/*   }, */
/*   episode: { */
/*     gql: episodeGraphQL, */
/*     filter: v => ({ ...v, versions: v.versions.filter(v => v.episode.sku == col) }), */
/*     entityList: (col) => col.characterVersions.map(v => ['character', v.ref.sku]) */
/*                          .concat(col.spellcardVersions.map(v => ['spellcard', v.ref.sku])), */
/*   }, */
/* } */

/* const collection = computed(() => colQuery.loading.value ? {} : colQuery.result.value.collection); */
/* const entityLookup = computed(() => { */
/*   let ids = entityList.value.map(v => v[1]); */
/*   let prev = [[null, null]].concat(entityList.value.slice(0, -1)); */
/*   let next = entityList.value.slice(1).concat([[null, null]]); */
/*   return _.zip(ids, prev, next).reduce((acc, [id, p, n]) => ({ ...acc, [id]: { prev: p, next: n } }), {}); */
/* }); */

/* const colLink = (direction) => { */
/*   let col = collection.value[direction]; */
/*   if(!col) return null; */
/*   let { type, sku } = col.firstEntity; */
/*   return `/${colType}/${col.sku}/${type}/${sku}`; */
/* }; */

</script>
