<template>
  <nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <router-link class="navbar-brand" :to="{name:'Home'}">Sohee</router-link>

    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
      <li class="nav-item">
        <router-link class="nav-link active" aria-current="page" to="/todos">Todos</router-link>
      </li>
    </ul>
  </div>
</nav>
<div class="container">
  <router-view/>
</div>
<Toast v-show="showToast" :message="toastMessage" :type="toastAlertType"/>
</template>

<script>
import Toast from'@/components/ToastAlert.vue'
import { useToast } from '@/composables/toast'

export default {
  components: {
    Toast
  },
  setup() {
     const {
      toastMessage,
      toastAlertType,
      showToast,
      tiggerToast
    } = useToast()

    console.log(showToast.value)

    return {
      toastMessage,
      toastAlertType,
      showToast,
      tiggerToast
    }
  }
}
</script>

<style>

</style>