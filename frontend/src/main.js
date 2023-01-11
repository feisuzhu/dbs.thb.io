import { ApolloClient, InMemoryCache } from '@apollo/client/core'
import { createApolloProvider } from '@vue/apollo-option'
import VueApolloComponents from '@vue/apollo-components'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
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

// ----- font awesome -----
import { faDeleteLeft } from '@fortawesome/free-solid-svg-icons'
library.add(faDeleteLeft)


// ----- app -----
const app = createApp(App)

app.use(router)
app.use(apolloProvider)
app.use(VueApolloComponents)
app.component('fa-icon', FontAwesomeIcon)

app.mount('#app')
