<template>
  <div>
    <div class="btn btn-title" style="width:98.5%">
      <span class="badge badge-sku">{{ card.sku }}</span>
      {{ display_title }}
      <span class="badge badge-rarity rarity-color" :class="card.rarity | lowercase">{{ card.rarity }}</span>
    </div>
    <div class="progress progress-striped rarity-color active" :class="card.rarity | lowercase">
      <div class="rarity-color bar" :class="card.rarity | lowercase">
        画师：{{ card.illustrator }} &nbsp; &nbsp; | &nbsp; &nbsp; 版本：{{ card.version }}
      </div>
    </div>
  </div>
</template>

<style>
.badge-sku {
    background-color: #797979;
    float: left;
}

.badge-rarity {
    float: right;
}

.rarity-color.pr  { background-color: #ff3737 !important; }
.rarity-color.ssr { background-color: #ff4c76 !important; }
.rarity-color.sr  { background-color: #ff8400 !important; }
.rarity-color.sp  { background-color: #ffa0a0 !important; }
.rarity-color.r   { background-color: #5ea3f1 !important; }
.rarity-color.uc  { background-color: #3fa74f !important; }
.rarity-color.c   { background-color: #797979 !important; }
.rarity-color.st   { background-color: #6bd77f !important; }

.progress.rarity-color .bar {
  width: 100%;
}
</style>

<script>
export default {
    name: 'card-info',
    props: ['card'],
    computed: {
        display_title() {
          var c = this.card;
          return c.name ? `「${c.title}」${c.name}` : c.title;
        },
    },
}
</script>
