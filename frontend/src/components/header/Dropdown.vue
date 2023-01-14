<template>
  <div class="dropdown menu-item">
    <router-link class="header" :to="to" @mouseover="shouldShow = true" @mouseleave="shouldShow = false">{{ name }}</router-link>
    <ul class="dropdown-menu" :class="{ show: shouldShow }">
      <slot />
    </ul>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { ref, defineProps } from 'vue';

const shouldShow = ref(false);
const props = defineProps({
  name: String,
  to: String,
});
</script>
