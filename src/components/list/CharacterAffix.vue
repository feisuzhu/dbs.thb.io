<template>
  <ul>
    <li v-for="c in cards"><router-link :to="'/list/' + c.id">{{ c.name }}</router-link></li>
  </ul>
</template>

<script>
  export default {
    name: 'character-affix',
    props: ['cards'],
  }
</script>
