<template>
  <ApolloQuery :query="categoryQuery" tag="">
    <template v-slot="{ result: { data, error }, isLoading }">
      <nav class="sticky-top">
        <div class="container">
          <div class="row">
            <div class="col-auto">
              <a class="icon" href="#" @click="$router.back()">
                <icon-delete-left />
              </a>
            </div>
            <div class="col-auto dbs-nav-link">
              <router-link to="/articles">全部</router-link>
            </div>
            <div class="col-auto dbs-nav-link" v-for="c in data.articleCategories" v-if="!isLoading && !error">
              <router-link :to="`/articles/${c.slug}`">{{ c.name }}</router-link>
            </div>
          </div>
        </div>
      </nav>
    </template>
  </ApolloQuery>
</template>

<style lang="scss">
  @import "bootstrap/scss/functions";
  @import "bootstrap/scss/variables";
  @import "bootstrap/scss/mixins";

  nav {
    .dbs-nav-link a {
      color: #666;
      font-size: 0.8em;
      font-weight: bold;
      text-decoration: none;
      text-align: center;
      &.router-link-active {
        color: white;
        font-size: 0.9em;
      }

      @include media-breakpoint-up(sm) {
        font-size: 0.9em;
        &.router-link-active {
          font-size: 1em;
        }
      }
    }
  }
</style>

<script setup>
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component'
import { RouterLink } from 'vue-router'
import gql from 'graphql-tag'

const categoryQuery = gql`
  query ArticleCategories {
    articleCategories {
      slug name
    }
  }
`;
</script>
