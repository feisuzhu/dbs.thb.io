<template>
  <div class="well" style="padding: 8px 0;">
  <ul class="nav nav-list">
  	<li class="nav-header">角色列表</li>
    <router-link :to="'/list/' + c.id" exact active-class="active" tag="li" v-for="c in characters"><a>{{ c.name }}</a></router-link>
  </ul>
</div>
</template>

<script>
  export default {
    name: 'character-affix',
    props: ['characters'],
  }
</script>
