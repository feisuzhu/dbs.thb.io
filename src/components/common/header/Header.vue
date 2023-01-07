<template>
  <ApolloQuery :query="headerQuery">
    <template v-slot="{ result: { data, error }, isLoading }">
      <header class="page-header">
        <div class="container">
          <div class="row">
            <div class="col-4">
              <div class="logo"><a href="/"><img :src="isLoading ? '' : data.landing.logo" alt="" /></a></div>
            </div>
            <div class="col"></div>
            <div class="col-4 align-self-end">
              <OutboundLinks :links="isLoading ? [] : data.outboundLinks" />
              <MainMenu />
            </div>
          </div>
        </div>
      </header>
    </template>
  </ApolloQuery>
</template>

<script setup>
import OutboundLinks from '@/components/common/links/OutboundLinks.vue'
import MainMenu from '@/components/common/header/MainMenu.vue'
import gql from 'graphql-tag'

const headerQuery = gql`
  query Header {
    landing {
      logo
    }
    outboundLinks {
      id name icon mono url
    }
  }
`;
</script>

<style lang="scss">
header.page-header {
    border-top: 5px solid #d00b01;
    padding: 36px 0 21px;

    .logo img {
      width: 277px;
      height: 65px;
    }
}
</style>
