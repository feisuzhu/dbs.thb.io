<template>
  <ApolloQuery :query="footerQuery" tag="">
    <template v-slot="{ result: { data, error }, isLoading }">
      <footer class="page-footer">
        <div class="container">
          <div class="row">
            <div class="col-4">
              <div class="logo"><a href="/"><img :src="isLoading ? '' : data.landing.monologo" alt="" /></a></div>
              <pre class="text">{{ isLoading ? '' : data.landing.footer }}</pre>
            </div>
            <div class="col"></div>
            <div class="col-4">
              <OutboundLinks />
              <MainMenu flavor="footer" />
            </div>
          </div>
        </div>
      </footer>
    </template>
  </ApolloQuery>
</template>

<script setup>
import OutboundLinks from '@/components/common/links/OutboundLinks.vue'
import MainMenu from '@/components/common/header/MainMenu.vue'
import gql from 'graphql-tag'

const footerQuery = gql`
  query Footer {
    landing {
      monologo
      footer
    }
  }
`;
</script>

<style lang="scss">
  footer.page-footer {
    background-color: rgb(30, 30, 30);
    margin: 36px 0 0 0;
    padding: 36px 0 20px 0;

    .logo img {
      width: 277px;
      height: 65px;
    }

    .text {
      color: #444;
      font-size: 12px;
      font-family: "Helvetica Neue", sans-serif;
      line-height: 18px;
    }
  }
</style>
