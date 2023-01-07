<template>
  <div class="page_container">
    <div class="breadcrumb">
      <div class="wrap">
        <div class="container"> <a href="#">首页</a><span>/</span>公告</div>
      </div>
    </div>
    <div class="wrap">
      <div class="container">
        <section>
          <h2 class="title"><span>{{blog.title}}</span></h2>
          <img :src="require('assets/blogs/title-images/' + blog.id + '.jpg')" alt="" />
          <div ref="content">
            Loading...
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
  import { ref, onMounted } from 'vue';

  const blogs = require('data/blogs.yaml');
  const content = ref(null);

  onMounted(() => {
    var url = require('assets/blogs/text/' + this.blog.id + '.md');
    fetch(url).then((resp) => {
      if(resp.ok) {
        return resp.text();
      }
    }).then((text) => {
        content.value.innerHTML=marked(text);
    });
  });

    /* computed: { */
    /*   blog() { */
    /*     var id = this.$route.params.id; */
    /*     return this.blogs.find((b) => b.id == id); */
    /*   } */
    /* } */
</script>
