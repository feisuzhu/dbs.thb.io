<template>
  <div class="meta">
    <p class="pad"></p>
    <p>画师：{{ version.illustrator.name }}</p>
    <p v-if="version.episodes.length">从 {{ episodes }} 获得</p>
    <p class="pad"></p>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  version: {
    type: Object,
  }
});

const episodes = computed(() => props.version.episodes.map(e => e.sku).join(' / '));
</script>

<style lang="scss" scoped>
  .meta {
    width: 100%;

    display: flex;
    flex-direction: column;
    width: 100%;
    vertical-align: middle;

    p {
      margin: 0;
      flex: 0 0 auto;
      text-align: center;
      color: #717171;

      &.pad {
        flex: 1 0 auto;
      }
    }
  }
</style>
