<template>
  <div class="card-cell row-fluid show-grid" :class="'card-rarity-' + card.rarity">
    <div class="span5" align="center">
      <img :src="require('assets/card-images/' + card.sku + '.jpg')" width="362" />
    </div>
    <div class="span7" align="center">
      <card-info :card="card" />
      <table class="table table-bordered table-striped">
        <tbody>
          <tr>
            <td style="width:20%">华丽度</td>
            <td>{{ card.gorgeousness }}</td>
          </tr>
          <tr>
            <td>消耗灵力</td>
            <td><card-cost :card="card" /></td>
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
            <td><span v-for="a in card.attributes" class="badge badge-inverse">{{ a }}</span></td>
          </tr>
          <tr>
            <td>发动需要</td>
            <td v-for="s in card.special">{{ s }}</td>
          </tr>
          <tr>
            <td colspan="2">{{ card.effect }}</td>
          </tr>
          <tr>
            <td colspan="2"><i>“{{ card.line }}”</i></td>
          </tr>
        </tbody>
      </table>
      <table class="table table-bordered table-striped">
        <tbody v-for="faq in card.faq">
          <tr>
            <td>效果解释与FAQ</td>
          </tr>
          <tr>
            <td><u>{{ faq.answer }}</u></td>
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
  import CardInfo from 'components/list/widgets/CardInfo.vue';
  import CardCost from 'components/list/widgets/CardCost.vue';
  export default {
    name: 'spellcard',
    props: ['card'],
    components: {
        CardInfo,
        CardCost,
    },
  }
</script>
