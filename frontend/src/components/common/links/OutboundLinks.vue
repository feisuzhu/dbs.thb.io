<template>
  <div class="outbound-links">
    <ul>
      <LinkItem v-for="link in links" :key="link.id" :link="link" />
    </ul>
  </div>
</template>

<style lang="scss">
  .outbound-links {
      text-align: right;
      padding: 3px 4px 9px 0;

      ul {
        list-style: none;
        margin: 0;
        padding: 0;
      }
  }
</style>

<script setup>
import gql from 'graphql-tag'
import LinkItem from '@/components/common/links/LinkItem.vue'

const props = defineProps({
  links: {
    type: Array,
    required: true
  }
});
</script>
