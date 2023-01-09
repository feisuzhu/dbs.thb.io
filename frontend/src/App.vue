<template>
  <Header />
  <RouterView />
  <Footer />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from '@/components/common/header/Header.vue'
import Footer from '@/components/common/header/Footer.vue'
</script>

