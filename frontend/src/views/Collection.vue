<template>
  <ApolloQuery :query="collection.query" :variables="{sku: $route.params.sku }" tag="">
    <template v-slot="{ result: { data, error }, isLoading, query }">
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
              <i class="no-more" v-if="!data?.collection.prev">
                <icon-chevrons-left />
              </i>
              <router-link :to="`/${colType}/${data?.collection.prev.sku}`" @click="query.refetch() || true" v-else>
                <icon-chevrons-left />
              </router-link>
            </div>
            <div class="col-3 text-center d-md-none">
              <div class="sku">{{ data?.collection.sku }}</div>
            </div>
            <div class="col-auto nav-collection-image text-center d-none d-md-block" style="width: 379px;">
              <img :src="data?.collection.image" :alt="data?.collection.name">
            </div>
            <div class="col-auto text-end">
              <i class="no-more" v-if="!data?.collection.next">
                <icon-chevrons-right />
              </i>
              <router-link :to="`/${colType}/${data.collection.next.sku}`" v-else>
                <icon-chevrons-right />
              </router-link>
            </div>
          </div>
        </div>
      </nav>
      <div class="container collection-content-list" v-if="!isLoading">
        <div class="row">
          <div class="col-lg-6 twin-center" v-for="(ch, i) in collection.characters(data)" :key="`character-${i}`">
            <Character :card="ch" />
          </div>
          <div class="col-lg-6 twin-center" v-for="(sc, i) in collection.spellcards(data)" :key="`spellcard-${i}`">
            <Spellcard :card="sc" />
          </div>
        </div>
      </div>
    </template>
  </ApolloQuery>
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
import { RouterLink, useRoute } from 'vue-router'
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component';
import IconChevronLeft from '@/assets/chevron-left.svg?component';
import IconChevronRight from '@/assets/chevron-right.svg?component';
import IconChevronsLeft from '@/assets/chevrons-left.svg?component';
import IconChevronsRight from '@/assets/chevrons-right.svg?component';
import Character from '@/components/game/Character.vue'
import Spellcard from '@/components/game/Spellcard.vue'
import gql from 'graphql-tag'

const route = useRoute();
const colType = route.params.colType;

const buildQuery = gql`
  query QueryBuildContent($sku: String!) {
    collection: build(sku: $sku) {
      id sku name image
      characters {
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
      spellcards {
        sku title
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
          version
          rarity image line
          illustrator { name }
          episode { sku name }
        }
      }
      prev { sku }
      next { sku }
    }
  }
`;
const buildCharacters = (data) => data.collection.characters;
const buildSpellcards = (data) => data.collection.spellcards;

const episodeQuery = gql`
  query QueryEpisodeContent($sku: String!) {
    collection: episode(sku: $sku) {
      id
      sku name image
      characterVersions {
        version
        rarity image line
        illustrator { name }
        episode { sku name }
        character {
          sku title
          build { sku name }
          skills {
            name type description
          }
        }
      }
      spellcardVersions {
        version
        rarity image line
        illustrator { name }
        episode { sku name }

        spellcard {
          sku title
          build { sku name }
          type {
            name description bgcolor isAttack
          }
          gorgeousness
          cost
          effect
          intensity
          traits {
            name description bgcolor
          }
          faq
          basicConstraint
          extendedConstraints {
            type effect
          }
        }
      }
      prev { sku }
      next { sku }
    }
  }
`;
const transform = (l, k) => l.map(v => ({ ...v[k], versions: [v] }));
const episodeCharacters = (data) => transform(data.collection.characterVersions, 'character');
const episodeSpellcards = (data) => transform(data.collection.spellcardVersions, 'spellcard');

var collection = {};

if(colType == 'build') {
  collection = {
    query: buildQuery,
    characters: buildCharacters,
    spellcards: buildSpellcards,
  };
} else if(colType == 'episode') {
  collection = {
    query: episodeQuery,
    characters: episodeCharacters,
    spellcards: episodeSpellcards,
  };
} else {
  console.error('Unknown collection type', colType);
}

</script>
