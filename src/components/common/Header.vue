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
                                    <li><a href="https://projectzephyr.taobao.com/" class="taobao">taobao</a></li>
                                    <li><a href="http://weibo.com/hxmdf" class="weibo">weibo</a></li>
                                    <li><a href="http://shang.qq.com/wpa/qunwpa?idkey=01adf7b2febd09c239255418f5ba7293cff0f448c10bd6b7896cc9bcd9997afc" class="qq">qq</a></li>
                                    <li><a href="http://www.allcpp.cn/organize.aspx?circleid=3071" class="cpp">cpp</a></li>
                                    <li><a href="http://zhuanlan.zhihu.com/irinwind" class="zhihu">zhihu</a></li>
                                </ul>
                            </div>
                            <div class="clear"></div>
                            <nav id="main_menu">
                                <div class="menu_wrap">
                                    <superfish class="nav">
                                      <li><a href="#">首页</a></li>
                                      <li><a href="#about">简介</a></li>
                                      <li class="sub-menu"><a href="#/episodes">作品</a>
                                          <ul>
                                            <li v-for="ep in episodes">
                                              <router-link :to="'/episodes/' + ep.id"><span>-</span>{{ ep.title }}</router-link>
                                            </li>
                                          </ul>
                                      </li>
                                      <li class="sub-menu"><a href="#">资料</a>
                                           <ul>
                                              <li><a href="#list"><span>-</span>符卡资料</a></li>
                                              <li><a href="#rules"><span>-</span>决斗规则</a></li>
                                              <li><a href="#story"><span>-</span>符梦传说</a></li>
                                          </ul>
                                      </li>
                                      <li><a href="#blog">公告</a>
                                      </li>
                                      <li><a href="#contacts">社团</a></li>
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
