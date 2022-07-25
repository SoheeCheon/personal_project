<template>
  <div
    class="card"
    :style="{
      height: tH + 'px',
      gridRowEnd: gap,
      backgroundColor: 'gray',
      borderRadius: '10px'
    }"
  >
    <div class="image">
      <img :src="image.urls.small" class="image" :style="{ width: '100%' }" />
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { round } from 'mathjs'

export default {
  props: {
    image: {
      type: Object,
      required: true
    }
  },
  setup() {
    const tH = ref(null)
    const gap = ref(null)

    onMounted(() => {
        tH.value = round(this.image.height / (this.image.width / 400))
        gap.value = round(this.tH / 10)
        gap.value = `span ${gap.value}`
    })

    return {
        tH,
        gap
    }
  }
}
</script>

<style>

</style>