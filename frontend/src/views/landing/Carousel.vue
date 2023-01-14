<template>
    <div id="landing-carousel" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
            <button v-for="(s, i) in slides" type="button" data-bs-target="#landing-carousel" :data-bs-slide-to="i" :class="{active: i == 0}" aria-current="true" :aria-label="'Slide ' + i"></button>
        </div>
        <div class="carousel-inner">
            <div v-for="(s, i) in slides" class="carousel-item" :class="{active: i == 0}">
                <a :href="s.url"><img :src="s.image" class="d-block w-100"></a>
            </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#landing-carousel" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">上一张</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#landing-carousel" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">下一张</span>
        </button>
    </div>
</template>

<script setup>
const props = defineProps({
    slides: {
        type: Array,
        required: true
    }
})
</script>

<style lang="scss">
  #landing-carousel {
    img {
      min-height: 250px;
      object-fit: cover;
    }
  }
</style>
