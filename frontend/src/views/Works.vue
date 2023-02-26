<template>
  <ApolloQuery :query="worksQuery" tag="">
    <template v-slot="{ result: { data, error }, isLoading }">
      <nav class="sticky-top">
        <div class="container">
          <div class="row">
            <div class="col-auto">
              <a class="icon" href="#" @click="$router.back()">
                <icon-delete-left />
              </a>
            </div>
            <div class="col"></div>
          </div>
        </div>
      </nav>
      <div class="container works-list" v-if="!isLoading">
        <div class="row">
          <div class="col"><h5>按构筑查询</h5></div>
        </div>
        <div class="row">
          <div class="col-lg-6 twin-center-text" v-for="(build, i) in data.builds" :key="i">
            <router-link class="icon" :to="build.sku" v-if="!build.dummy">
              <img class="work-image" :src="build.image" :alt="build.name">
            </router-link>
            <img class="work-image" :src="build.image" :alt="build.name" v-else>
          </div>
        </div>
        <div class="row">
          <div class="col"><h5>按卡包查询</h5></div>
        </div>
        <div class="row">
          <div class="col-lg-6 twin-center-text" v-for="(episode, i) in data.episodes" :key="i">
            <router-link class="icon" :to="episode.sku" v-if="!episode.dummy">
              <img class="work-image" :src="episode.image" :alt="episode.name">
            </router-link>
            <img class="work-image" :src="episode.image" :alt="episode.name" v-else>
          </div>
        </div>
      </div>
    </template>
  </ApolloQuery>
</template>

<style lang="scss">
  .works-list {
    $work-img-width: 378px;
    $work-img-height: 124px;

    margin-top: 20px;

    img.work-image {
      display: inline-block;
      max-width: 100%;
      max-height: $work-img-height;
      margin: 12px 0;
      object-fit: contain;
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
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component'
import gql from 'graphql-tag'

const worksQuery = gql`
  query Works {
    builds {
      sku name image dummy
    }
    episodes {
      sku name image dummy
    }
  }
`;
</script>
