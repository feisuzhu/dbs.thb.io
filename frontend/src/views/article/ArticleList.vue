<template>
  <ApolloQuery :query="articlesQuery" :variables="{ category: $route.params.category, reverse }" tag="">
    <template v-slot="{ result: { data, error }, isLoading }">
      <ListNavigation />
      <div class="container articles" v-if="!isLoading && !error">
        <a class="sorting" @click="reverse = !reverse">
          <ArrowDownAZ v-if="!reverse" />
          <ArrowDownZA v-if="reverse" />
          发布时间
        </a>
        <template v-for="(article, idx) in (data.articles || data.category.articles)">
          <div class="row article-entry">
            <div class="col-12 col-md-4 cover" v-if="article.image">
              <img :src="article.image">
            </div>
            <div class="col content">
              <span class="category h5">{{ article.category.name }}</span>
              <router-link class="title" :to="`/articles/${article.category.slug}/${article.slug}`">
                <h3>{{ article.title }}</h3>
              </router-link>
              <div class="date">{{ dayjs(article.createdAt).format('LL') }}</div>
              <div class="excerpt">{{ article.content }}</div>
            </div>
          </div>
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

  .articles {
    padding: 0 20px;

    @include media-breakpoint-up(sm) {
      padding: 0 60px;
    }

    a.sorting {
      height: 24px;
      display: block;
      line-height: 24px;
      width: max-content;
      color: #666;
      text-decoration: none;
      font-size: 20px;
      margin: 24px auto;
      cursor: pointer;

      svg {
        margin: 0;
        height: 24px;
        path {
          fill: currentColor;
        }
      }
    }

    .article-entry {
      .cover {
        aspect-ratio: 2.3;
        img {
          width: 100%;
          object-fit: cover;
          border-radius: 12px;
        }
      }

      .category {
        font-weight: bold;
        margin-right: 6px;
      }

      .title {
        @include media-breakpoint-up(sm) {
          margin-right: 10px;
        }
        color: var(--dbs-red);
        text-decoration: none;

        h3 {
          display: inline;
          font-weight: bold;
        }
      }

      .date {
        font-style: italic;
        color: #666;
      }

      .excerpt {
        margin-top: 10px;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
      }
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
import ListNavigation from './ListNavigation.vue'
import ArrowDownAZ from '@/assets/fa-arrow-down-a-z.svg?component'
import ArrowDownZA from '@/assets/fa-arrow-down-z-a.svg?component'
import gql from 'graphql-tag'
import { RouterLink } from 'vue-router'
import dayjs from 'dayjs'
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'


const route = useRoute();
const reverse = ref(true);


const articlesQuery = computed(() => {
  if (route.params.category) {
    return gql`
      query ArticlesQuery($reverse: Boolean!, $category: String!) {
        category: articleCategory(slug: $category) {
          articles(reverse: $reverse) {
            slug
            title
            content(type: EXCERPT)
            image
            createdAt
            category {
              name slug
            }
          }
        }
      }
    `;
  } else {
    return gql`
      query AllArticlesQuery($reverse: Boolean!) {
        articles(reverse: $reverse) {
          slug
          title
          content(type: EXCERPT)
          image
          createdAt
          category {
            name slug
          }
        }
      }
    `;
  }
});
</script>
