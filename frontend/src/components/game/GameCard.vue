<template>
  <div class="game-card">
    <div class="padding"></div>
    <div class="header row" :class="'rarity-' + card.versions[vi].rarity.toLowerCase()">
      <div class="h-pad"></div>
      <div class="col-auto">
        <slot name="tags"></slot>
      </div>
      <div class="rarity">{{ card.versions[vi].rarity }}</div>
    </div>
    <div class="info">
      <div class="body">
        <div class="left">
          <div class="card-image">
            <!--<img :src="card.versions[vi].image" alt="">-->
            <PokemonCSSCard :img="card.versions[vi].image" :back="back" @clickOnActive="emit('click')" />
            <Meta :version="card.versions[vi]" />
          </div>
        </div>
        <div class="right">
          <slot name="content"></slot>
        </div>
        <Meta class="secondary-meta" :version="card.versions[vi]" />
      </div>
      <div class="footer row">
        <div v-for="(v, i) in card.versions" class="col-auto tab" :class="{current: i == vi}">
          <button @click="vi = i">{{ v.version }}</button>
        </div>
        <div class="col"></div>
        <div class="col-auto sku">{{ card.sku }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import PokemonCSSCard from './pokemon-css/PokemonCSSCard.vue'
import Meta from './Meta.vue'
import { ref } from 'vue'

const props = defineProps({
  card: { type: Object },
  back: { type: String },
});

const emit = defineEmits(['click']);

const vi = ref(0);
import { useRouter } from 'vue-router'
</script>

<style lang="scss">
  @import "bootstrap/scss/functions";
  @import "bootstrap/scss/variables";
  @import "bootstrap/scss/mixins";

  .game-card {
    font-size: 18px;

    @include media-breakpoint-only(xxl) { font-size: 18px;   }
    @include media-breakpoint-only(xl)  { font-size: 16px;   }
    @include media-breakpoint-only(lg)  { font-size: 13px;   }
    @include media-breakpoint-only(md)  { font-size: 18px;   }
    @include media-breakpoint-only(sm)  { font-size: 15px;   }
    @include media-breakpoint-only(xs)  { font-size: 2.5vw;  }

    --img-offs-x: 0.56em;
    --img-offs-y: 1.4em;
    --header-height: 3em;
    --meta-height: 3.5em;
    --footer-height: 2em;
    --r: 0.83em;

    --hpad: 46%;

    position: relative;
    display: block;
    margin: 0.83em 0px;
    width: 100%;
    aspect-ratio: 1.2744;

    .support   { background-color: #868f97; }
    .center    { background-color: #009504; }
    .hyper     { background-color: #950000; }
    .exclusive { background-color: #7d6e9f; }

    .padding {
      height: var(--img-offs-y);
    }

    .h-pad {
      width: var(--hpad);
    }

    .info {
      display: block;
      width: calc(100% - var(--img-offs-x));
      height: calc(100% - var(--img-offs-y) - var(--header-height));
      box-shadow: 2px 2px 8px #ccc;
      border-radius: 0 0 var(--r) var(--r);
      margin: 0px 0px 0px var(--img-offs-x);
    }

    .header {
      position: relative;
      z-index: -1;
      height: var(--header-height);
      margin: 0 0px 0px var(--img-offs-x);
      background-color: #a2dfff;
      border-radius: var(--r) var(--r) 0 0;
      text-align: right;

      .rarity {
        display: block;
        position: absolute;
        top: 0;
        right: 0;
        z-index: -1;
        font-size: 4.22222em;
        line-height: 0.71em;
        font-family: "404";
        color: white;
        user-select: none;
        padding: 0;
        transform: translate(2.5px, -7.7px);
      }

      & > div {
        padding: 0;
      }

      .tag {
        display: inline-block;
        color: white;
        line-height: 1em;
        font-size: 1em;
        font-weight: bold;
        margin: calc((var(--header-height) - 1em - 0.28em * 2)/2) 3px;
        padding: 0.28em 0.56em;
        border-radius: 3px;
      }

      &.rarity-n   { background-color: #cfded2; }
      &.rarity-r   { background-color: #a2dfff; }
      &.rarity-sr  { background-color: #ffee9e; }
      &.rarity-ssr { background-color: #ffa1aa; }
      &.rarity-pr  { background-color: #ff5868; }
      &.rarity-tr  { background-color: #ff813d; }
    }

    .body {
      display: flex;
      height: calc(100% - var(--footer-height));
      /* height: 100%; */
      box-shadow: -2px 0px 5px white;
      background-color: #f7f7f7;

      .left {
        display: flex;
        flex-direction: column;
        width: var(--hpad);
        height: calc(100% + 0.9em);
        /* transform: translate(calc(var(--img-offs-x) * -1), calc((var(--img-offs-y) + var(--header-height)) * -1)); */
        margin-left: calc(var(--img-offs-x) * -1);
        margin-right: calc(var(--img-offs-x));
        margin-top: calc((var(--img-offs-y) + var(--header-height)) * -1);

        .card-image {
          /* height: calc(100% - var(--meta-height)); */
          height: 100%;

          img {
            max-width: 100%;
            max-height: calc(100% + var(--img-offs-y) + var(--header-height));
          }
        }

        .v-pad {
          display: flex;
          height: calc(100% - var(--meta-height));
          width: 100%;
        }

      }

      .right {
        display: flex;
        flex-direction: column;
        width: calc(100% - var(--hpad));
        height: 100%;
        padding: 6px;
        /* overflow: hidden; */

        * {
          transition: flex 0.1s ease-in-out;
        }


        & > * {
          display: flex;
          flex: 0 0 auto;
        }

        & > .resizable {
          flex: 0 1 auto;
          min-height: 0;
        }

        .title {
          width: 100%;
          height: 2em;
          margin: 0.5px auto 0.17em auto;
        }

        .tag {
          display: inline-block;
          color: white;
          line-height: 1em;
          font-size: 1em;
          font-weight: bold;
          margin: 0.45em auto;
          padding: 0.28em 1em;
          border-radius: 3px;
        }

        & > p {
          text-align: left;
          margin: 5px;
          overflow: hidden;
          font-size: 1em;
        }

        p[tabindex], div[tabindex] {
          overflow: hidden;
          flex: 0 1 auto;
          &:focus {
            flex: 0 0 auto;
          }
        }
      }
    }

    .footer {
      height: var(--footer-height);
      background-color: #dfdfdf;
      margin: 0px;
      border-radius: 0 0 var(--r) var(--r);
      z-index: -10;

      .tab {
        font-size: 1.11111em;
        line-height: var(--footer-height);
        background-color: #c0c0c0;
        padding: 0px 1.8em;
        border-radius: 0 0 0.6em 0.6em;
        color: #52575c;
        font-weight: bold;

        &.current {
          background-color: #f7f7f7;
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
        font-size: 1em;
        line-height: var(--footer-height);
        font-weight: bold;
        color: #a0a0a0;
      }
    }

    .meta {
      height: var(--meta-height);
      transform: translateX(var(--img-offs-x));
    }

    .secondary-meta {
      display: none;
    }
  }
</style>
