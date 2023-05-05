<template>
  <div
    ref="thisCard"
    class="pokemon-css-card"
    :class="{ active, interacting, loading, interactive: true }"
    :style="dynamicStyles"
    :data-number="number"
    :data-subtypes="subtypes"
    :data-supertype="supertype"
    :data-rarity="rarity"
  >
    <div class="pokemon-css-card__translater">
      <button
        class="pokemon-css-card__rotator"
        @click="toggleActivate"
        @blur="deactivate"
        @pointermove="interact"
        @mouseout="interactEnd"
      >
        <img class="pokemon-css-card__back" :src="back" />
        <div class="pokemon-css-card__front">
          <!--<img :src="lazy_img" @load="imageLoader" /> giving up lazy loading-->
          <img :src="img" @load="imageLoader" />
          <div class="pokemon-css-card__shine"></div>
          <div class="pokemon-css-card__glare"></div>
        </div>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch, computed } from "vue";
import { activeCard, orientation, resetBaseOrientation, clamp, round, adjust, generateId } from "./helpers.js";
import { spring } from "./svelte-spring.js";

import "./css/base.css";

const props = defineProps({
  name: {
    type: String,
  },
  number: {
    type: String,
  },
  set: {
    type: String,
  },
  types: {
    type: String,
  },
  subtypes: {
    type: String,
    default: "basic",
  },
  supertype: {
    type: String,
    default: "pokémon",
  },
  rarity: {
    type: String,
    default: "common",
  },
  img: {
    type: String,
  },
  back: {
    type: String,
    default: "https://tcg.pokemon.com/assets/img/global/tcg-card-back-2x.jpg",
  },
});

const emit = defineEmits(['activate', 'clickOnActive'])

const randomSeed = {
  x: Math.random(),
  y: Math.random()
}

const randomId = generateId();
const thisCard = ref(null);

const cosmosPosition = {
  x: Math.floor( randomSeed.x * 734 ),
  y: Math.floor( randomSeed.y * 1280 )
};


let repositionTimer;

const active = ref(false);
const interacting = ref(false);
const loading = ref(true);
const lazy_img = ref('');

let firstPop = true;
let isVisible = document.visibilityState === "visible";

const springInteractSettings = { stiffness: 0.132, damping: 0.25 };
const springPopoverSettings = { stiffness: 0.033, damping: 0.45 };
let springRotate = spring({ x: 0, y: 0 }, springInteractSettings);
let springGlare = spring({ x: 50, y: 50, o: 0 }, springInteractSettings);
let springBackground = spring({ x: 50, y: 50 }, springInteractSettings);
let springRotateDelta = spring({ x: 0, y: 0 }, springPopoverSettings);
let springTranslate = spring({ x: 0, y: 0 }, springPopoverSettings);
let springScale = spring({ v: 1 }, springPopoverSettings);

const interact = (e) => {
  if (!isVisible) {
    return (interacting.value = false);
  }

  // prevent other background cards being interacted with
  if (activeCard.value && activeCard.value !== randomId) {
    return (interacting.value = false);
  }

  interacting.value = true;

  if (e.type === "touchmove") {
    e.clientX = e.touches[0].clientX;
    e.clientY = e.touches[0].clientY;
  }

  const $el = e.target;
  const rect = $el.getBoundingClientRect(); // get element's current size/position
  const absolute = {
    x: e.clientX - rect.left, // get mouse position from left
    y: e.clientY - rect.top, // get mouse position from right
  };
  const percent = {
    x: clamp(round((100 / rect.width) * absolute.x)),
    y: clamp(round((100 / rect.height) * absolute.y)),
  };
  const center = {
    x: percent.x - 50,
    y: percent.y - 50,
  };

  updateSprings({
    x: adjust(percent.x, 0, 100, 37, 63),
    y: adjust(percent.y, 0, 100, 33, 67),
  },{
    x: round(-(center.x / 7)),
    y: round(center.y / 5),
  },{
    x: round(percent.x),
    y: round(percent.y),
    o: 1,
  });
};

const interactEnd = (e, delay = 500) => {
  setTimeout(function () {
    const snapStiff = 0.05;
    const snapDamp = 0.09;
    interacting.value = false;

    springRotate.stiffness = snapStiff;
    springRotate.damping = snapDamp;
    springRotate.set({ x: 0, y: 0 }, { soft: 1 });

    springGlare.stiffness = snapStiff;
    springGlare.damping = snapDamp;
    springGlare.set({ x: 50, y: 50, o: 0 }, { soft: 1 });

    springBackground.stiffness = snapStiff;
    springBackground.damping = snapDamp;
    springBackground.set({ x: 50, y: 50 }, { soft: 1 });
  }, delay);
};

const activate = (e) => {
  if (activeCard.value && activeCard.value === randomId) {
    emit('clickOnActive');
    return;
  }
  activeCard.value = randomId;
  resetBaseOrientation();
};

const deactivate = (e) => {
  activeCard.value = '';
};


const toggleActivate = (e) => {
  if (activeCard.value && activeCard.value === randomId) {
    activeCard.value = '';
  } else {
    activeCard.value = randomId;
    resetBaseOrientation();
  }
};

const reposition = (e) => {
  clearTimeout(repositionTimer);
  repositionTimer = setTimeout(() => {
    if (activeCard.value && activeCard.value === randomId) {
      setCenter();
    }
  }, 300);
};

const setCenter = () => {
  const rect = thisCard.value.getBoundingClientRect(); // get element's size/position
  const view = document.documentElement; // get window/viewport size

  const delta = {
    x: round(view.clientWidth / 2 - rect.x - rect.width / 2),
    y: round(view.clientHeight / 2 - rect.y - rect.height / 2),
  };
  springTranslate.set({
    x: delta.x,
    y: delta.y,
  });
};

const popover = () => {
  const rect = thisCard.value.getBoundingClientRect(); // get element's size/position
  let delay = 100;
  let scaleW = (window.innerWidth / rect.width) * 0.9 * 2;
  let scaleH = (window.innerHeight / rect.height) * 0.9 * 2;
  let scaleF = 2;
  setCenter();
  if (firstPop) {
    delay = 1000;
    springRotateDelta.set({
      x: 360,
      y: 0,
    });
  }
  firstPop = false;
  springScale.set({ v: Math.min(scaleW, scaleH, scaleF) });
  interactEnd(null, delay);
};

const retreat = () => {
  springScale.set({ v: 1 }, { soft: true });
  springTranslate.set({ x: 0, y: 0 }, { soft: true });
  springRotateDelta.set({ x: 0, y: 0 }, { soft: true });
  interactEnd(null, 100);
};

const reset = () => {
  interactEnd(null, 0);
  springScale.set({ v: 1 }, { hard: true });
  springTranslate.set({ x: 0, y: 0 }, { hard: true });
  springRotateDelta.set({ x: 0, y: 0 }, { hard: true });
  springRotate.set({ x: 0, y: 0 }, { hard: true });
};

watch(activeCard, (value) => {
  if (value && value === randomId) {
    popover();
    active.value = true;
    emit('activate', true);
  } else {
    retreat();
    active.value = false;
    emit('activate', false);
  }
});


const staticStyles = computed(() => `
  --seedx: ${randomSeed.x};
  --seedy: ${randomSeed.y};
  --cosmosbg: ${cosmosPosition.x}px ${cosmosPosition.y}px;
`);

const dynamicStyles = computed(() => `
  --pointer-x: ${springGlare.values.x}%;
  --pointer-y: ${springGlare.values.y}%;
  --pointer-from-center: ${
    clamp( Math.sqrt(
      (springGlare.values.y - 50) * (springGlare.values.y - 50) +
      (springGlare.values.x - 50) * (springGlare.values.x - 50)
    ) / 50, 0, 1) };
  --pointer-from-top: ${springGlare.values.y / 100};
  --pointer-from-left: ${springGlare.values.x / 100};
  --card-opacity: ${springGlare.values.o};
  --rotate-x: ${springRotate.values.x + springRotateDelta.values.x}deg;
  --rotate-y: ${-springRotate.values.y - springRotateDelta.values.y}deg;
  --background-x: ${springBackground.values.x}%;
  --background-y: ${springBackground.values.y}%;
  --card-scale: ${springScale.values.v * 0.5};
  --translate-x: ${springTranslate.values.x}px;
  --translate-y: ${springTranslate.values.y}px;
`);

const orientate = (e) => {

  const x = e.relative.gamma;
  const y = e.relative.beta;
  const limit = { x: 16, y: 18 };

  const degrees = {
    x: clamp(x, -limit.x, limit.x),
    y: clamp(y, -limit.y, limit.y),
  };

  updateSprings({
    x: adjust(degrees.x, -limit.x, limit.x, 37, 63),
    y: adjust(degrees.y, -limit.y, limit.y, 33, 67),
  },{
    x: round(degrees.x * -1),
    y: round(degrees.y),
  },{
    x: adjust(degrees.x, -limit.x, limit.x, 0, 100),
    y: adjust(degrees.y, -limit.y, limit.y, 0, 100),
    o: 1,
  });

};

const updateSprings = ( background, rotate, glare ) => {

  springBackground.stiffness = springInteractSettings.stiffness;
  springBackground.damping = springInteractSettings.damping;
  springRotate.stiffness = springInteractSettings.stiffness;
  springRotate.damping = springInteractSettings.damping;
  springGlare.stiffness = springInteractSettings.stiffness;
  springGlare.damping = springInteractSettings.damping;

  springBackground.set(background);
  springRotate.set(rotate);
  springGlare.set(glare);

}

watch(activeCard, (value) => {
  if (value && value === randomId) {
    interacting.value = true;
    orientate(orientation);
  }
});

watch(orientation, (value) => {
  if (activeCard.value && activeCard.value === randomId) {
    interacting.value = true;
    orientate(orientation);
  }
});

document.addEventListener("visibilitychange", (e) => {
  isVisible = document.visibilityState === "visible";
  reset();
});

const imageLoader = (e) => {
  loading.value = false;
};

onMounted(() => {
  // set the front image on mount so that
  // the lazyloading can work correctly
  lazy_img.value = props.img;
  window.addEventListener('scroll', reposition);

});

onUnmounted(() => {
  window.removeEventListener('scroll', reposition);
});
</script>

<style scoped>
/* :root { */
/*   --pointer-x: 50%; */
/*   --pointer-y: 50%; */
/*   --card-scale: 1; */
/*   --card-opacity: 0; */
/*   --translate-x: 0px; */
/*   --translate-y: 0px; */
/*   --rotate-x: 0deg; */
/*   --rotate-y: 0deg; */
/*   --background-x: var(--pointer-x); */
/*   --background-y: var(--pointer-y); */
/*   --pointer-from-center: 0; */
/*   --pointer-from-top: var(--pointer-from-center); */
/*   --pointer-from-left: var(--pointer-from-center); */
/* } */
.pokemon-css-card {
  position: relative;
  isolation: isolate;
  width: 200%;
  height: 200%;
  top: 0;
  left: 0;
}

.pokemon-css-card__translater {
  transform-origin: top left;
}

.pokemon-css-card.active {
  z-index: 9999;
}
</style>
