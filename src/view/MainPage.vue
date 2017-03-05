<template>
    <!--page_container-->
    <div class="page_container">
        <!--slider-->
        <div id="main_slider">
          <Slider :speed="5000" :show-arrow="true">
            <li :data-bg="require('jessica/img/slider/1.jpg')"></li>
            <li :data-bg="require('jessica/img/slider/2.jpg')"></li>
            <li :data-bg="require('jessica/img/slider/3.jpg')"></li>
          </Slider>
          <div class="clear"></div>
        </div>
        <!--//slider-->

        <!--Welcome-->
        <div class="wrap block">
            <div class="container welcome_block">
              <div class="welcome_line welcome_t"></div>
              现世决斗异变已然开启，少女们的力量凭依于符卡，幕后的真凶仍隐于谜团……<span>欢迎来到幻想梦斗符的世界！</span>
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
                          <span class="img_icon icon1"></span>
                            <span class="link_title">以符卡决斗为核心的原创规则</span>
                         梦斗符是一款 集换式卡牌游戏（TCG）. 在具有两人对战，收集卡牌，构建卡组与交易等元素之外，首次以“符卡战斗”为核心设计规则，超越了一般TCG的“场上生物”这一概念，更契合东方Project的世界观，同时降低了上手难度. 
                        </a>
                    </div>
                    <div class="span3">
                        <a href="#">
                          <span class="img_icon icon2"></span>
                            <span class="link_title">画风各异的授权插绘与精美UI</span>
                          梦斗符是开放合作的同人企划，所使用的所有插绘都是画师的授权作品，而卡框UI则由主催统一精心设计。梦斗符接纳了各种不同风格的插绘，无论是软萌或帅气，亦或是赛璐璐或厚涂，总有能触动你的瞬间！
                        </a>
                    </div>
                    <div class="span3">
                        <a href="#">
                          <span class="img_icon icon3"></span>
                            <span class="link_title">优良的卡牌用纸与印刷工艺</span>
                          梦斗符选用了350g的铜版纸，附以亮油光膜工艺，采用与《MAGIC（万智牌）》同样的6.3cm*8.8cm的标准大尺寸切割。力求手感舒适，同时便于使用通用卡套收藏。梦斗符的游戏过程可以不依赖游戏场地，随时随地都可来一场符卡决斗！
                        </a>
                    </div>
                    <div class="span3">
                        <a href="#">
                          <span class="img_icon icon4"></span>
                            <span class="link_title">丰富的线上线下活动与比赛</span>
                          TCG的生命力在于比赛，因此丝风自始至终关注梦斗符的竞赛模式，定期举办并颁发奖励，并以位于上海的聚游桌游吧为固定活动据点，方便线下聚会。除此之外，还有线上贴吧、论坛、Q 群的丰富社群活动以及新符卡的设计讨论等待你的参与！
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
                  <Slick>
                    <div class="post_carousel">
                      <img :src="require('jessica/img/products/sd02.jpg')" alt="" />
                      <div class="title_t"><a href="#">初战之舞 妖星闪奏曲</a></div>
                        <div class="post_meta">
                        即将于 ComicUP20 上市
                        </div>
                        琪露诺终于再也无法忍受三月精小队的嘲弄和恶作剧，她发誓将用她得意的冰冻能力让三月精知道什么叫「最强」！于是她拉上了蕾蒂和大妖精组成了新的联队……妖精大战争，一触即发！ <a href="#SD02" class="arrow_link">了解更多...</a>
                    </div>  
                    <div class="post_carousel">
                        <img :src="require('jessica/img/products/yyyh.jpg')" alt="" />
                        <div class="title_t"><a href="#">随机扩充包 永夜月华之章</a></div>
                          <div class="post_meta">
                          即将于 ComicUP20 上市
                          </div>
                          红月降临，万物疯狂，藏匿在竹林深处的永远亭，究竟谁才是这场夺走真实之月，创造虚伪红月的主犯？ <a href="#yyyh" class="arrow_link">了解更多...</a>
                    </div>  
                     <div class="post_carousel">
                        <img :src="require('jessica/img/products/qslw.jpg')" alt="" />
                        <div class="title_t"><a href="#">随机扩充包  七色轮舞之章</a></div>
                          <div class="post_meta">
                          已于 ComicUP19 上市
                          </div>
                          七色的人偶师，七曜的魔女与七彩的门卫。绚烂华彩将一同绽放！ <a href="#qslw" class="arrow_link">了解更多...</a>
                    </div>  
                    <div class="post_carousel">
                        <img :src="require('jessica/img/products/mlxy.jpg')" alt="" />
                        <div class="title_t"><a href="#">随机扩充包  梦恋星愿之章</a></div>
                          <div class="post_meta">
                          已于 ComicUP19 上市
                          </div>
                          博丽的巫女、黑白的魔法使、祝风的现人神……幻想乡的故事，由此开始！<a href="#mlxy" class="arrow_link">了解更多...</a>
                    </div>  
                  </Slick>
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
.mainpage-carousel .slick-slide{
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
    var cards = require('data/cards.yaml');
    return { cards: cards };
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
