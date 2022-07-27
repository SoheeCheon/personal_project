<template>
  <div class="wrapper">
    <div class="heading">
      <h1>Masonry Layout Design Examples</h1>
    </div>
    <div class="cards" v-if="images.length">
      <image-card v-for="image in images" :key="image.id" :image="image" />
    </div>
    <div class="cards-loading" v-else>Loading image....</div>
  </div>
</template>

<script>
import ImageCard from '@/components/ImageCard.vue'

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
    
  }
}


    
</script>

<style>
.wrapper .cards {
  display: grid;
  column-gap: 10px;
  row-gap: 7px;
  grid-template-columns: repeat(4, 300px);
  justify-content: center;
  max-width: var(--card-container-width);
}
</style>