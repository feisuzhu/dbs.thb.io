<template>
  <div class="post">
    <h2>{{ card.title }} {{ card.name }}</h2>
    <!-- Start of post image -->
    <div class="intro">
      <a href="#"><img class="alignleft" :src="require('assets/card-images/' + card.sku + '.jpg')" width="300" height="409" alt="left aligned" /></a>
      <div class="form_submit">
        <ul>
          <li>编号：{{ card.sku }}</li>
          <li>稀有度：{{ card.rarity }}</li>
          <li>画师：{{ card.illustrator }}</li>
          <li>版本：{{ card.version }}</li>
        </ul>
      </div>
    </div>
    <div class="post_comments">
      <div v-for="s in card.skills">
        <p>{{ s.type }}</p>
        <p>{{ s.name }}</p>
        <p>{{ s.desc }}</p>
        <hr>
      </div>
    </div>
    <div class="post_content_wrapper">
      <div v-for="faq in card.faq">
        <p>Q: {{ faq.question }}</p>
        <p>A: {{ faq.answer }}</p>
        <hr>
      </div>
    </div>

    <div class="other_post_details_wrapper">
      <!-- Start of post content -->
      <div class="post_content">
        <div class="post_content_wrapper">
          <p>*This Card is come from {{ card.origin }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'character',
    props: ['card'],
  }
</script>
