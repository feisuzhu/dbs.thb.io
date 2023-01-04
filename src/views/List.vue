<template>
  <div class="page_container">
    <div class="breadcrumb">
      <div class="wrap">
        <div class="container"> <a href="#">首页</a><span>/</span><a href="#/library">资料库</a><span>/</span>符卡资料库</div>
      </div>
    </div>
    <div class="container inner_content">
      <section>
        <div class="row show-grid">
          <br>
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
          <div class="CharacterAffix">
          <div class="span2">
            <character-affix :characters="characters"></character-affix>
          </div>
          </div>
        </div>
      </section>
    </div>
    <div class="go-top">
      <div class="arrow"></div>
      <div class="stick"></div>
    </div>
  </div>
</template>
<style>
@media (min-width: 1801px) {
  .CharacterAffix .span2{
      position:fixed;
      min-width:10%;
      max-width:20%;
      height:100%;
      left:71%;
      bottom:-20%;
      overflow-x:hidden;
  }
}
@media (min-width: 1501px) and (max-width:1800px){
  .CharacterAffix .span2{
      position:fixed;
      max-width:20%;
      height:100%;
      left:75%;
      bottom:-20%;
      overflow-x:hidden;
  }
}
@media (min-width: 1201px) and (max-width: 1500px){
  .CharacterAffix .span2{
      position:fixed;
      min-width:13%;
      max-width:20%;
      height:100%;
      left:81%;
      right:160px;
      bottom:-20%;
      overflow-x:hidden;
  }
}
  @media (min-width: 980px) and (max-width: 1200px){
    .CharacterAffix .span2{
        position:fixed;
        min-width:18%;
        max-width:32%;
        height:100%;
        right:-1%;
        bottom:-20%;
        overflow-x:hidden;
    }
  }
  @media (min-width: 768px) and (max-width: 979px) {
    .CharacterAffix .span2{
        position:fixed;
        min-width:20%;
        max-width:40%;
        height:100%;
        right:-1%;
        top:300px;
        overflow-x:hidden;
    }
  }
  @media (max-width: 767px) {
    .CharacterAffix .span2{
        position:absolute;
        max-width:28%;
        max-height:100%;
        right:-4.5%;
        top:330px;
        overflow-x:hidden;
    }
    .span10{
      max-width:76%;
      overflow-x:hidden;
    }
    div.go-top {
      display: none;
      opacity: 0.6;
      z-index: 999999;
      position: fixed;
      bottom: 113px;
      left: 90%;
      margin-left: 40px;
      border: 1px solid #a38a54;
      width: 38px;
      height: 38px;
      background-color: #eddec2;
      border-radius: 3px;
      cursor: pointer;
    }

    div.go-top:hover {
      opacity: 1;
      filter: alpha(opacity=100);
    }

    div.go-top div.arrow {
      position: absolute;
      left: 10px;
      top: -1px;
      width: 0;
      height: 0;
      border: 9px solid transparent;
      border-bottom-color: #cc3333;
}

    div.go-top div.stick {
      position: absolute;
      left: 15px;
      top: 15px;
      width: 8px;
      height: 14px;
      display: block;
      background-color: #cc3333;
      -webkit-border-radius: 1px;
      -moz-border-radius: 1px;
      border-radius: 1px;
}
  }
</style>
<script>
  import Character from '@/components/list/Character.vue'
  import Spellcard from '@/components/list/Spellcard.vue'
  import CharacterAffix from '@/components/list/CharacterAffix.vue'

  const cards = require('data/cards.loader.json');
  const characters = require('data/characters.yaml');

    /* computed: { */
    /*     interested() { */
    /*         var id = this.$route.params.id; */
    /*         if(!id) { */
    /*         } */
    /*         return { */
    /*             cards: this.cards[id], */
    /*             character: this.characters.find((c) => c.id == id), */
    /*         } */
    /*     } */
    /* }, */
    /* beforeRouteEnter(to, from, next) { */
    /*   if(to.params.id) { */
    /*     next(); */
    /*   } else { */
    /*     var characters = require('data/characters.yaml'); */
    /*     next('/list/' + characters[0].id); */
    /*   } */
    /* }, */
  /* } */
</script>
