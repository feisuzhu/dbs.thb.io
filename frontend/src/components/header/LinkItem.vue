<template>
  <li class="outbound-link-item">
    <a :href="link.url" :alt="link.name" target="_blank" @mouseover="isActive = true" @mouseleave="isActive = false">
      <img :src="link.mono" :alt="link.name" :class="{ active: !isActive }" />
      <img :src="link.icon" :alt="link.name" :class="{ active: isActive }" />
    </a>
  </li>
</template>

<style lang="scss">
  .outbound-link-item {
      padding: 0;
      margin: 0px 3px 0px 3px;
      display: inline-block;
      height: 30px;
      width: 30px;
      line-height: 30px;
      position: relative;

      a {
          height: 30px;
          width: 30px;
          display: block;
      }

      img {
          position: absolute;
          top: 0px;
          left: 0px;
          height: 30px;
          width: 30px;

          transition-duration: 0.2s;
          transition-timing-function: ease-in;

          opacity: 0;
      }

      img.active {
          opacity: 1;
          transition-duration: 0s;
      }
  }
</style>

<script setup>
import { ref } from 'vue'
import gql from 'graphql-tag'

const isActive = ref(false);

const props = defineProps({
  link: {
    type: Object,
    required: true
  }
});
</script>
