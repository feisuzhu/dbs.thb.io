<template>
  <div class="page_container">
        <div v-for="c in cards[0].characters">
          <character :card="c"></character>
        </div>

        <div v-for="c in cards[0].spellcards">
          <spellcard :card="c"></spellcard>
        </div>
    <div>
      <character-affix :cards="cards"></character-affix>
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
