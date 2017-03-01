import Vue from 'vue'
import VueRouter from 'vue-router'

import List from 'view/List.vue'

import HeaderSection from 'components/common/Header.vue'
import FooterSection from 'components/common/Footer.vue'

import 'index.html'
import 'jessica/css/bootstrap.css'
import 'jessica/css/bootstrap-responsive.css'
import 'jessica/css/camera.css'
import 'jessica/css/docs.css'
import 'jessica/css/prettyPhoto.css'
import 'jessica/css/theme.css'

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
