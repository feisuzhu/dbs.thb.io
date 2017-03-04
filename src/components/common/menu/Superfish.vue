<template>
  <ul class="sf-menu">
    <slot />
  </ul>
</template>

<script>
import 'superfish'
export default {
  name: 'superfish',
  mounted() {
    $(this.$el).superfish();
  }
}
</script>
