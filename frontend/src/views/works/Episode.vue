<template>
  <ApolloQuery :query="episodeQuery" :variables="{sku: $route.params.sku }" tag="">
    <template v-slot="{ result: { data, error }, isLoading, query }">
      <Navigation>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!data?.episode.prev">
            <icon-chevrons-left />
          </i>
          <router-link :to="'/episode/' + data?.episode.prev.sku" @click="query.refetch() || true" v-else>
            <icon-chevrons-left />
          </router-link>
        </div>
        <div class="col-3 text-center d-md-none">
          <div class="sku">{{ data?.episode.sku }}</div>
        </div>
        <div class="col-auto nav-episode-image text-center d-none d-md-block" style="width: 379px;">
          <img :src="data?.episode.image" :alt="data?.episode.name">
        </div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!data?.episode.next">
            <icon-chevrons-right />
          </i>
          <router-link :to="'/episode/' + data.episode.next.sku" v-else>
            <icon-chevrons-right />
          </router-link>
        </div>
      </Navigation>
      <div class="container episode-content-list" v-if="!isLoading">
        <div class="row">
          <div class="col-lg-6 twin-center" v-for="(ch, i) in transform(data.episode.characterVersions, 'character')" :key="'character-' + i">
            <Character :card="ch" />
          </div>
          <div class="col-lg-6 twin-center" v-for="(sc, i) in transform(data.episode.spellcardVersions, 'spellcard')" :key="'spellcard-' + i">
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
  }

  .nav-episode-image {
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

  .episode-content-list {
    margin-top: 20px;
  }

</style>

<script setup>
import { RouterLink } from 'vue-router'
import IconChevronLeft from '@/assets/chevron-left.svg?component';
import IconChevronRight from '@/assets/chevron-right.svg?component';
import IconChevronsLeft from '@/assets/chevrons-left.svg?component';
import IconChevronsRight from '@/assets/chevrons-right.svg?component';
import Navigation from '@/components/nav/Navigation.vue'
import Character from '@/components/game/Character.vue'
import Spellcard from '@/components/game/Spellcard.vue'
import gql from 'graphql-tag'

const transform = (l, k) => l.map(v => ({ ...v[k], versions: [v] }));

const episodeQuery = gql`
  query QueryEpisodeContent($sku: String!) {
    episode(sku: $sku) {
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
</script>
