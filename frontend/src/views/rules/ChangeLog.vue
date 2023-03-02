<template>
  <ApolloQuery :query="changelogQuery" :variables="{ slug: $route.params.page }" tag="">
    <template v-slot="{ result: { data, error }, isLoading }">
      <Navigation />
      <div class="container changelog-content" v-if="!isLoading && !error">
        <template v-for="(article, idx) in data.changelog.articles">
          <h4>{{ article.title }}</h4><div class="date">{{ dayjs(article.createdAt).format('LL') }}</div>
          <article v-html="article.content"></article>
          <hr>
        </template>
      </div>
    </template>
  </ApolloQuery>
</template>

<style lang="scss">
  @import "bootstrap/scss/functions";
  @import "bootstrap/scss/variables";
  @import "bootstrap/scss/mixins";

  .changelog-content {
    margin-top: 20px;
    padding: 0 20px;

    @include media-breakpoint-up(sm) {
      margin-top: 60px;
      padding: 0 60px;
    }

    h4 {
      @include media-breakpoint-up(sm) {
        display: inline;
        margin-right: 10px;
      }
      font-weight: bold;
      color: var(--dbs-red);
    }

    .date {
      display: inline;
      font-style: italic;
      color: #666;
    }

    article {
      margin-top: 10px;
    }

    hr {
      margin: 30px 0;
    }

    hr:last-child {
      display: none;
    }
  }
</style>

<script setup>
import Navigation from './Navigation.vue'
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component'
import gql from 'graphql-tag'
import { RouterLink } from 'vue-router'
import dayjs from 'dayjs'

const changelogQuery = gql`
  query ChangelogQuery {
    changelog: articleCategory(slug: "changelog") {
      articles(reverse: true) {
        title
        content
        createdAt
      }
    }
  }
`;
</script>
