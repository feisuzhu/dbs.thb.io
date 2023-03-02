import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/',                   component: import('@/views/landing/Landing.vue')},
    {path: '/works',              component: import('@/views/Works.vue')},
    {path: '/:page(rules)',       component: import('@/views/rules/RulesPage.vue')},
    {path: '/:page(vocabulary)',  component: import('@/views/rules/RulesPage.vue')},
    {path: '/changelog',          component: import('@/views/rules/ChangeLog.vue')},
    {path: '/articles',           component: import('@/views/article/ArticleList.vue')},
    {path: '/articles/:category', component: import('@/views/article/ArticleList.vue')},
    {path: '/articles/:category/:slug', component: import('@/views/article/Article.vue')},

    {path: '/community',          component: import('@/views/community/Community.vue')},
    {path: '/shop',               component: import('@/views/community/Shop.vue')},

    // {path: '/about',    component: import('@/views/About.vue')},
    // {path: '/blogs',    component: import('@/views/BlogList.vue')},
    // {path: '/blog/:id', component: import('@/views/Blog.vue')},
    // {path: '/rules',    component: import('@/views/Rules.vue')},
    // {path: '/story',    component: import('@/views/Story.vue')},

    {path: '/:sku',         component: import('@/views/Collection.vue')},
    {path: '/:col/:sku',    component: import('@/views/card/Card.vue')},
  ]
})

export default router
