<template>
  <nav class="sticky-top">
    <div class="container">
      <div class="row">
        <div class="col-auto">
          <a href="#" @click="$router.back()">
            <icon-delete-left />
          </a>
        </div>
        <div class="col-auto card-name">擦科个东方</div>
        <div class="col" style="padding: 0"></div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!prevCollectionLink">
            <icon-chevrons-left />
          </i>
          <router-link :to="prevCollectionLink" v-else>
            <icon-chevrons-left />
          </router-link>
        </div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!prevCardLink">
            <icon-chevron-left />
          </i>
          <router-link :to="prevCardLink" v-else>
            <icon-chevron-left />
          </router-link>
        </div>
        <div class="col-auto col-md-2 text-center">
          <div class="sku">{{ sku }}</div>
        </div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!nextCardLink">
            <icon-chevron-right />
          </i>
          <router-link :to="nextCardLink" v-else>
            <icon-chevron-right />
          </router-link>
        </div>
        <div class="col-auto text-end">
          <i class="no-more" v-if="!nextCollectionLink">
            <icon-chevrons-right />
          </i>
          <router-link :to="nextCollectionLink" v-else>
            <icon-chevrons-right />
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<style lang="scss">
  nav {
    .sku {
      transform: translate(0, -3px);
    }

    .no-more {
      color: #555;
    }

    @media (max-width: 376px) {
      .row > div {
        padding: 0 6px;
      }
    }
  }
</style>

<script setup>
import IconDeleteLeft from '@/assets/fa-delete-left.svg?component';
import IconChevronLeft from '@/assets/chevron-left.svg?component';
import IconChevronRight from '@/assets/chevron-right.svg?component';
import IconChevronsLeft from '@/assets/chevrons-left.svg?component';
import IconChevronsRight from '@/assets/chevrons-right.svg?component';

const props = defineProps({
  sku: { type: String, required: true, },
  name: { type: String, required: true, },
  prevCollectionLink: { type: String, required: true, },
  nextCollectionLink: { type: String, required: true, },
  prevCardLink: { type: String, required: true, },
  nextCardLink: { type: String, required: true, },
});
</script>
