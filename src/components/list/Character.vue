<template>
  <div class="row-fluid show-grid">
    <!-- Start of post image -->
    <div class="span5" align="center">
      <card-image :card="card" />
    </div>
    <div class="span7" align="center">
      <card-info :card="card" />
      <table class="table table-bordered table-striped">
        <tbody v-for="s in card.skills">
          <tr>
            <td><span class="badge skill-type" :class="s.type | lowercase">{{ s.type }}</span><b>{{ s.name }}</b></td>
          </tr>
          <tr>
            <td>{{ s.desc }}</td>
          </tr>
        </tbody>
        <tbody>
        <tr>
            <td colspan="2"><i>“{{ card.line }}”</i></td>
          </tr>
          </tbody>
      </table>
      <table v-if="card.faq" class="table table-bordered table-striped">
        <tbody>
          <tr>
            <td>效果解释与FAQ</td>
          </tr>
          <tr v-for="faq in card.faq">
            <td><u>{{ faq.answer }}</u></td>
          </tr>
        </tbody>
      </table>
      <!-- Start of post content -->
    </div>
  </div>
</template>

<style>
.skill-type.center { background-color: #40a340; }
.skill-type.hyper  { background-color: #e84242; }
</style>

<script>
  import CardInfo from 'components/list/widgets/CardInfo.vue';
  import CardImage from 'components/list/widgets/CardImage.vue';
  export default {
    name: 'character',
    props: ['card'],
    components: {
        CardInfo,
        CardImage,
    },
  }
</script>
