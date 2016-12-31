<template>
  <div>
    <div id="slider_wrapper">
      <div id="breadcrumb_wrapper">
        <h1>符卡图鉴</h1>

        <div id="breadcrumb">
          <ul>
            <li><a href="index.html">首页</a> </li>
            <li>&#8250;&nbsp; <a href="library.html">资料库</a></li>
            <li>&#8250;&nbsp; <a href="cardlist.html">符卡图鉴</a></li>
            <li>&#8250;&nbsp; 灵梦</li>
          </ul>
        </div>
      </div>
    </div>

    <div id="wrapper">
      <div class="left_content_wrapper">
        <div v-for="c in cards[0].characters">
          <character :card="c"></character>
        </div>
        <div v-for="c in cards[0].spellcards">
          <spellcard :card="c"></spellcard>
        </div>
      </div>
    </div>

    <div class="right_content_wrapper">
      <character-affix :cards="cards"></character-affix>
    </div>
    <div class="clear"></div>
  </div>
</template>

<script>
import Character from 'components/list/Character.vue'
import Spellcard from 'components/list/Spellcard.vue'
import CharacterAffix from 'components/list/CharacterAffix.vue'

export default {
  name: 'List',
  data() {
    var cards = require('data/cards.yaml');
    return { cards: cards };
  },
  components: { Character, CharacterAffix, Spellcard },
}
</script>
