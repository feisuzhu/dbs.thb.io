<template>
  <div class="page_container">
        <div class="breadcrumb">
          <div class="wrap">
                <div class="container">
                    <a href="#">首页</a><span>/</span>符卡资料库
                </div>
            </div> 
        </div>

        <div class="container inner_content">

        
        <section id="gridSystem">
        <div class="row show-grid">
                <div class="span9">
                  <div v-for="c in cards[0].characters">
                  <character :card="c"></character>
                  </div>
                  <div v-for="c in cards[0].spellcards">
                  <spellcard :card="c"></spellcard>
                </div>


                </div>

                <div class="span3">     
                  <character-affix :cards="cards">
                  </character-affix>
                </div>
        </div>
        <section/>
        </div>

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
