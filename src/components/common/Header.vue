<template>
  <!--header-->
    <div class="header">
      <div class="wrap">
          <div class="navbar navbar_ clearfix">
              <div class="container">
                    <div class="row">
                        <div class="span4">
                          <div class="logo"><a href="index.html"><img :src="require('jessica/img/logo.png')" alt="" /></a></div>
                        </div>
                        <div class="span8">
                          <div class="follow_us">
                                <ul>
                                    <li><a href="#" class="facebook">Facebook</a></li>
                                    <li><a href="#" class="vimeo">Vimeo</a></li>
                                    <li><a href="#" class="tumbrl">Tumbrl</a></li>
                                    <li><a href="#" class="twitter">Twitter</a></li>
                                    <li><a href="#" class="delicious">Delicious</a></li>
                                </ul>
                            </div>
                            <div class="clear"></div>
                            <nav id="main_menu">
                                <div class="menu_wrap">
                                    <Superfish class="nav">
                                      <li class="current"><a href="index.html">Home</a></li>
                                      <li><a href="about.html">About</a></li>
                                      <li class="sub-menu"><a href="javascript:{}">Features</a>
                                          <ul>
                                              <li><a href="scaffolding.html"><span>-</span>Scaffolding</a></li>
                                              <li><a href="typography.html"><span>-</span>Typography</a></li>
                                              <li><a href="shortcodes.html"><span>-</span>Shortcodes</a></li>
                                              <li><a href="tables.html"><span>-</span>Tables</a></li>
                                          </ul>
                                      </li>
                                      <li class="sub-menu"><a href="javascript:{}">Portfolio</a>
                                           <ul>
                                              <li><a href="portfolio_2columns.html"><span>-</span>2 Columns</a></li>
                                              <li><a href="portfolio_3columns.html"><span>-</span>3 Columns</a></li>
                                              <li><a href="portfolio_4columns.html"><span>-</span>4 Columns</a></li>
                                          </ul>
                                      </li>
                                      <li class="sub-menu"><a href="javascript:{}">Blog</a>
                                           <ul>
                                              <li><a href="blog.html"><span>-</span>Blog with right sidebar</a></li>
                                              <li><a href="blog_post.html"><span>-</span>Blog post</a></li>
                                          </ul>
                                      </li>
                                      <li><a href="contacts.html">Contacts</a></li>
                                    </Superfish>
                                </div>
                             </nav>
                        </div>
                    </div>
                </div>
             </div>
        </div>
    </div>
    <!--//header-->
</template>

<script>
  import Superfish from 'components/common/menu/Superfish.vue'
  export default {
    name: 'header',
    components: {
      Superfish,
    },
  }
</script>
