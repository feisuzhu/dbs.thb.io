<template>
  <nav class="sticky-top">
    <div class="container">
      <div class="row">
        <div class="col-auto">
          <a href="#" @click="$router.back()">
            <icon-delete-left />
          </a>
        </div>
        <div class="col"></div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!collection.prev">
            <icon-chevrons-left />
          </i>
          <router-link :to="colLink('prev')" v-else>
            <icon-chevrons-left />
          </router-link>
        </div>
        <div class="col-3 text-center">
          <div class="sku">{{ sku }}</div>
        </div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!collection.next">
            <icon-chevrons-right />
          </i>
          <router-link :to="colLink('next')" v-else>
            <icon-chevrons-right />
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useQuery } from '@vue/apollo-composable'
import { RouterLink, useRoute } from 'vue-router'
import { computed } from 'vue'
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component';
import IconChevronLeft from '@/assets/chevron-left.svg?component';
import IconChevronRight from '@/assets/chevron-right.svg?component';
import IconChevronsLeft from '@/assets/chevrons-left.svg?component';
import IconChevronsRight from '@/assets/chevrons-right.svg?component';
import Character from '@/components/game/Character.vue'
import Spellcard from '@/components/game/Spellcard.vue'
import gql from 'graphql-tag'
import _ from 'lodash'

// { path: '/:col(build|episode)/:colsku/:typ(character|spellcard)/:sku',

const route = useRoute();
const p = route.params;

var colGraphQL    = null;
var filter        = null;
var entityGraphQL = null;
var entityList    = null;

const buildQuery = useQuery(gql`
  query CollectionBuildQuery($sku: String!) {
    collection: build(sku: $sku) {
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
`, () => ({
  enabled: p.colType == 'build',
  variables: { sku: p.col },
}));

const episodeQuery = useQuery(gql`
  query CollectionEpisodeQuery($sku: String!) {
    collection: episode(sku: $sku) {
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
`, () => ({
  enabled: p.colType == 'episode',
  variables: { sku: p.col },
}));

const characterQuery = useQuery(gql`
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
`, () => ({
  enabled: p.type == 'character',
  variables: { sku: p.sku },
}));

const spellcardQuery = useQuery(gql`
  query SpellcardQuery($sku: String!) {
    spellcard(sku: $sku) {
      id
      sku title
      gorgeousness cost intensity
      type {
        name description bgcolor isAttack
      }
      traits {
        name description bgcolor
      }
      effect
      faq
      basicConstraint
      extendedConstraints {
        type effect
      }
      build { sku name }
      versions {
        version
        rarity image line
        illustrator { name }
        episode { sku name }
      }
    }
  }
`, () => ({
  enabled: p.type == 'spellcard',
  variables: { sku: p.sku },
}));
const collectionConfig = {
  build: {
    gql: buildGraphQL,
    filter: v => v,
    entityList: (col) => col.characters.map(v => ['character', v.sku])
                         .concat(col.spellcards.map(v => ['spellcard', v.sku])),
  },
  episode: {
    gql: episodeGraphQL,
    filter: v => ({ ...v, versions: v.versions.filter(v => v.episode.sku == col) }),
    entityList: (col) => col.characterVersions.map(v => ['character', v.ref.sku])
                         .concat(col.spellcardVersions.map(v => ['spellcard', v.ref.sku])),
  },
}

const collection = computed(() => colQuery.loading.value ? {} : colQuery.result.value.collection);
const entityLookup = computed(() => {
  let ids = entityList.value.map(v => v[1]);
  let prev = [[null, null]].concat(entityList.value.slice(0, -1));
  let next = entityList.value.slice(1).concat([[null, null]]);
  return _.zip(ids, prev, next).reduce((acc, [id, p, n]) => ({ ...acc, [id]: { prev: p, next: n } }), {});
});

const colLink = (direction) => {
  let col = collection.value[direction];
  if(!col) return null;
  let { type, sku } = col.firstEntity;
  return `/${colType}/${col.sku}/${type}/${sku}`;
};

</script>


<template>
  <Navigation :sku="sku"
              :prevColLink="prevColLink"
              :nextColLink="nextColLink"
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
  type:  { type: String, required: true },
  sku:   { type: String, required: true },
});


const buildQuery = useQuery(gql`
  query CollectionBuildQuery($sku: String!) {
    collection: build(sku: $sku) {
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
`, () => ({
  variables: { sku: props.build },
}));

const col = computed(() => buildQuery.loading.value ? {} : buildQuery.result.value.collection);
const cards = computed(() => [[null, null]]
                             .concat(col.characters.map(v => ['character', v.sku]))
                             .concat(col.spellcards.map(v => ['spellcard', v.sku]))
                             .concat([[null, null]]));


const prevCollectionLink = computed(() => {
  if (col.value.prev == null) return null;
  let [type, sku] = col.value.prev.firstEntity;
  return `/build/${col.value.prev.sku}/${type}/${sku}`;
});

const nextCollectionLink = computed(() => {
  if (col.value.next == null) return null;
  let [type, sku] = col.value.next.firstEntity;
  return `/build/${col.value.next.sku}/${type}/${sku}`;
});

const prevCardLink = computed(() => {
  let [type, sku] = cards.value[cards.value.findIndex(v => v[1] == props.sku) - 1];
  if (type == null) return null;
  return `/build/${props.build}/${type}/${sku}`;
});

const nextCardLink = computed(() => {
  let [type, sku] = cards.value[cards.value.findIndex(v => v[1] == props.sku) + 1];
  if (type == null) return null;
  return `/build/${props.build}/${type}/${sku}`;
});

</script>
