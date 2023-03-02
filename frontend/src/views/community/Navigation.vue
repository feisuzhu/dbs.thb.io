<template>
  <nav class="sticky-top">
    <div class="container">
      <div class="row">
        <div class="col-auto">
          <a class="icon" href="#" @click="$router.back()">
            <icon-delete-left />
          </a>
        </div>
        <div class="col nav-links">
          <a></a>
          <router-link to="/community">在线社群</router-link>
          <router-link to="/shop">店铺信息</router-link>
          <router-link to="/deck">卡组分享</router-link>
          <a class="d-none d-sm-block"></a>
        </div>
        <div class="col-auto">
          <a class="icon"></a>
        </div>
      </div>
    </div>
  </nav>
</template>

<style lang="scss">
  @import "bootstrap/scss/functions";
  @import "bootstrap/scss/variables";
  @import "bootstrap/scss/mixins";

  nav {
    .nav-links {
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 18pt;
      a {
        flex: 1 0 auto;
        color: #666;
        font-size: 0.8em;
        font-weight: bold;
        text-decoration: none;
        text-align: center;
        &.router-link-active {
          color: white;
          font-size: 0.9em;
        }

        @include media-breakpoint-up(sm) {
          font-size: 0.9em;
          &.router-link-active {
            font-size: 1em;
          }
        }
      }
    }
  }
</style>

<script setup>
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component'
import { RouterLink } from 'vue-router'
</script>
