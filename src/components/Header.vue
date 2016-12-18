<template>
  <div>
    <div id="social_bar_wrapper">
      <div id="social_bar">
        <ul id="social">
          <li class="trigger"></li>
          <li class="sinaWB">
            <a href="http://weibo.com/hxmdf" target="_blank">
              <img src="ico/sina1.png" width="30" height="30" alt="sinaWB" />
            </a>
          </li>

          <li class="bbs">
            <a href="http://dbs.thbattle.net" target="_blank">
              <img src="ico/bbs1.png" width="30" height="30" alt="bbs" />
            </a>
          </li>

          <li class="tb">
            <a href="http://projectzephyr.taobao.com" target="_blank">
              <img src="ico/tb1.png" width="30" height="30" alt="tb" />
            </a>
          </li>
        </ul>
      </div>
    </div>

    <div id="menu_wrapper">
      <div id="logo_menu_wrapper">
        <div id="top_logo">
          <a href="index.html">
            <img src="img/logo.png" height="40" width="247" alt="top logo" />
          </a>
        </div>

        <div id="top_menu">
          <ul class="sf-menu">
            <li><a href="index.html">莲台野 <span>幻想的门扉</span></a></li>
            <li><a href="products.html">香霖堂 <span>得意之作</span></a></li>
            <li>
              <a class="active" href="library.html">魔法图书室 <span>资料库</span></a>
              <ul>
                <li><a href="cardlist.html">符卡图鉴</a></li>
                <li><a href="rules.html">规则集</a></li>
                <li><a href="faq.html">FAQ整理</a></li>
              </ul>
            </li>
            <li>
              <a href="contact.html">花果子念报<span>姑且算是号外</span></a>
              <ul>
                <li><a href="staff.html">制作人员</a></li>
                <li><a href="history.html">旧秘境史</a></li>
                <li><a href="blog.html">新幻想史</a></li>
              </ul>
            </li>
          </ul>
        </div>
        <div class="clear"></div>
      </div>
    </div>
  </div>
</template>


<script>
  export default {
    name: 'header',
  }
</script>

<style>
</style>
