import Vue from 'vue'
import VueRouter from 'vue-router'
import Vue2Filters from 'vue2-filters'

import About from 'view/About.vue'
import Blog from 'view/Blog.vue'
import Contacts from 'view/Contacts.vue'
import Episodes from 'view/Episodes.vue'
import Library from 'view/Library.vue'
import List from 'view/List.vue'
import MainPage from 'view/MainPage.vue'
import Rules from 'view/Rules.vue'
import Story from 'view/Story.vue'

import HeaderSection from 'components/common/header/Header.vue'
import FooterSection from 'components/common/footer/Footer.vue'

import 'jessica/css/bootstrap.css'
import 'jessica/css/bootstrap-responsive.css'
import 'jessica/css/theme.css'
import 'jessica/css/jquery.mmenu.css'

import 'index.html'


Vue.use(VueRouter);
Vue.use(Vue2Filters);

require('data/cards.loader.json');
var history = require('connect-history-api-fallback');

var app = new Vue({
  el: '#app',
  router: new VueRouter({
    routes: [
      {path: '/',         component: MainPage},
      {path: '/blog',     component: Blog},
      {path: '/contacts', component: Contacts},
      {path: '/episodes', component: Episodes},
      {path: '/library',  component: Library},
      {path: '/list',     component: List},
      {path: '/list/:id', component: List},
      {path: '/rules',    component: Rules},
      {path: '/story',    component: Story},

    ],
    scrollBehavior (to, from, savedPosition) {
      return { x: 0, y: 0 }
    }
  }),
  components: { HeaderSection, FooterSection },
});
