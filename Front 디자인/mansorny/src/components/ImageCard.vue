<template>
  <div
    class="grid-item"
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
import { ref } from 'vue'
import { round } from 'mathjs'

export default {
  props: {
    image: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    const tH = ref(null)
    const gap = ref(null)

    tH.value = round(props.image.height / (props.image.width / 300))
    gap.value = round(tH.value / 10)
    gap.value = `span ${gap.value}`


    return {
        tH,
        gap
    }
  }
}
</script>

<style>

</style>