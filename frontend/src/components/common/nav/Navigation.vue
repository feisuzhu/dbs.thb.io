<template>
  <nav>
    <div class="container">
      <div class="row">
        <div class="col-md-1">
          <a href="#" @click="$router.back()">
            <fa-icon icon="fa-solid fa-delete-left" />
          </a>
        </div>
        <div class="col-md"></div>
        <div class="col-md-6 text-md-end">
          <slot />
        </div>
      </div>
    </div>
  </nav>
</template>

<style lang="scss">
nav {
  $nav-height: 48px;

  background-color: #1e1e1e;
  height: $nav-height;
  line-height: $nav-height;

  a {
    display: block;
    width: $nav-height;
    height: $nav-height;
    text-align: center;
    color: white;
    font-size: calc($nav-height / 2);
  }
}
</style>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
