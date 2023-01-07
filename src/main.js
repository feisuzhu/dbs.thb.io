import { ApolloClient, InMemoryCache } from '@apollo/client/core'
import { createApolloProvider } from '@vue/apollo-option'
import VueApolloComponents from '@vue/apollo-components'
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

const app = createApp(App)

app.use(router)
app.use(apolloProvider)
app.use(VueApolloComponents)

app.mount('#app')
