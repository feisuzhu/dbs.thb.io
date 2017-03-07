<template>
  <div class="row-fluid show-grid">
    <!-- Start of post image -->
    <div class="span5" align="center">
      <img :src="require('assets/card-images/' + card.sku + '.jpg')" width="400" height="409" align="middle" />
    </div>
    <div class="span7" align="center">
      <card-info :card="card" />
      <table class="table table-bordered table-striped">
        <tbody v-for="s in card.skills" class="nav nav-list">
          <tr>
            <td><span class="badge skill-type" :class="s.type | lowercase">{{ s.type }}</span>{{ s.name }}</td>
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

<style>
.skill-type.center { background-color: #40a340; }
.skill-type.hyper  { background-color: #e84242; }
</style>

<script>
  import CardInfo from 'components/list/widgets/CardInfo.vue';
  export default {
    name: 'character',
    props: ['card'],
    components: {
        CardInfo,
    },
  }
</script>
