<template>
  <ImageCardList :images="images"/>
</template>

<script>
import ImageCardList from '@/components/ImageCardList.vue'
import { ref } from 'vue'
import axios from 'axios'

export default {
  components: {
    ImageCardList
  },
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

    getRandomImages(30)

    return {
      images
    }
  }
}
</script>

<style>
</style>
