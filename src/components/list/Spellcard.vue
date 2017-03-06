<template>
  <div class="row-fluid show-grid">
    <div class="span5" align="center">
       <h2 class="title" style="text-align:center">{{ card.title }}</h2>
       <img class="post" :src="require('assets/card-images/' + card.sku + '.jpg')"
            width="300" height="409" alt="left aligned" />
    </div>
    <div class="span7" align="center">
      <div class="btn btn-primary disabled" style="width:14%">{{ card.sku }}</div>
      <div class="btn btn-inverse disabled" style="width:67%">画师：{{ card.illustrator }} | 版本：{{ card.version }}</div>
      <div class="btn btn-danger disabled"
      style="width:10%">{{ card.rarity }}</div>
      <table class="table table-bordered table-striped">
        <tbody>
          <tr>
            <td style="width:20%">华丽度</td>
            <td>{{ card.gorgeousness }}</td>
          </tr>
          <tr>
            <td>消耗灵力</td>
            <td>{{ card.cost }}</td>
          </tr>
          <tr>
            <td>符卡类型</td>
            <td>{{ card.type }}</td>
          </tr>
          <tr>
            <td>战力</td>
            <td>{{ card.intensity }}</td>
          </tr>
          <tr>
            <td>特性</td>
            <td><span v-for="a in card.attributes" class="badge badge-inverse">{{ a }}</span>
            </td>
          </tr>
          <tr>
            <td>发动需要</td>
            <td v-for="s in card.special">{{ s }}</td>
          </tr>
          <tr>
            <td colspan="2">{{ card.effect }}</td>
          </tr>
          <tr>
            <td colspan="2">“{{ card.line }}”</td>
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
    name: 'spellcard',
    props: ['card'],
  }
</script>
