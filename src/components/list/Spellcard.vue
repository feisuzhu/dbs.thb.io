<template>
  <div class="row-fluid show-grid">
    
      <div class="span8">

         <h2>{{ card.title }}</h2>
         <div>
         <a href="#"><img class="alignleft" :src="require('assets/card-images/' + card.sku + '.jpg')" width="300" height="409" alt="left aligned" /></a>
                <div>
                <ul>
                <li>编号：{{ card.sku }}</li>
                <li>稀有度：{{ card.rarity }}</li>
                <li>画师：{{ card.illustrator }}</li>
                <li>版本：{{ card.version }}</li>
                </ul>
                </div>
         </div>
         <div>
            <ul>
            <li>华丽度：{{ card.gorgeousness }}</li>
            <li>消耗灵力：{{ card.cost }}</li>
            <li>战斗符卡：{{ card.type }} {{ card.intensity }}</li>
            <li>特性：<span v-for="a in card.attributes">{{ a }}</span></li>
            <li v-for="s in card.special">{{ s }}</li>
            <li>{{ card.effect }}</li>
            <li>“{{ card.line }}”</li>
            </ul>
        </div>
        <div>
            <div v-for="faq in card.faq">
            <p>Q: {{ faq.question }}</p>
            <p>A: {{ faq.answer }}</p>
            <hr>
            </div>
        </div>

        <div>
          <p>*This Card is come from {{ card.origin }}</p>
        </div>

      </div>

  </div>

</template>

<script>
  export default {
    name: 'spellcard',
    props: ['card'],
  }
</script>
