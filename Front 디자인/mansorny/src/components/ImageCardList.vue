<template>
  <div class="wrapper">
    <div class="heading">
      <h1>Masonry Layout Design Examples</h1>
    </div>
    <div class="grid" v-if="images.length">
      <div class="grid-sizer"></div>
      <ImageCard v-for="image in images" :key="image.id" :image="image" />
    </div>
    <div class="cards-loading" v-else>Loading image....</div>
  </div>
</template>

<script>
import ImageCard from '@/components/ImageCard.vue'
import { createApp } from 'vue'
import MasonryWall from '@yeger/vue-masonry-wall'

export default {
  components:{
    ImageCard
  },
  props: {
    images: {
      type: Array,
      require: true
    }
  },
  setup() {
    const app = createApp()

    app.use(MasonryWall)

  }
}


    
</script>

<style>


</style>