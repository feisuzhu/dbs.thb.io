import Vue from 'vue'
import VueRouter from 'vue-router'
import Vue2Filters from 'vue2-filters'

import List from 'view/List.vue'
import MainPage from 'view/MainPage.vue'
import Blog from 'view/Blog.vue'

import HeaderSection from 'components/common/header/Header.vue'
import FooterSection from 'components/common/footer/Footer.vue'

import 'jessica/css/bootstrap.css'
import 'jessica/css/bootstrap-responsive.css'
import 'jessica/css/theme.css'

import 'index.html'


Vue.use(VueRouter);
Vue.use(Vue2Filters);

var app = new Vue({
  el: '#app',
  router: new VueRouter({
    routes: [
      {path: '/', component: MainPage},
      {path: '/list', component: List},
      {path: '/blog', component: Blog},
    ],
  }),
  components: { HeaderSection, FooterSection },
});
