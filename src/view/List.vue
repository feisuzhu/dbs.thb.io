<template>
  <div class="page_container">
    <div class="breadcrumb">
      <div class="wrap">
        <div class="container"> <a href="#">首页</a><span>/</span>符卡资料库</div>
      </div>
    </div>
    <div class="container inner_content">
      <section>
        <div class="row show-grid">
          </br>
          <div class="span10">
            <div v-for="c in interested.character.cards">
              <character :card="c"></character>
              <hr>
            </div>
            <div v-for="c in interested.cards">
              <spellcard :card="c"></spellcard>
              <hr>
            </div>
          </div>
          <div class="span2">
            <character-affix :characters="characters"></character-affix>
          </div>
        </div>
      </section>
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
      var cards = require('data/cards.loader.json');
      var characters = require('data/characters.yaml');
      return {
        cards: cards,
        characters: characters,
      };
    },
    computed: {
        interested() {
            var id = this.$route.params.id || characters[0].id;
            return {
                cards: this.cards[id],
                character: this.characters.find((c) => c.id == id),
            }
        }
    },
    components: { Character, CharacterAffix, Spellcard },
  }
</script>
