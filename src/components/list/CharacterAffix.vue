<template>
  <div class="well" style="padding: 8px 0;">
  <ul class="nav nav-list">
  	<li class="nav-header">角色列表</li>
    <li v-for="c in characters"><router-link :to="'/list/' + c.id">{{ c.name }}</router-link></li>
  </ul>
</div>
</template>

<script>
  export default {
    name: 'character-affix',
    props: ['characters'],
  }
</script>
