<template>
  <div class="row-fluid show-grid">
      
    <!-- Start of post image -->
    <div class="span5" align="center">
      <img class="post" :src="require('assets/card-images/' + card.sku + '.jpg')"
      width="400" height="409" align="middle" />
    </div>
    <div class="span7" align="center">
        <div class="btn btn-title" style="width:98.5%" >
        <span class="badge badge-sku" style="float:left">{{ card.sku }}
        </span> 「{{ card.title }}」{{ card.name }}
        
        <span :class="'badge badge-' + card.rarity" style="float:right">{{ card.rarity }}</span>

      </div>
        <div :class="'progress progress-' + card.rarity + ' progress-striped active'">
        <div :class="'bar bar-' + card.rarity">
        画师：{{ card.illustrator }} &nbsp &nbsp | &nbsp &nbsp 版本：{{ card.version }}</div>
      </div>

      <table class="table table-bordered table-striped">
        <tbody v-for="s in card.skills" class="nav nav-list">
          <tr>
            <td><span :class="'badge badge-'+ s.type">{{ s.type }}</span>
            {{ s.name }}</td>
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
