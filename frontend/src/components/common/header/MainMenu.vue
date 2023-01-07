<template>
  <nav class="main-menu">
    <li><router-link class="header" to="/">首页</router-link></li>
    <li>
      <div class="dropdown">
        <a class="header" href="#" data-bs-toggle="dropdown">作品</a>
        <ul class="dropdown-menu">
          <ApolloQuery tag="" :query="episodesQuery">
            <template v-slot="{ result: { data, error }, isLoading }">
              <li v-for="ep in data.episodes" v-if="!isLoading">
                <router-link class="dropdown-item" :to="'/episodes/' + ep.id">{{ ep.title }}</router-link>
              </li>
            </template>
          </ApolloQuery>
          <li><hr class="dropdown-divider"></li>
          <li>
            <router-link class="dropdown-item" to="/episodes">查看全部</router-link>
          </li>
        </ul>
      </div>
    </li>
    <li>
      <div class="dropdown">
        <a class="header" href="#" data-bs-toggle="dropdown">资料</a>
        <ul class="dropdown-menu">
          <li><router-link class="dropdown-item" to="/library">library</router-link></li>
          <li><router-link class="dropdown-item" to="/list">符卡资料</router-link></li>
          <li><router-link class="dropdown-item" to="/rules">决斗规则</router-link></li>
          <li><router-link class="dropdown-item" to="/story">符梦传说</router-link></li>
        </ul>
      </div>
    </li>
    <li><router-link class="header" to="/blogs">公告</router-link></li>
    <li><router-link class="header" to="/contacts">社团</router-link></li>
  </nav>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import gql from 'graphql-tag'

const episodesQuery = gql`
  query Episodes {
    episodes {
      id title
    }
  }
`;

</script>

<style lang="scss">
  .main-menu {
    text-align: right;

    & > li {
      display: inline-block;
      margin: 0 10px;
    }

    a.header {
      color: #313131;
      text-decoration: none;
      cursor: pointer;
      line-height: 18px;
      font-family: Microsoft Yahei,simsun;
      font-weight: 800;
      font-size: 16px;
      text-shadow: none;
      padding: 0;
      text-align: left;

      &:hover {
        /* color: #c5c5c5; */
        color: #313131;
        text-decoration: underline;
      }
    }
  }

/* @media (min-width: 1201px) { */
/*   .menu_wrap{ */
/*       text-align:left; */
/*       padding:0px 4% 0px 0px; */
/*   } */
/* } */
/* @media (min-width: 980px) and (max-width: 1200px) { */
/*   .menu_wrap{ */
/*       text-align:left; */
/*       padding:0px 2% 0px 0px; */
/*   } */
/* } */
/* @media (max-width: 979px) { */
/*   .menu_wrap{ */
/*       text-align:left; */
/*       padding:0px 33.5% 0px 0px; */
/*   } */
/* } */
/* @media (max-width: 480px) { */
/*   .menu_wrap{ */
/*       text-align:left; */
/*       padding:0px 8% 0px 0px; */
/*   } */
/* } */
/* @media (max-width: 414px) { */
/*   .menu_wrap{ */
/*       text-align:left; */
/*       padding:0px 12.6% 0px 0px; */
/*   } */
/* } */
/* @media (max-width: 375px) { */
/*   .menu_wrap{ */
/*       text-align:left; */
/*       padding:0px 8.5% 0px 0px; */
/*   } */
/* } */
/* @media (max-width: 360px) { */
/*   .menu_wrap{ */
/*       text-align:left; */
/*       padding:0px 6% 0px 0px; */
/*   } */
/* } */
/* @media (max-width: 320px) { */
/*   .menu_wrap{ */
/*       text-align:left; */
/*       padding:0px 0px 0px 0px; */
/*       width:105.7% */
/*   } */
/* } */
</style>
