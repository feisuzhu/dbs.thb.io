<template>
  <ApolloQuery :query="landingQuery" class="landing">
    <template v-slot="{ result: { data, error }, isLoading }">
      <!-- carousel -->
      <Carousel :slides="isLoading ? [] : data.landing.slides" />

      <!-- slogan -->
      <div class="container slogan-block" v-if="!isLoading">
        <hr class="upper">
        <p class="small">{{ data.landing.smallSlogan }}</p>
        <p class="big">{{ data.landing.bigSlogan }}</p>
        <hr class="lower">
      </div>

      <!-- works -->
      <div class="container">
        <h5 class="section-title">作品一览</h5>
        <div class="row align-items-start">
          <div class="col-sm-6 col-lg-3" v-for="work in data.landing.works" :key="work.id" v-if="!isLoading">
            <div class="work-block">
              <img :src="work.image" class="card-img-top">
              <div class="body">
                <h5 class="title">{{ work.title }}</h5>
                <h6 class="subtitle">{{ work.subtitle }}</h6>
                <p class="text">{{ work.description }}</p>
                <a :href="work.url" class="card-link">{{ work.urltext }}</a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <hr class="gap">

      <!-- columns -->
      <div class="container">
        <div class="row align-items-start">
          <div class="col-md" v-for="column in data.landing.columns" :key="column.id" v-if="!isLoading">
            <div class="column-block">
              <h5 class="title">{{ column.title }}</h5>
              <h6 class="subtitle">{{ column.subtitle }}</h6>
              <p class="text">{{ column.description }}</p>
              <a :href="column.url" class="card-link">{{ column.urltext }}</a>
            </div>
          </div>
        </div>
      </div>
    </template>
  </ApolloQuery>
</template>

<style lang="scss">
.landing a {
  text-decoration: none;
  color: var(--dbs-red);
  &:hover {
    text-decoration: underline;
  }
}

.slogan-block {
  text-align: center;
  padding: 48px 0;
  line-height: 20px;
  color: #3b3b3b;
  font-family: Microsoft Yahei,simhei;
  font-weight: 400;

  hr {
    border: 0;
    height: 1.2px;
    background: rgb(255,255,255);
    background: linear-gradient(90deg, rgba(255,255,255,1) 0%, rgba(100,100,100,1) 50%, rgba(255,255,255,1) 100%);

    &.upper { margin-bottom: 36px; }
    &.lower { margin-top: 36px; }
  }

  .small { font-size: 18px; }
  .big { font-size: 30px; }
}

.section-title {
  font-weight: bold;
}

.work-block {
  margin: 15px 0 15px 0;

  img { border-radius: 5px; }
  .body { padding-top: 14px; }
  .title { color: var(--dbs-red); font-size: 17px; }
  .subtitle { color: #9d9d9d; font-style: italic; font-size: 12px; }
  .text { font-size: 12px; margin: 0; }
  a { font-size: 12px; }
}

.gap {
  border: 0;
  margin: 50px 0 0 0;
}

.column-block {
  margin: 15px 0 15px 0;
  .title { font-weight: bold; margin-bottom: 12px; }
  .subtitle { color: #9d9d9d; font-style: italic; font-size: 12px; }
  .text { font-size: 12px; margin: 0 0 8px 0; }
  a { font-size: 17px; }
}
</style>

<script setup>
import Carousel from '@/views/landing/Carousel.vue'

import gql from 'graphql-tag'

const landingQuery = gql`
query Landing {
  landing {
    id
    smallSlogan bigSlogan
    slides {
      id image url
    }
    works {
      id image title subtitle description
      url urltext
    }
    columns {
      id title subtitle description
      url urltext
    }
  }
}
`
</script>
