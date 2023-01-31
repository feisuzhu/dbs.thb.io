import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/',             component: import('@/views/landing/Landing.vue')},
    {path: '/works',        component: import('@/views/works/Works.vue')},
    {path: '/about',        component: import('@/views/About.vue')},
    {path: '/blogs',        component: import('@/views/BlogList.vue')},
    {path: '/blog/:id',     component: import('@/views/Blog.vue')},
    {path: '/library',      component: import('@/views/Library.vue')},
    {path: '/list',         component: import('@/views/List.vue')},
    {path: '/list/:id',     component: import('@/views/List.vue')},
    {path: '/rules',        component: import('@/views/Rules.vue')},
    {path: '/story',        component: import('@/views/Story.vue')},
    {path: '/:colType(build|episode)/:sku',   component: import('@/views/works/Collection.vue')},
  ]
})

export default router
