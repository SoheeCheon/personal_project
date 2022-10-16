<template>
  <ImageCardList :images="ImangeList"/>
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
		// 받아온 이미지를 저장하는 객체
    const ImangeList = ref([])
		
		// 랜덤 이미지를 가져오는 함
    const getRandomImages = async (count) => {
      try {
        const res = await axios.get(
          process.env.VUE_APP_URL + '/photos/random',
          {
            headers: {
              Authorization: 'Client-ID ' + process.env.VUE_APP_ACCESS_KEY
            },
            params: {
              count
            }
          }
        )
        // 받아온 데이터를 저장
        ImangeList.value = res.data
        console.log(ImangeList.value)
      } catch (error) {
        console.error(error)
      }
    } 

  // 이미지 가져오기
  getRandomImages(30)
	

  return {
    ImangeList
  }
  }
}
</script>

<style>

</style>
