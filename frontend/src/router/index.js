import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(''),
  routes: [
    {path: '/',                   component: () => import('@/views/landing/Landing.vue')},
    {path: '/works',              component: () => import('@/views/Works.vue')},
    {path: '/:page(rules)',       component: () => import('@/views/rules/RulesPage.vue')},
    {path: '/:page(vocabulary)',  component: () => import('@/views/rules/RulesPage.vue')},
    {path: '/:page(faq)',         component: () => import('@/views/rules/RulesPage.vue')},
    {path: '/articles',           component: () => import('@/views/article/ArticleList.vue')},
    {path: '/articles/:category', component: () => import('@/views/article/ArticleList.vue')},
    {path: '/articles/:category/:slug', component: () => import('@/views/article/Article.vue')},

    {path: '/community',          component: () => import('@/views/community/Community.vue')},
    {path: '/shop',               component: () => import('@/views/community/Shop.vue')},

    {path: '/:sku',               component: () => import('@/views/Collection.vue')},

    { path: '/:pathMatch(.*)', redirect: '/' }
  ]
})

export default router
