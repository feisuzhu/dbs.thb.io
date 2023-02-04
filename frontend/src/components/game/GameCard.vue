<template>
  <div class="game-card">
    <div class="scaler">
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
              <img :src="card.versions[vi].image" alt="">
            </div>
            <div class="meta">
              <p class="pad"></p>
              <p>画师：{{ card.versions[vi].illustrator.name }}</p>
              <p v-if="card.versions[vi].episode">从 {{ card.versions[vi].episode.sku }} 获得</p>
              <p class="pad"></p>
            </div>
          </div>
          <div class="right">
            <slot name="content"></slot>
          </div>
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
    $img-offs-x: 10px;
    $img-offs-y: 25px;
    $header-height: 54px;
    $meta-height: 64px;
    $footer-height: 36px;
    $radius: 15px;
    $frame-aspect-ratio: 1.2744;
    $hpad: 46%;

    position: relative;
    display: block;
    margin: 15px 0px;
    width: 100%;
    aspect-ratio: $frame-aspect-ratio;

    .support   { background-color: #868f97; }
    .center    { background-color: #009504; }
    .hyper     { background-color: #950000; }
    .exclusive { background-color: #7d6e9f; }

    .scaler {
      display: block;
      position: absolute;
      top: 0;
      left: 0;
      transform-origin: top left;
      width: calc(100% * var(--factor));
      height: calc(100% * var(--factor));
      transform: scale(calc(1/var(--factor)));

      --factor: 1;
      @include media-breakpoint-only(xxl) { --factor: 1;    }
      @include media-breakpoint-only(xl)  { --factor: 1.1;  }
      @include media-breakpoint-only(lg)  { --factor: 1.35; }
      @include media-breakpoint-only(md)  { --factor: 1;    }
      @include media-breakpoint-only(sm)  { --factor: 1.2;  }
      @include media-breakpoint-only(xs)  { --factor: 1.3;  }
      @media (max-width: 480px)           { --factor: 1.5;  }
      @media (max-width: 425px)           { --factor: 1.7;  }
    }

    .padding {
      height: $img-offs-y;
    }

    .h-pad {
      width: $hpad;
    }

    .info {
      display: block;
      width: calc(100% - $img-offs-x);
      height: calc(100% - $img-offs-y - $header-height);
      box-shadow: 2px 2px 8px #ccc;
      border-radius: 0 0 $radius $radius;
      margin: 0px 0px 0px $img-offs-x;
    }

    .header {
      position: relative;
      z-index: -1;
      height: $header-height;
      margin: 0 0px 0px $img-offs-x;
      background-color: #a2dfff;
      border-radius: $radius $radius 0 0;
      text-align: right;

      .rarity {
        display: block;
        position: absolute;
        top: 0;
        right: 0;
        z-index: -1;
        font-size: 76px;
        line-height: $header-height;
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
        $font-sz: 18px;

        display: inline-block;
        color: white;
        line-height: $font-sz;
        font-size: $font-sz;
        font-weight: bold;
        margin: calc(($header-height - $font-sz - 5px * 2)/2) 3px;
        padding: 5px 10px;
        border-radius: 3px;
      }

      &.rarity-n  { background-color: #cfded2; }
      &.rarity-r  { background-color: #a2dfff; }
      &.rarity-sr { background-color: #ffee9e; }
    }

    .card-image {
      height: calc(100% - $meta-height);

      img {
        max-width: 100%;
        max-height: calc(100% + $img-offs-y + $header-height);
        border-radius: $radius;
        transform: translate(-$img-offs-x, -$img-offs-y - $header-height);
      }

    }

    .body {
      display: flex;
      height: calc(100% - $footer-height);
      box-shadow: -2px 0px 5px white;
      background-color: #f7f7f7;

      .left {
        display: flex;
        flex-direction: column;
        width: $hpad;
        height: 100%;

        .v-pad {
          display: flex;
          height: calc(100% - $meta-height);
          width: 100%;
        }

        .meta {
          display: flex;
          flex-direction: column;
          width: 100%;
          height: $meta-height;
          vertical-align: middle;

          p {
            margin: 0;
            flex: 0 0 auto;
            text-align: center;
            color: #717171;

            &.pad {
              flex: 1 0 auto;
            }
          }

        }
      }

      .right {
        display: flex;
        flex-direction: column;
        width: calc(100% - $hpad);
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
          height: 36px;
          margin: 8px auto 3px auto;
        }

        .tag {
          $font-sz: 18px;

          display: inline-block;
          color: white;
          line-height: $font-sz;
          font-size: $font-sz;
          font-weight: bold;
          margin: 8px auto;
          padding: 5px 16px;
          border-radius: 3px;
        }

        & > p {
          text-align: left;
          margin: 5px;
          overflow: hidden;
          font-size: 18px;
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
      height: $footer-height;
      background-color: #dfdfdf;
      margin: 0px;
      border-radius: 0 0 $radius $radius;
      z-index: -10;

      .tab {
        font-size: 20px;
        line-height: $footer-height;
        background-color: #c0c0c0;
        padding: 0px 36px;
        border-radius: 0 0 12px 12px;
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
        font-size: 18px;
        line-height: $footer-height;
        font-weight: bold;
        color: #a0a0a0;
      }
    }
  }
</style>
