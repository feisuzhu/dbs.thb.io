<template>
  <ApolloQuery :query="headerQuery" tag="">
    <template v-slot="{ result: { data, error }, isLoading }">
      <header class="page-header">
        <div class="container">
          <div class="row">
            <div class="col-lg-4">
              <div class="logo text-center text-lg-start"><a href="/"><img :src="isLoading ? '' : data.landing.logo" alt="" /></a></div>
            </div>
            <div class="col-lg"></div>
            <div class="text-center text-lg-end col-lg-4">
              <OutboundLinks />
              <MainMenu flavor="header" />
            </div>
          </div>
        </div>
      </header>
    </template>
  </ApolloQuery>
</template>

<script setup>
import OutboundLinks from './OutboundLinks.vue'
import MainMenu from './MainMenu.vue'
import gql from 'graphql-tag'

const headerQuery = gql`
  query Header {
    landing {
      logo
    }
  }
`;
</script>

<style lang="scss">
header.page-header {
    border-top: 5px solid var(--dbs-red);
    padding: 36px 0 21px;

    .logo img {
      width: 277px;
      height: 65px;
      margin: 0 0 21px;
    }
}
</style>
