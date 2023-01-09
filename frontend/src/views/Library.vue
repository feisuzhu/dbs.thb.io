<template>
  <div class="page_container">
    <div class="breadcrumb">
      <div class="wrap">
        <div class="container"> <a href="#">首页</a><span>/</span>资料库</div>
      </div>
    </div>
    <div class="wrap block carousel_block">
      <div class="container">
        <h2 class="upper">符卡资料库</h2>
        <div class="row mainpage-carousel">
          <!--<slick>-->
            <div class="post_carousel" v-for="c in characters">
              <router-link :to="'/list/' + c.id">
                <img :src="require('assets/library-images/' + c.id + '.jpg')" alt="" />
              <div class="title_t">
                <b>{{ c.name }}</b>
              </div>
              <div class="post_meta">{{ c.meta }}</div>
              查看符卡...
            </router-link>
            </div>
          <!--</slick>-->
        </div>
      </div>
    </div>
    <div class="wrap block">
    <div class="container">
      <div class="row">
        <div class="span6 post">
          <router-link to="/rules">
            <h2 class="title_t"><span>决斗规则</span></h2>
            <img :src="require('assets/library-images/rules.jpg')" alt="" />

              <div class="post_meta">
              真正纯粹的符卡决斗——用灵力宣言符卡，设置陷阱攻其不备，发动状态增强战力！
              </div>
              <div class="title_t">了解梦斗符的游戏流程与规则...</div>
              </router-link>
          </div>
          <div class="span6 post">
          <router-link to="/story">
            <h2 class="title_t"><span>背景故事</span></h2>
            <img :src="require('assets/library-images/story.jpg')" alt="" />
            <div class="post_meta">现世决斗异变已然开启，少女们的力量凭依于符卡，幕后的真凶仍隐于谜团……
            </div>
            <div class="title_t">了解梦斗符背后的剧情故事...</div>
          </router-link>
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<style>
  .mainpage-carousel {
    margin-left: -15px !important;
  }
  .mainpage-carousel .slick-slide {
    margin: 0 15px;
  }
</style>

<script setup>
  const characters = require('data/characters.yaml');
</script>
