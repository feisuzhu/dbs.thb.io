<template>
  <span class="card-cost" :class="`cost-${card.cost}` | lowercase"> </span>
</template>

<style>
.card-cost {
  display:inline-block;
  height:20px;
  margin:auto auto -5px auto;
  text-align:left;
  background-position:left top;
  background-repeat:no-repeat;
}

.card-cost.cost-0 {
  background-image:url(img/cost-free.png);
  width:100px;
}

.card-cost.cost-1 {
  background-image:url(img/cost-spirits.png);
  width:20px;
}

.card-cost.cost-2 {
  background-image:url(img/cost-spirits.png);
  width:40px;
}

.card-cost.cost-3 {
  background-image:url(img/cost-spirits.png);
  width:60px;
}

.card-cost.cost-4 {
  background-image:url(img/cost-spirits.png);
  width:80px;
}

.card-cost.cost-5 {
  background-image:url(img/cost-spirits.png);
  width:100px;
}

.card-cost.cost-lsc {
  background-image:url(img/cost-lastspell.png);
  width:100px;
}

.card-cost.cost-nul {
  background-image:url(img/cost-nullity.png);
  width:100px;
}
</style>

<script>
export default {
    name: 'card-cost',
    props: ['card'],
}
</script>
