<template>
  <div class="page_container">
    <div class="breadcrumb">
      <div class="wrap">
        <div class="container"> <a href="#">首页</a><span>/</span>资料库</div>
      </div>
    </div>
    <div class="wrap planning">
    <div class="container">
      <div class="row">
        <div class="span4">
          <router-link to="/list">
            <span class="link_title">符卡资料</span>
            <span class="img_icon icon4"></span>
            <p style="text-align:center">点此进入，使用侧边栏切换角色</p>
          </router-link>
        </div>
        <div class="span4">
            <router-link to="/rules">
              <span class="link_title">决斗规则</span>
              <span class="img_icon icon4"></span>
              <p style="text-align:center">施工中</p>
            </router-link>
          </div>
          <div class="span4">
          <router-link to="/list">
            <span class="link_title">背景故事</span>
            <span class="img_icon icon4"></span>
            <p style="text-align:center">施工中</p>
          </router-link>
        </div>
      </div>
      <h2>少女施工中...</h2>
    </div>
  </div>
  </div>
  </div>
  </div>
</template>

<script>
  export default {
    name: 'Library',
    }
</script>
