<template>
  <nav id="nav" class="sticky-top">
    <div class="container">
      <div class="row">
        <div class="col-auto">
          <a href="#" @click="$router.back()">
            <icon-delete-left />
          </a>
        </div>
        <div class="col"></div>
        <slot></slot>
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
  font-family: "404";
  font-size: 16pt;
  color: white;

  a, i {
    color: white;
    display: block;
    width: calc($nav-height - 16px);
    height: $nav-height;
    text-align: center;
    font-size: calc($nav-height / 2);
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

<script setup>
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component';
import { RouterLink, RouterView } from 'vue-router'
</script>
