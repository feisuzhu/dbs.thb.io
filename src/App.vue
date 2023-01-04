<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HeaderSection from '@/components/common/header/Header.vue'
import FooterSection from '@/components/common/footer/Footer.vue'
</script>

<template>
  <HeaderSection />
  <RouterView />
  <FooterSection />
</template>
