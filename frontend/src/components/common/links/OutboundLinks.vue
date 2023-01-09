<template>
  <ApolloQuery :query="linksQuery">
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
      text-align: right;
      padding: 3px 4px 9px 0;

      ul {
        list-style: none;
        margin: 0;
        padding: 0;
      }
  }
</style>

<script setup>
import gql from 'graphql-tag'
import LinkItem from '@/components/common/links/LinkItem.vue'

const linksQuery = gql`
  query OutboundLinks {
    outboundLinks {
      id name icon mono url
    }
  }
`;
</script>
