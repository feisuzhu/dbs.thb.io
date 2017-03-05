<template>

  <div class="row-fluid show-grid">


    <!-- Start of post image -->

      <div class="span6">
             <h2 class="title">{{ card.title }} {{ card.name }}</h2>

             <img class="alignleft" :src="require('assets/card-images/' + card.sku + '.jpg')" width="300" height="409" alt="left aligned" />
      </div>
      <div class="span6">
            <button class="btn">{{ card.sku }}
            </button>
            <button class="btn">画师：{{ card.illustrator }}
            </button>
            <button class="btn">版本：{{ card.version }}
            </button>

            <button class="btn">稀有度：{{ card.rarity }}
            </button>
            <hr>
            <div v-for="s in card.skills">
            <p>{{ s.type }}</p>
            <p>{{ s.name }}</p>
            <p>{{ s.desc }}</p>
            <hr>
            </div>
      </div>
    <div>
      <div v-for="faq in card.faq">
        <p>Q: {{ faq.question }}</p>
        <p>A: {{ faq.answer }}</p>
        <hr>
      </div>
    </div>

    <div>
      <!-- Start of post content -->
      <div>
        <div>
          <p>*This Card is come from {{ card.origin }}</p>
        </div>
      </div>
    </div>
<hr>
</div>

</template>

<script>
  export default {
    name: 'character',
    props: ['card'],
  }
</script>
