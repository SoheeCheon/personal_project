<template>
  <masonry-wall :images="images" :ssr-columns="1" :column-width="300" :padding="16">
    <template #default="{ image }">
      <img :src="image.urls.small" class="image" :style="{ width: '100%' }" />
    </template>
  </masonry-wall>
</template>

<script>
// import ImageCardList from '@/components/ImageCardList.vue'
import { onMounted, ref } from 'vue'
import axios from 'axios'
import VueMasornyWall from '@/vue-masorny-wall.vue'

export default {
  setup() {
    const images = ref([])

    const getRandomImages = async (count) => {
      try {
        const res = await axios.get(process.env.VUE_APP_URL + 'photos/random/', {
          headers: {
            Authorization: 'Client-ID ' + process.env.VUE_APP_ACCESS_KEY
          },
          params: {
            count
          }
        })
        // Binding data to this component data
        images.value = res.data
        console.log(res.data)
      } catch (error) {
        console.error(error)
      }
    }

    onMounted(() => {
      getRandomImages(30)
    })    

    return {
      images
    }
  }
}
</script>

<style>
* { box-sizing: border-box; }

body { font-family: sans-serif; }

/* ---- grid ---- */

.grid {
  background: #EEE;
  max-width: 1200px;
}

/* clearfix */
.grid:after {
  content: '';
  display: block;
  clear: both;
}

/* ---- grid-item ---- */

.grid-sizer,
.grid-item {
  width: 20%;
}

.grid-item {
  height: 120px;
  float: left;
  background: #D26;
  border: 2px solid #333;
  border-color: hsla(0, 0%, 0%, 0.5);
  border-radius: 5px;
}
</style>
