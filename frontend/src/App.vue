<template>
  <Header />
  <RouterView />
  <Footer />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from '@/components/header/Header.vue'
import Footer from '@/components/header/Footer.vue'
</script>

<style lang="scss">
  @import "bootstrap/scss/functions";
  @import "bootstrap/scss/variables";
  @import "bootstrap/scss/mixins";

  @font-face {
    font-family: "404";
    src: url(@/assets/404-CAI978.ttf) format("truetype");
  }

  .twin-center {
    @include media-breakpoint-up(lg) {
      &:nth-child(even) {
        text-align: left;
        & > div {
            float: left;
        }
      }
      &:nth-child(odd) {
        text-align: right;
        & > div {
            float: right;
        }
      }
    }
    @include media-breakpoint-down(lg) {
      text-align: center;
    }
  }
</style>
