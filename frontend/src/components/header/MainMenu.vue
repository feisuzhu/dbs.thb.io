<template>
  <div class="main-menu">
    <ul :class="flavor">
      <li><router-link class="item-link" to="/">首页</router-link></li>
      <li><router-link class="item-link" to="/works">符卡</router-link></li>
      <li><router-link class="item-link" to="/rules">规则</router-link></li>
      <li><router-link class="item-link" to="/articles">公告</router-link></li>
      <li><router-link class="item-link" to="/contacts">社区</router-link></li>
    </ul>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

const props = defineProps({
  flavor: {
    type: String,
  }
});
</script>

<style lang="scss">
  .main-menu {
    margin: 12px 0 6px;

    ul {
      padding: 0;
    }

    ul li {
      display: inline-block;
      margin: 0 10px;
      padding: 0;
    }

    a.item-link {
      text-decoration: none;
      cursor: pointer;
      line-height: 18px;
      font-family: Microsoft Yahei,simsun;
      font-weight: 800;
      font-size: 16px;
      text-shadow: none;
      padding: 0;
      text-align: left;

      &:hover {
        text-decoration: underline;
      }

      &.router-link-active {
        text-decoration: underline;
      }
    }

    .header a {
      color: #313131;
      &:hover {
        color: #313131;
      }
    }

    .footer a {
      color: #646464;
      &:hover {
        color: #808080;
      }
    }
  }
</style>
