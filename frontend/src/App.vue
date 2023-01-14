<template>
  <Header />
  <RouterView />
  <Footer />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from '@/components/header/Header.vue'
import Footer from '@/components/header/Footer.vue'
</script>

