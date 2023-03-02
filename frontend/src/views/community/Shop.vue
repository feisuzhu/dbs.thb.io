<template>
  <ApolloQuery :query="pageQuery" :variables="{ slug: $route.params.page }" tag="">
    <template v-slot="{ result: { data, error }, isLoading }">
      <Navigation />
      <div class="container shop-container">
        <template v-for="info in Array(10).fill(data.infoBlocks).flat()" v-if="!isLoading && !error">
          <hr>
          <div class="row shop-block">
            <div class="image col-12 col-md-5 order-md-2">
              <img :src="info.image" />
            </div>
            <div class="info col-12 col-md-7 order-md-1">
              <div>
                <span class="type">{{ info.type }}</span>
                <span class="title">{{ info.title }}</span>
              </div>
              <div class="subtitle">{{ info.subtitle }}</div>
              <div class="description">{{ info.description }}</div>
              <div class="buttons">
                <a class="button" v-for="btn in info.buttons" :style="`background-color: ${btn.color || 'black'}`" :href="btn.url">{{ btn.title }}</a>
              </div>
            </div>
          </div>
        </template>
      </div>
    </template>
  </ApolloQuery>
</template>

<style lang="scss">
  @import "bootstrap/scss/functions";
  @import "bootstrap/scss/variables";
  @import "bootstrap/scss/mixins";
  .shop-container {
    min-height: 80vh;
    hr {
      margin: 0;
    }
    @include media-breakpoint-up(lg) {
      max-width: 1050px;
    }

    .shop-block {
      font-size: 14pt;

      @include media-breakpoint-up(lg) {
        font-size: 18pt;
      }

      display: flex;
      align-items: start;
      padding: 0 1.5em;
      margin-top: 2em;
      margin-bottom: 2em;

      .info {
        flex: 1 0 auto;
        position: relative;
        margin: 15px 0 0 0;
        @include media-breakpoint-up(lg) {
          margin: 0;
        }

        .type {
          font-size: 0.8em;
          font-weight: bold;
          margin-right: 0.5em;
        }
        .title {
          font-size: 1em;
          font-weight: bold;
          color: var(--dbs-red);
        }
        .subtitle {
          font-size: 0.8em;
          color: #666;
          font-style: italic
        }
        .description {
          font-size: 0.7em;
        }
        .buttons {
          margin-top: 8px;
        }
        .button {
          display: inline-block;
          font-size: 0.7em;
          margin: 0 0.5em 0 0;
          padding: 0.2em 1em;
          text-decoration: none;
          cursor: pointer;
          color: white;
          svg {
            height: 0.8em;
            margin: 3px 0.4em 3px 0;
            fill: currentColor;
          }
        }
      }
      .image {
        img {
          width: 100%;
          aspect-ratio: 2.28;
          height: 100%;
          border-radius: 15px;
          object-fit: cover;
        }
      }
    }
  }

</style>

<script setup>
import Navigation from './Navigation.vue'
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component'
import gql from 'graphql-tag'
import { RouterLink } from 'vue-router'

const pageQuery = gql`
  query Communities {
    infoBlocks(category: SHOP) {
      type title subtitle
      description image
      buttons {
        title color url
      }
    }
  }
`;
</script>
