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
              现世决斗异变已然开启，少女们的力量凭依于符卡，幕后的真凶仍隐于谜团……<span>欢迎来到梦斗符的世界！</span>
                <div class="welcome_line welcome_b"></div>
            </div>
        </div>
        <!--//Welcome-->
        <!--planning-->
        <div class="wrap planning">
            <div class="container">
                <div class="row">
                    <div class="span3">
                        <a href="#">
                          
                            <span class="link_title">容易上手的决斗</span>
                            <span class="img_icon icon1"></span>
                         ◉> 梦斗符是一款 集换式卡牌游戏, 在具有两人对战，收集卡牌，构建卡组与交易等元素之外，首次以“符卡战斗”为核心设计规则，超越了一般TCG的“场上生物”这一概念，更契合东方Project的世界观，同时降低了上手难度.
                        </a>
                    </div>
                    <div class="span3">
                        <a href="#">
                          
                            <span class="link_title">画风精美的插绘</span>
                            <span class="img_icon icon2"></span>
                          ◉> 梦斗符是开放合作的同人企划，所使用的所有插绘都是画师的授权作品，而卡框UI则由主催统一精心设计。梦斗符接纳了各种不同风格的插绘，无论是软萌或帅气，亦或是赛璐璐或厚涂，总有能触动你的瞬间！
                        </a>
                    </div>
                    <div class="span3">
                        <a href="#">
                          
                            <span class="link_title">工艺优良的卡面</span>
                            <span class="img_icon icon3"></span>
                          ◉> 梦斗符选用了350g的铜版纸，附以亮油光膜工艺，采用与《万智牌》同样的6.3cm*8.8cm的标准大尺寸切割。力求手感舒适，同时便于使用通用卡套收藏。梦斗符的游戏过程可以不依赖游戏场地，随时随地都可来一场符卡决斗！
                        </a>
                    </div>
                    <div class="span3">
                        <a href="#">
                         
                            <span class="link_title">丰富精彩的活动</span>
                             <span class="img_icon icon4"></span>
                          ◉> TCG的生命力在于比赛，因此丝风自始至终关注梦斗符的竞赛模式，定期举办并颁发奖励，并以位于上海的聚游桌游吧为固定活动据点，方便线下聚会。除此之外，还有线上贴吧、论坛、Q 群的丰富社群活动以及新符卡的设计讨论等待你的参与！
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <!--//planning-->
        <!--latest posts-->
        <div class="wrap block carousel_block">
            <div class="container">
              <h2 class="upper">作品一览</h2>
              <div class="row mainpage-carousel">
                  <slick>
                    <div class="post_carousel" v-for="ep in episodes">
                      <img :src="require('assets/episode-images/' + ep.id + '.jpg')" alt="" />
                      <div class="title_t"><router-link :to="'/episodes/' + ep.id">{{ ep.title }}</router-link></div>
                        <div class="post_meta">{{ ep.meta }}</div>
                        {{ ep.desc }}
                        </br><router-link :to="'/episodes/' + ep.id">了解更多...</router-link>
                    </div>
                  </slick>
                </div>
            </div>
        </div>
        <!--//latest posts-->
    </div>
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
      cards: require('data/cards.yaml'),
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
