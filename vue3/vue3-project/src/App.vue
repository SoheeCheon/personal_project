<template>
  <div>{{ name }}</div>
  <input type="text" v-model="name">
  <button class="btn btn-primary" @click="onSumbit">Click</button>
</template>

<script>
import { ref } from 'vue'
// import { reactive } from 'vue'

export default {
  setup() {
    const name = ref('Sohee')

    const onSumbit = () => {
      console.log(name.value)
    }
    
    return {
      name,
      onSumbit,
    }
  },
}
</script>

<style>
.name {
  color: red;
}

.blue {
  color: blue
}
</style>