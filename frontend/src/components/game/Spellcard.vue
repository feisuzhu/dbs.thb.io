<template>
  <GameCard :card="card" back="/uploads/card/spellcard-back.jpg">
    <template #tags>
      <template v-if="card.type.isAttack">
        <span :style="`background-color: ${card.type.bgcolor};`" class="tag">{{ card.type.name }}：{{ card.intensity }}</span>
        <span style="background-color: #eb7ea9;" class="tag">战斗符卡</span>
      </template>
      <span :style="`background-color: ${card.type.bgcolor};`" class="tag" v-else>{{ card.type.name }}符卡</span>
    </template>

    <template #content>
      <SVGText class="title" :text="card.title" />
      <span class="tag" :class="card.basicConstraint.toLowerCase()">{{ card.build.name }}:{{ card.basicConstraint }}</span>
      <div class="content">
        <table class="detail">
          <tbody>
            <tr>
              <td class="detail-header">华丽度</td><td :class="{ emphasis: card.gorgeousness > 5 }">{{ card.gorgeousness }}</td>
              <td class="detail-header">灵力消耗</td><td>{{ card.cost }}</td>
            </tr>
            <tr v-if="card.type.isAttack">
              <td class="detail-header">原始战力</td><td :class="{ emphasis: card.gorgeousness > 5 }">{{ card.intensity }}</td>
              <td class="detail-header">伤害类型</td><td>{{ card.type.name }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div tabindex=0 class="content resizable" v-if="card.extendedConstraints?.length > 0">
        <table class="detail extended-constraints">
          <tbody>
            <tr v-for="ec in card.extendedConstraints">
              <td class="detail-header">{{ ec.type }}</td><td>{{ ec.effect }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <!--
      <div class="resizable content" v-if="card.extendedConstraints?.length == 1">
        <div class="detail extended-constraints" v-for="ec in card.extendedConstraints">
          <p class="detail-header">{{ ec.type }}</p>
          <p>{{ ec.effect }}</p>
        </div>
      </div>
      -->
      <p class="effect" tabindex=0 v-html="card.effect"></p>
    </template>
  </GameCard>
</template>

<script setup>
import GameCard from './GameCard.vue'
import SVGText from './SVGText.vue'
const props = defineProps({
  card: { type: Object },
});
</script>

<style lang="scss" scoped>
  .content {
    font-size: 1em;
  }

  .detail {
    width: 100%;
    margin: 0 0 8px 0;
    td {
      padding: 0 5px;
    }
  }

  .detail-header {
    white-space: nowrap;
    font-weight: bold;
    vertical-align: top;
  }

  .extended-constraints {
    color: red;
    p {
      margin: 0 5px;
    }
  }

  .emphasis {
    color: red;
  }
</style>
