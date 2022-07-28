<template>
  <Navbar/>
  <div class="container">
    <router-view/>
  </div>
  <Toast/>
</template>

<script>
import Toast from'@/components/ToastAlert.vue'
import Navbar from '@/components/NavBar.vue'

export default {
  components: {
    Toast,
    Navbar
  },
  setup() {
  }
}
</script>

<style scoped>

</style>