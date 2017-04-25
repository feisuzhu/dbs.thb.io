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
          <div class="row">
            <div class="span8">
              <div class="post" v-for="blog in blogs">
                <router-link :to="'/blog/' + blog.id">
                   <h2 class="title"><span>{{blog.title}}</span></h2>
                   <img :src="require('assets/blogs/title-images/' + blog.id + '.jpg')" alt="" />
                </router-link>
                <div class="post_info">
                  <div class="fleft">发表日期： <span>{{blog.time}}</span></div>
                  <div class="fright">{{blog.category}}</div>
                  <div class="clear"></div>
                </div>
                </br>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  </div>
  </div>
  </div>
</template>

<script>
  export default {
    name: 'BlogList',
    data() {
      return {
        blogs: require('data/blogs.yaml'),
      }
    }
  }
</script>
