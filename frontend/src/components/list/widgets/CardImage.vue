<template>
  <img :src="cardurl" width="362" />
</template>

<script>
export default {
  name: 'card-image',
  props: ['card'],
  computed: {
    cardurl() {
      var img = this.card.image || this.card.sku + '.jpg';
      try {
        return require('assets/card-images/' + img);
      } catch(e) { }
      return require('assets/card-images/empty.jpg');
    }
  }
}
</script>
