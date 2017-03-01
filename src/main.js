import Vue from 'vue'
import VueRouter from 'vue-router'

import List from 'view/List.vue'

import HeaderSection from 'components/common/Header.vue'
import FooterSection from 'components/common/Footer.vue'

import 'index.html'
import 'css/bootstrap.css'
import 'css/bootstrap-responsive.css'
import 'css/camera.css'
import 'css/docs.css'
import 'css/prettyPhoto.css'
import 'css/theme.css'

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
