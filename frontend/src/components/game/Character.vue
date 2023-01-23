<template>
  <div class="game-card">
    <div class="padding"></div>
    <div class="header" :class="'rarity-' + card.versions[vi].rarity.toLowerCase()">
      <div style="width: 50%;"></div>
      <div class="col">tags</div>
      <div class="col rarity">{{ card.versions[vi].rarity }}</div>
    </div>
    <img class="card-image" :src="card.versions[vi].image" alt="">
    <div class="body"></div>
    <div class="footer row">
      <div v-for="(v, i) in card.versions" class="col-auto tab" :class="{current: i == vi}">
        <button @click="vi = i">{{ v.version }}</button>
      </div>
      <div class="col"></div>
      <div class="col-auto sku">{{ card.sku }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const props = defineProps({
  card: {
    type: Object,
  }
});

const vi = ref(0);


</script>

<style lang="scss">
  @import "bootstrap/scss/functions";
  @import "bootstrap/scss/variables";
  @import "bootstrap/scss/mixins";

  .game-card {
    $img-offs-x: 15px;
    $img-offs-y: 25px;
    $header-height: 36px;
    $footer-height: 24px;
    $radius: 15px;

    position: relative;
    display: block;
    margin: 10px 0px 0px;
    width: 100%;
    aspect-ratio: 1.28;
    /* border: 1px solid #000; */

    .padding {
      height: $img-offs-y;
    }

    .header {
      display: flex;
      height: $header-height;
      margin: 0 0px 0px $img-offs-x;
      background-color: #a2dfff;
      border-radius: $radius $radius 0 0;
      text-align: right;
      box-shadow: 2px 2px 8px #ccc;

      & > div {
        flex: 0 0 auto;
      }

      .rarity {
        display: block;
        font-size: 52px;
        line-height: $header-height;
        font-family: "404";
        color: white;
        user-select: none;
        transform: translate(1px, -4.5px);
      }

      &.rarity-n  { background-color: #cfded2; }
      &.rarity-r  { background-color: #a2dfff; }
      &.rarity-sr { background-color: #ffee9e; }
    }

    .card-image {
      position: absolute;
      top: 0px;
      left: 0px;
      height: 80%;
      border-radius: 8px;
    }

    .body {
      display: block;
      height: calc(100% - $header-height - $footer-height - $img-offs-y);
      margin: 0px 0px 0px $img-offs-x;
      background-color: white;
      box-shadow: 2px 2px 8px #ccc, -2px 0px 5px white;
    }

    .footer {
      height: $footer-height;
      background-color: #dfdfdf;
      margin: 0px 0px 0px $img-offs-x;
      border-radius: 0 0 $radius $radius;
      box-shadow: 2px 2px 8px #ccc;

      .tab {
        font-size: 14px;
        background-color: #c0c0c0;
        padding: 0px 20px;
        border-radius: 0 0 8px 8px;
        color: #52575c;
        font-weight: bold;
        &.current {
          background-color: white;
        }
        button {
          background: none;
          color: inherit;
          border: none;
          padding: 0;
          font: inherit;
          cursor: pointer;
          outline: inherit;
        }
      }

      .sku {
        color: #a0a0a0;
      }
    }
  }
</style>
