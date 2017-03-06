<template>
  <div class="row-fluid show-grid">
    <!-- Start of post image -->
    <div class="span5">
      <h2 class="title">{{ card.title }} {{ card.name }}</h2>
      <img class="alignleft" :src="require('assets/card-images/' + card.sku + '.jpg')"
           width="300" height="409" alt="left aligned" />
    </div>
    <div class="span7">
      <div class="btn btn-primary disabled" style="width:14%">{{ card.sku }}</div>
      <div class="btn btn-inverse disabled" style="width:70%">画师：{{ card.illustrator }} | 版本：{{ card.version }}</div>
      <div class="btn btn-danger disabled" style="width:10%">{{ card.rarity }}</div>
      <table class="table table-bordered table-striped">
        <tbody v-for="s in card.skills" class="nav nav-list">
          <tr>
            <td><span class="badge badge-inverse">{{ s.type }}</span>{{ s.name }}</td>
          </tr>
          <tr>
            <td>{{ s.desc }}</td>
          </tr>
        </tbody>
      </table>
      <table class="table table-bordered table-striped">
        <tbody v-for="faq in card.faq">
          <tr>
            <td>Q: {{ faq.question }}</td>
          </tr>
          <tr>
            <td>A: {{ faq.answer }}</td>
          </tr>
        </tbody>
      </table>
      <!-- Start of post content -->
      <table class="table table-bordered table-striped">
        <tbody v-for="faq in card.faq">
          <tr>
            <td>*This Card is come from {{ card.origin }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'character',
    props: ['card'],
  }
</script>
