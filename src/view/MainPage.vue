<template>
  <!--page_container-->
  <div class="page_container">
    <!--slider-->
    <div id="main_slider">
      <slider :speed="5000" :show-arrow="true">
        <li :data-bg="require('assets/mainpage/slider/1.jpg')"></li>
        <li :data-bg="require('assets/mainpage/slider/2.jpg')"></li>
        <li :data-bg="require('assets/mainpage/slider/3.jpg')"></li>
      </slider>
      <div class="clear"></div>
    </div>
    <!--//slider-->
    <!--Welcome-->
    <div class="wrap block">
      <div class="container welcome_block">
        <div class="welcome_line welcome_t"></div>
          现世决斗异变已然开启，少女们的力量凭依于符卡，幕后的真凶仍隐于谜团……
          <span>欢迎来到梦斗符的世界！</span>
        <div class="welcome_line welcome_b"></div>
    </div>
  </div>
  <!--//Welcome-->

  <!--latest posts-->
  <div class="wrap block carousel_block">
    <div class="container">
      <h2 class="upper">作品一览</h2>
      <div class="row mainpage-carousel">
        <slick>
          <div class="post_carousel" v-for="ep in episodes">
            <img :src="require('assets/episode-images/' + ep.id + '.jpg')" alt="" />
            <div class="title_t">
              <router-link :to="'/episodes/' + ep.id">{{ ep.title }}</router-link>
            </div>
            <div class="post_meta">{{ ep.meta }}</div>{{ ep.desc }}</br>
            <router-link :to="'/episodes/' + ep.id">了解更多...</router-link>
          </div>
        </slick>
      </div>
    </div>
  </div>
  <!--planning-->
  <div class="wrap">
    <div class="container">

      <div class="row">
        <div class="post_carousel span4">
            <h2 class="upper">快速上手</h2>
            <div class="post_meta">梦斗符是一款全新概念的集换式卡牌游戏。</div> 在具有两人对战，收集卡牌，构建卡组与交易等传统TCG元素的基础上，首次以「弹幕相杀」而不是「场上生物」为核心设计规则，更契合东方Project的世界观，同时降低了上手难度.
            <router-link to="/rules"><div class="title_t">了解梦斗符规则...</div></router-link>

        </div>
        <div class="post_carousel span4">
          <h2 class="upper">华丽精美</h2>
            <div class="post_meta">梦斗符是开放合作、兼容并包的同人企划。</div>所使用的所有插绘都是画师的授权作品。而卡框UI则由主催统一精心设计。梦斗符接纳了各种不同风格的插绘，无论是软萌或帅气，亦或是赛璐璐或厚涂，总有能触动你的瞬间！
            <router-link to="/list"><div class="title_t">查看精美卡面...</div></router-link>

        </div>
        <div class="post_carousel span4">
          <h2 class="upper">诚意制作</h2>
            <div class="post_meta">梦斗符用料扎实、工艺先进、包装精美。</div>采用与《万智牌》同样的6.3cm*8.8cm的标准大尺寸切割。力求手感舒适，同时便于使用通用卡套收藏。梦斗符的游戏过程可以不依赖游戏场地，随时随地都可来一场符卡决斗！
            <a href="https://projectzephyr.taobao.com/"><div class="title_t">立即购买...</div></a>
        </div>
      </div>
    </div>
  </div>
  <!--//planning-->
  </div>
    <!--//latest posts-->
  <!--//page_container-->
</template>

<style>
  .mainpage-carousel {
    margin-left: -15px !important;
  }
  .mainpage-carousel .slick-slide {
    margin: 0 15px;
  }
</style>

<script>
  import Character from 'components/list/Character.vue'
  import Spellcard from 'components/list/Spellcard.vue'
  import CharacterAffix from 'components/list/CharacterAffix.vue'
  import Slider from 'components/common/slider/Slider.vue'
  import Slick from 'components/common/slick/Slick.vue'

  export default {
    name: 'List',
    data() {
      return {
        episodes: require('data/episodes.yaml'),
      }
    },
    components: {
      Slider,
      Slick,
      Character,
      CharacterAffix,
      Spellcard,
    },
  }
</script>
