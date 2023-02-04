import { ApolloClient, InMemoryCache } from '@apollo/client/core'
import { createApolloProvider } from '@vue/apollo-option'
import VueApolloComponents from '@vue/apollo-components'
import { DefaultApolloClient } from "@vue/apollo-composable";
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './main.scss'

import * as bootstrap from 'bootstrap'

const cache = new InMemoryCache()
const apolloClient = new ApolloClient({
  cache,
  uri: '/graphql',
})

const apolloProvider = createApolloProvider({
  defaultClient: apolloClient,
})

// ----- app -----
const app = createApp(App)

app.use(router)
app.use(apolloProvider)
app.use(VueApolloComponents)
app.provide(DefaultApolloClient, apolloClient)

app.mount('#app')
