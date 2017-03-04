import Vue from 'vue'
import VueRouter from 'vue-router'

import List from 'view/List.vue'
import Mainpage from 'view/Mainpage.vue'

import HeaderSection from 'components/common/Header.vue'
import FooterSection from 'components/common/Footer.vue'

import 'index.html'
import 'jessica/css/bootstrap.css'
import 'jessica/css/bootstrap-responsive.css'
import 'jessica/css/camera.css'
import 'jessica/css/docs.css'
import 'jessica/css/prettyPhoto.css'
import 'jessica/css/theme.css'

/*import 'jessica/js/application.js'
import 'jessica/js/bootstrap.js'
import 'jessica/js/camera.js'
import 'jessica/js/jquery.easing.1.3.js'
import 'jessica/js/jquery.isotope.min.js'
import 'jessica/js/jquery.jcarousel.js'
import 'jessica/js/jquery.mobile.customized.min.js'
import 'jessica/js/jquery.preloader.js'
import 'jessica/js/jquery.prettyPhoto.js'
import 'jessica/js/jquery.tweet.js'
import 'jessica/js/myscript.js'
import 'jessica/js/sorting.js'
import 'jessica/js/superfish.js'
import 'jessica/js/google-code-prettify/prettify.css'
import 'jessica/js/google-code-prettify/prettify.js'*/

Vue.use(VueRouter);

var app = new Vue({
  el: '#app',
  router: new VueRouter({
    routes: [
      {path: '/list', component: List},
      {path: '/mainpage', component: Mainpage},
    ]
  }),
  components: { HeaderSection, FooterSection },
})
