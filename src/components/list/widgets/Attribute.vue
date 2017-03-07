<template>
  <popover effect="fade" placement="top" :title="attr" :content="attrs[attr]">
    <span class="badge badge-inverse">{{ attr }}</span>
  </popover>
</template>

<style>
</style>

<script>
import { popover } from 'vue-strap';

export default {
  name: 'attribute',
  data() {
    var attrs = require('data/attributes.yaml');
    return {
      attrs: attrs
    };
  },
  props: ['attr'],
  components: {
    popover
  },
}
</script>
