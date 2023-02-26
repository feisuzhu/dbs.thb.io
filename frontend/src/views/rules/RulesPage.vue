<template>
  <ApolloQuery :query="pageQuery" :variables="{ slug: $route.params.page }" tag="">
    <template v-slot="{ result: { data, error }, isLoading }">
      <Navigation />
      <div class="container page-content">
        <article v-html="data.page.article.content" v-if="!isLoading && !error">
        </article>
      </div>
    </template>
  </ApolloQuery>
</template>

<style lang="scss">
  .page-content {
    max-width: 900px;
    margin-top: 20px;
  }
</style>

<script setup>
import Navigation from './Navigation.vue'
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component'
import gql from 'graphql-tag'
import { RouterLink } from 'vue-router'

const pageQuery = gql`
  query PageQuery($slug: String!) {
    page: articleCategory(slug: "page") {
      article(slug: $slug) {
        content
      }
    }
  }
`;
</script>
