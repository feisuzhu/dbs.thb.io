<template>
  <svg :viewBox="`${-width / 2} -12 ${width} 24`">
    <text x="0" y="0">{{ text }}</text>
  </svg>
</template>

<script setup>
import { computed } from 'vue';
const props = defineProps({
  text: {
    type: String,
  }
});

const AsciiWidth = 0.60;
const width = computed(() => {
  return 16 * Array
    .from(props.text)
    .map(a => !/\p{ASCII}/u.test(a) * (1 - AsciiWidth) + AsciiWidth)
    .reduce((a, v) => a + v, 0);
})

</script>

<style lang="scss" scoped>
  svg text {
    dominant-baseline:middle;
    text-anchor:middle;
    font-size: 16px;
    font-weight: bold;
  }
</style>
