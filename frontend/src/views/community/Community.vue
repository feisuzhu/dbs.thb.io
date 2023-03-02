<template>
  <ApolloQuery :query="pageQuery" :variables="{ slug: $route.params.page }" tag="">
    <template v-slot="{ result: { data, error }, isLoading }">
      <Navigation />
      <div class="container community-container">
        <div class="row">
          <template v-for="info in data.infoBlocks" v-if="!isLoading && !error">
            <hr>
            <div class="community-block col-12 col-md-6">
              <div class="grouper">
                <div class="info">
                  <div class="decoupler">
                    <div>
                      <span class="type">{{ info.type }}</span>
                      <span class="title">{{ info.title }}</span>
                    </div>
                    <div class="subtitle">{{ info.subtitle }}</div>
                    <div class="description">{{ info.description }}</div>
                    <div class="buttons">
                      <a class="button" v-for="btn in info.buttons" :style="`background-color: ${btn.color || 'black'}`" :href="btn.url"><IconSharpPlus />{{ btn.title }}</a>
                    </div>
                  </div>
                </div>
                <div class="image">
                  <img :src="info.image" />
                </div>
              </div>
            </div>
          </template>
        </div>
      </div>
    </template>
  </ApolloQuery>
</template>

<style lang="scss">
  @import "bootstrap/scss/functions";
  @import "bootstrap/scss/variables";
  @import "bootstrap/scss/mixins";
  .community-container {
    min-height: 80vh;
  }

  .community-block {
    font-size: 14pt;

    @include media-breakpoint-up(lg) {
      font-size: 18pt;
    }

    display: flex;
    aspect-ratio: 2;
    align-items: center;
    padding: 0 1.5em;
    --split: 76%;

    .grouper {
      width: 100%;
      display: flex;
    }

    .info {
      flex: 1 0 auto;
      width: var(--split);
      position: relative;
      .decoupler {
        position: absolute;
        height: 100%;
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
      flex: 0 0 auto;
      width: calc(100% - var(--split));
      img {
        width: 100%;
      }
    }
  }
  hr {
    margin: 0;
  }
  @include media-breakpoint-up(md) {
    hr:nth-child(4n+3), hr:nth-child(1) {
      display: none !important;
    }
  }
</style>

<script setup>
import Navigation from './Navigation.vue'
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component'
import IconSharpPlus from '@/assets/fa-sharp-regular-plus.svg?component'
import gql from 'graphql-tag'
import { RouterLink } from 'vue-router'

const pageQuery = gql`
  query Communities {
    infoBlocks(category: COMMUNITY) {
      type title subtitle
      description image
      content
      buttons {
        title color url
      }
    }
  }
`;
</script>
