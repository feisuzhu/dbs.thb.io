<template>
  <GameCard :card="card" :build="build">
    <template #tags>
      <template v-if="card.type.isAttack">
        <span :style="`background-color: ${card.type.bgcolor};`" class="tag">{{ card.type.name }}：{{ card.intensity }}</span>
        <span style="background-color: #eb7ea9;" class="tag">战斗符卡</span>
      </template>
      <span :style="`background-color: ${card.type.bgcolor};`" class="tag" v-else>{{ card.type.name }}符卡</span>
    </template>

    <template #content>
      <SVGText class="title" :text="card.title" />
      <span class="tag" :class="card.basicConstraint.toLowerCase()">{{ build.name }}:{{ card.basicConstraint }}</span>
      <div class="content">
        <table class="detail">
          <tbody>
            <tr>
              <td class="detail-header">华丽度</td><td :class="{ emphasis: card.gorgeousness > 5 }">{{ card.gorgeousness }}</td>
              <td class="detail-header">灵力消耗</td><td>{{ card.cost }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="content" v-if="card.extendedConstraints">
        <table class="detail extended-constraints">
          <tbody>
            <tr v-for="ec in card.extendedConstraints">
              <td class="detail-header">{{ ec.type }}</td><td>{{ ec.effect }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="resizable content">
        <p class="effect">{{ card.effect }}</p>
      </div>
    </template>
  </GameCard>
</template>

<script setup>
import GameCard from './GameCard.vue'
import SVGText from './SVGText.vue'
const props = defineProps({
  build: { type: Object },
  card: { type: Object },
});
</script>

<style lang="scss" scoped>
  .content {
    font-size: 18px;
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
  }

  .emphasis {
    color: red;
  }

  .effect {
    margin: 5px 0 0 0;
    text-align: left;
    display: -webkit-box;
    -webkit-line-clamp: 6;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
</style>
