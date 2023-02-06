<template>
  <ApolloQuery :query="spellcardQuery" :variables="{ sku: card }" tag="">
    <template v-slot="{ result: { data, error }, isLoading, query }">
      <GameCard :card="data.spellcard" class="single" v-if="!isLoading && !error">
        <template #tags>
          <template v-if="data.spellcard.type.isAttack">
            <span :style="`background-color: ${data.spellcard.type.bgcolor};`" class="tag">{{ data.spellcard.type.name }}：{{ data.spellcard.intensity }}</span>
            <span style="background-color: #eb7ea9;" class="tag">战斗符卡</span>
          </template>
          <span :style="`background-color: ${data.spellcard.type.bgcolor};`" class="tag" v-else>{{ data.spellcard.type.name }}符卡</span>
        </template>

        <template #content>
          <h3 class="title-text">{{ data.spellcard.title }}</h3>
          <SVGText class="title" :text="data.spellcard.title" />
          <span class="tag" :class="data.spellcard.basicConstraint.toLowerCase()">{{ data.spellcard.build.name }}:{{ data.spellcard.basicConstraint }}</span>
          <div class="content">
            <table class="detail">
              <tbody>
                <tr>
                  <td class="detail-header">华丽度</td><td :class="{ emphasis: data.spellcard.gorgeousness > 5 }">{{ data.spellcard.gorgeousness }}</td>
                  <td class="detail-header">灵力消耗</td><td>{{ data.spellcard.cost }}</td>
                </tr>
                <tr v-if="data.spellcard.type.isAttack">
                  <td class="detail-header">原始战力</td><td :class="{ emphasis: data.spellcard.gorgeousness > 5 }">{{ data.spellcard.intensity }}</td>
                  <td class="detail-header">伤害类型</td><td>{{ data.spellcard.type.name }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div tabindex=0 class="content resizable" v-if="data.spellcard.extendedConstraints?.length > 0">
            <table class="detail extended-constraints">
              <tbody>
                <tr v-for="ec in data.spellcard.extendedConstraints">
                  <td class="detail-header">{{ ec.type }}</td><td>{{ ec.effect }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <!--
          <div class="resizable content" v-if="data.spellcard.extendedConstraints?.length == 1">
            <div class="detail extended-constraints" v-for="ec in card.extendedConstraints">
              <p class="detail-header">{{ ec.type }}</p>
              <p>{{ ec.effect }}</p>
            </div>
          </div>
          -->
          <p>{{ data.spellcard.effect }}</p>
        </template>
      </GameCard>
    </template>
  </ApolloQuery>
</template>

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
    p {
      margin: 0 5px;
    }
  }

  .emphasis {
    color: red;
  }
</style>

<script setup>
import GameCard from '@/components/game/GameCard.vue'
import SVGText from '@/components/game/SVGText.vue'
import gql from 'graphql-tag'

const props = defineProps({
  card: { type: Object },
});

const spellcardQuery = gql`
  query SpellcardQuery($sku: String!) {
    spellcard(sku: $sku) {
      id
      sku title
      gorgeousness cost intensity
      type {
        name description bgcolor isAttack
      }
      traits {
        name description bgcolor
      }
      effect
      faq
      basicConstraint
      extendedConstraints {
        type effect
      }
      build { sku name }
      versions {
        version
        rarity image line
        illustrator { name }
        episode { sku name }
      }
    }
  }
`;
</script>
