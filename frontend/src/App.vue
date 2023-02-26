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
      &:nth-child(even) > div { float: left; }
      &:nth-child(odd) > div { float: right; }
    }
  }

  .twin-center-text {
    @include media-breakpoint-up(lg) {
      &:nth-child(even) { text-align: left; }
      &:nth-child(odd)  { text-align: right; }
    }
    @include media-breakpoint-down(lg) {
      text-align: center;
    }
  }

  nav {
    --nav-height: 48px;

    background-color: #1e1e1e;
    height: var(--nav-height);
    line-height: var(--nav-height);
    font-family: "404";
    font-size: 16pt;
    color: white;

    a.icon, i {
      color: white;
      display: block;
      width: calc(var(--nav-height) - 16px);
      height: var(--nav-height);
      text-align: center;
      font-size: calc(var(--nav-height) / 2);
      vertical-align: middle;

      svg {
        padding: 12px 0;
        margin: 0 auto;
        display: block;
        height: 100%;
        path {
          fill: currentColor;
        }
      }
    }

    a:hover {
      color: white;
    }
  }

</style>
