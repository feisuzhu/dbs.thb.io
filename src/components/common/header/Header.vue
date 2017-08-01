<template>
  <!--header-->
  <div class="header">
    <div class="wrap">
      <div class="navbar navbar_ clearfix">
        <div class="container">
          <div class="row">
            <div class="span4">
              <div class="logo"><a href="index.html"><img :src="require('assets/common/logo.png')" alt="" /></a>
              </div>
            </div>
            <div class="span8">
              <div class="follow_us">
                <ul>
                  <li><a href="https://projectzephyr.taobao.com/" class="taobao">taobao</a></li>
                  <li><a href="http://weibo.com/hxmdf" class="weibo">weibo</a></li>
                  <li><a href="http://shang.qq.com/wpa/qunwpa?idkey=01adf7b2febd09c239255418f5ba7293cff0f448c10bd6b7896cc9bcd9997afc" class="qq">qq</a></li>
                  <li><a href="http://www.allcpp.cn/organize.aspx?circleid=3071" class="cpp">cpp</a></li>
                  <li><a href="http://zhuanlan.zhihu.com/irinwind" class="zhihu">zhihu</a></li>
                </ul>
              </div>
              <div class="clear"></div>
              <nav class="main_menu">
                <div class="menu_wrap">
                  <superfish class="nav">
                    <li><router-link to="/">首页</router-link></li>
                    <li class="sub-menu">
                      <router-link to="/episodes">作品</router-link>
                      <ul>
                        <li v-for="ep in episodes">
                          <router-link :to="'/episodes/' + ep.id"><span>-</span>{{ ep.title }}</router-link>
                        </li>
                      </ul>
                    </li>
                    <li class="sub-menu">
                      <router-link to="/library">资料</router-link>
                      <ul>
                        <li><router-link to="/list"><span>-</span>符卡资料</router-link></li>
                        <li><router-link to="/rules"><span>-</span>决斗规则</router-link></li>
                        <li><router-link to="/story"><span>-</span>符梦传说</router-link></li>
                      </ul>
                    </li>
                    <li><router-link to="/blogs">公告</router-link></li>
                    <li><router-link to="/contacts">社团</router-link></li>
                  </superfish>
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
<style>
@media (min-width: 1201px) {
  .menu_wrap{
      text-align:left;
      padding:0px 4% 0px 0px;
  }
}
@media (min-width: 980px) and (max-width: 1200px) {
  .menu_wrap{
      text-align:left;
      padding:0px 2% 0px 0px;
  }
}
@media (max-width: 979px) {
  .menu_wrap{
      text-align:left;
      padding:0px 33.5% 0px 0px;
  }
}
@media (max-width: 480px) {
  .menu_wrap{
      text-align:left;
      padding:0px 8% 0px 0px;
  }
}
@media (max-width: 414px) {
  .menu_wrap{
      text-align:left;
      padding:0px 12.6% 0px 0px;
  }
}
@media (max-width: 375px) {
  .menu_wrap{
      text-align:left;
      padding:0px 8.5% 0px 0px;
  }
}
@media (max-width: 360px) {
  .menu_wrap{
      text-align:left;
      padding:0px 6% 0px 0px;
  }
}
@media (max-width: 320px) {
  .menu_wrap{
      text-align:left;
      padding:0px 0px 0px 0px;
      width:105.7%
  }
}
  .follow_us {
      text-align:right;
      padding:3px 4px 9px 0;
  }

  .follow_us ul li {
      padding:0;
      margin:0 0 0 5px;
      display:inline-block;
      line-height:30px;
  }
  .follow_us a {
      background-image:url(top_socials.png);
      background-repeat:no-repeat;
      height:30px;
      width:30px;
      display:block;
      text-indent:-9999px;
      text-align:left;
  }
  .follow_us a.taobao       { background-position: 0      0;     }
  .follow_us a.taobao:hover { background-position: 0      -30px; }
  .follow_us a.weibo        { background-position: -35px  0;     }
  .follow_us a.weibo:hover  { background-position: -35px  -30px; }
  .follow_us a.qq           { background-position: -70px  0;     }
  .follow_us a.qq:hover     { background-position: -70px  -30px; }
  .follow_us a.cpp          { background-position: -105px 0;     }
  .follow_us a.cpp:hover    { background-position: -105px -30px; }
  .follow_us a.zhihu        { background-position: -140px 0;     }
  .follow_us a.zhihu:hover  { background-position: -140px -30px; }
</style>

<script>
  import Superfish from 'components/common/menu/Superfish.vue'
  export default {
    name: 'header',
    data() {
        var episodes = require('data/episodes.yaml');
        return { episodes: episodes };
    },
    components: {
      Superfish,
    },
  }
</script>
