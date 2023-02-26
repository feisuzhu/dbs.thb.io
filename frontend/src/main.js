import dayjs from 'dayjs'
import { ApolloClient, InMemoryCache } from '@apollo/client/core'
import { createApolloProvider } from '@vue/apollo-option'
import VueApolloComponents from '@vue/apollo-components'
import { DefaultApolloClient } from "@vue/apollo-composable";
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './main.scss'

import localizedFormat from 'dayjs/plugin/localizedFormat'
import zh from 'dayjs/locale/zh-cn'
dayjs.extend(localizedFormat)
dayjs.locale(zh)

import * as bootstrap from 'bootstrap'

const cache = new InMemoryCache({
    // https://github.com/apollographql/apollo-client/issues/7648
    possibleTypes: {
        Card: [
            "Character",
            "Spellcard",
        ],
        Collection: [
            "Build",
            "Episode",
        ]
    }
});

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
