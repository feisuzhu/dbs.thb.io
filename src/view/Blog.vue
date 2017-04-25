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
  </div>
  </div>
</template>

<script>
  import marked from 'marked'

  export default {
    name: 'Blog',
    data() {
      return {
        blogs: require('data/blogs.yaml'),
      }
    },
    mounted() {
      var url = require('assets/blogs/articles/' + this.blog.id + '.md');
      fetch(url).then((resp) => {
        if(resp.ok) {
          return resp.text();
        }
      }).then((text) => {
          this.$refs.content.innerHTML=marked(text);
      });
    },
    computed: {
      blog() {
        var id = this.$route.params.id;
        return this.blogs.find((b) => b.id == id);
      }
    }
  };
</script>
