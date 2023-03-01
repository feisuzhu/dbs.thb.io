<template>
  <ApolloQuery :query="articleQuery" :variables="{ category: $route.params.category, slug: $route.params.slug }" tag="">
    <template v-slot="{ result: { data, error }, isLoading }">
      <ArticleNavigation :category="data?.category.name" :title="data?.category.article.title" />
      <article class="container article" v-if="!isLoading && !error">
        <div class="cover" v-if="data.category.article.image">
          <img :src="data.category.article.image">
        </div>
        <div class="date">{{ dayjs(data.category.article.createdAt).format('LL') }}</div>
        <div class="content" v-html="data.category.article.content"></div>
      </article>
    </template>
  </ApolloQuery>
</template>

<style lang="scss">
  @import "bootstrap/scss/functions";
  @import "bootstrap/scss/variables";
  @import "bootstrap/scss/mixins";

  article.article {
    padding: 0 20px;

    @include media-breakpoint-up(sm) {
      padding: 0 70px;
    }

    .cover {
      margin: 20px 0;

      @include media-breakpoint-up(sm) {
        margin: 40px 0;
      }

      display: flex;
      justify-content: center;
      align-items: center;

      img {
        width: 90%;
        height: auto;
        border-radius: 15px;

      }
    }

    .date {
      font-style: italic;
      font-size: 1.1em;
      color: #666;
    }

    .content {
      margin: 20px 0;
      img {
        max-width: 100%;
      }
    }
  }
</style>

<script setup>
import ArticleNavigation from './ArticleNavigation.vue'
import gql from 'graphql-tag'
import { RouterLink } from 'vue-router'
import dayjs from 'dayjs'
import { ref, computed } from 'vue'


const articleQuery = gql`
  query ArticleQuery($category: String!, $slug: String!) {
    category: articleCategory(slug: $category) {
      name slug
      article(slug: $slug) {
        title
        content
        image
        createdAt
      }
    }
  }
`;
</script>
