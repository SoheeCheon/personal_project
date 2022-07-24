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
  
</template>

<script>
export default {

}
</script>

<style>

</style>