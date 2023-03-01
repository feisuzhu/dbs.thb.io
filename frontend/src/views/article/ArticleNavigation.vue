<template>
  <nav class="sticky-top">
    <div class="container">
      <div class="row">
        <div class="col-auto">
          <a class="icon" href="#" @click="$router.back()">
            <icon-delete-left />
          </a>
        </div>
        <div class="col-auto category">{{ props.category }}</div>
        <div class="col title">{{ props.title }}</div>
        <div class="col-auto category invisible d-none d-sm-block">{{ props.category }}</div>
        <div class="col-auto invisible d-none d-sm-block"><a class="icon"></a></div>
      </div>
    </div>
  </nav>
</template>

<style lang="scss">
  @import "bootstrap/scss/functions";
  @import "bootstrap/scss/variables";
  @import "bootstrap/scss/mixins";

  nav {
    .category {
      color: #666;
      font-size: 0.8em;
      font-weight: bold;
      text-decoration: none;
      @include media-breakpoint-up(sm) {
        font-size: 0.9em;
      }
      white-space: nowrap;
    }

    .title {
      color: white;
      font-size: 0.9em;
      text-align: center;
      font-weight: bold;
      text-decoration: none;
      overflow: hidden;
      @include media-breakpoint-up(sm) {
        font-size: 1em;
      }
    }

  }
</style>

<script setup>
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component'
import { RouterLink } from 'vue-router'
import gql from 'graphql-tag'

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  category: {
    type: String,
    required: true
  }
});

</script>
