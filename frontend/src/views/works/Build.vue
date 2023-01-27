<template>
  <ApolloQuery :query="buildQuery" :variables="{sku: $route.params.sku }" tag="">
    <template v-slot="{ result: { data, error }, isLoading, query }">
      <Navigation>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!data?.build.prev">
            <icon-chevrons-left />
          </i>
          <router-link :to="'/build/' + data?.build.prev.sku" @click="query.refetch() || true" v-else>
            <icon-chevrons-left />
          </router-link>
        </div>
        <div class="col-3 text-center d-md-none">
          <div class="sku">{{ data?.build.sku }}</div>
        </div>
        <div class="col-auto nav-build-image text-center d-none d-md-block" style="width: 379px;">
          <img class="nav-build-image" :src="data?.build.image" :alt="data?.build.name">
        </div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!data?.build.next">
            <icon-chevrons-right />
          </i>
          <router-link :to="'/build/' + data.build.next.sku" v-else>
            <icon-chevrons-right />
          </router-link>
        </div>
      </Navigation>
      <div class="container build-content-list" v-if="!isLoading">
        <div class="row">
          <div class="col-lg-6 twin-center" v-for="(ch, i) in data.build.characters" :key="'character-' + i">
            <Character :card="ch" />
          </div>
          <div class="col-lg-6 twin-center" v-for="(sc, i) in data.build.spellcards" :key="'spellcard-' + i">
            <Spellcard :card="sc" :build="data.build" />
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
    .nav-build-image {
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

  .build-content-list {
    $work-img-width: 378px;
    $work-img-height: 124px;

    margin-top: 20px;

    img.work-image {
      display: inline-block;
      width: $work-img-width;
      height: $work-img-height;
      margin: 12px 0;
      border-radius: 8px;
    }

    h5 {
        text-align: center;
        margin: 16px 0 8px;
        font-weight: bold;
    }
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

const buildQuery = gql`
  query QueryBuildContent($sku: String!) {
    build(sku: $sku) {
      sku name image
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
</script>
