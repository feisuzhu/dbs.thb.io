<template>
  <div class="card-cell row-fluid show-grid">
    <div class="span5" align="center">
      <card-image :card="card" />
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
            <td><span v-for="a in card.attributes" @click="showAttr(a)" class="badge badge-inverse card-attr">{{ a }}</span></td>
          </tr>
          <tr v-if="current_attr">
            <td colspan="2">{{ current_attr.name }}：{{ current_attr.desc }}</td>
          </tr>
          <tr v-for="s in card.special">
            <td>发动需要</td>
            <td>{{ s }}</td>
          </tr>
          <tr>
            <td colspan="2">{{ card.effect }}</td>
          </tr>
          <tr>
            <td colspan="2"><i>“{{ card.line }}”</i></td>
          </tr>
        </tbody>
      </table>
      <table v-if="card.faq && card.faq.length" class="table table-bordered table-striped">
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
        <tbody>
          <tr>
            <td>* This card comes from {{ card.origin || 'MISSING' }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style>
.card-attr {
  cursor: pointer;
}
</style>

<script>
  import CardInfo from 'components/list/widgets/CardInfo.vue';
  import CardCost from 'components/list/widgets/CardCost.vue';
  import CardImage from 'components/list/widgets/CardImage.vue';
  export default {
    name: 'spellcard',
    props: ['card'],
    data() {
      return {
        current_attr: null,
      };
    },
    methods: {
      showAttr(attr) {
        var attrs = require('data/attributes.yaml');
        this.current_attr = {
          name: attr,
          desc: attrs[attr],
        };
      }
    },
    components: {
        CardInfo,
        CardCost,
        CardImage,
    },
  }
</script>
