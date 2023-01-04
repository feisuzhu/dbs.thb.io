<template>
  <div class="page_container">
    <div class="breadcrumb">
      <div class="wrap">
        <div class="container"> <a href="#">首页</a><span>/</span><a href="#/library">资料库</a><span>/</span>决斗规则</div>
      </div>
    </div>
    <div class="wrap">
      <div class="container">
        <section>
          <div ref="content" class="rules-text">
            Loading...
          </div>
        </section>
      </div>
    </div>
  </div>

</template>

<style>

.rules-text {
  color: #555555;
  padding-left: 50px;
  padding-right: 50px;
  padding-bottom: 50px;
}

.rules-text h1 {
  font-size: 25px;
  text-align: center;
}

.rules-text h2 {
  font-size: 15px;
}

.rules-text p {
  font-size: 12px;
  line-height: 24px;
}

.rules-text p img {
  text-align: center;
}

.rules-text li {
  font-size: 12px;
  line-height: 24px;
}

.rules-text img {
  max-width: 120px;
  padding-left: 10px;
  padding-right: 10px;
  padding-bottom: 10px;
}



</style>

<script setup>
  const content = ref(null);

  onMounted(() => {
    var url = require('assets/rules/dbs-rules.md');
    fetch(url).then((resp) => {
      if(resp.ok) {
        return resp.text();
      }
    }).then((text) => {
        content.value.innerHTML=text;
    });
  });
</script>
