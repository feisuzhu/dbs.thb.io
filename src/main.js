import Vue from 'vue'
import VueRouter from 'vue-router'

import List from 'view/List.vue'

import HeaderSection from 'components/common/Header.vue'
import FooterSection from 'components/common/Footer.vue'

import 'index.html'

Vue.use(VueRouter);

var app = new Vue({
  el: '#app',
  router: new VueRouter({
    routes: [
      {path: '/list', component: List},
    ]
  }),
  components: { HeaderSection, FooterSection },
})
