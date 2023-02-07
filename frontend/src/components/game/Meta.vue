<template>
  <div class="meta">
    <p class="pad"></p>
    <p>画师：{{ version.illustrator.name }}</p>
    <p v-if="version.episode">从 {{ version.episode.sku }} 获得</p>
    <p class="pad"></p>
  </div>
</template>

<script setup>
const props = defineProps({
  version: {
    type: Object,
  }
});
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
