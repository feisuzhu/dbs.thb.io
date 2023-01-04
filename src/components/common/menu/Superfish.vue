<template>
  <ul ref="menu" class="sf-menu">
    <slot />
  </ul>
</template>

<script setup>
/* import 'superfish'; */
import { ref, onMounted } from 'vue';

const menu = ref(null);
/* onMounted(() => $(menu.value).superfish()); */
</script>
