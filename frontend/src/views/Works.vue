<template>
  <Navigation />
</template>

<style lang="scss">
</style>

<script setup>
import Navigation from '@/components/common/nav/Navigation.vue'
import gql from 'graphql-tag'

const worksQuery = gql`
  query Works {
  }
`;
</script>   
