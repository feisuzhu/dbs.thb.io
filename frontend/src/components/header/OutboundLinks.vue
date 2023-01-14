<template>
  <ApolloQuery :query="linksQuery" tag="">
    <template v-slot="{ result: { data, error }, isLoading }">
      <div class="outbound-links">
        <ul v-if="!isLoading">
          <LinkItem v-for="link in data.outboundLinks" :key="link.id" :link="link" />
        </ul>
      </div>
    </template>
  </ApolloQuery>
</template>

<style lang="scss">
  .outbound-links {
      margin: 0px 3px 6px;

      ul {
        list-style: none;
        margin: 0;
        padding: 0;
      }
  }
</style>

<script setup>
import gql from 'graphql-tag'
import LinkItem from './LinkItem.vue'

const linksQuery = gql`
  query OutboundLinks {
    outboundLinks {
      id name icon mono url
    }
  }
`;
</script>
