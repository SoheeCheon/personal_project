<template>
  <h1>Home Page</h1>
  <h2>{{ count }}</h2>
  <button @click="count++">Add</button>
</template>

<script>
import { useCount } from '@/composables/count'

export default {
  setup() {
    const { count } = useCount()

    return {
      count
    }
  }

}
</script>

<style>

</style>