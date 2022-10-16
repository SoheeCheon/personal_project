<template>
  <div class="form-group">
    <label>{{ label }}</label>
    <input type="text" class="form-control" :value="subject" @input="onInput">
    <div v-if="error" class="text-color mb-3"> {{error}}</div>
  </div>
</template>

<script>
export default {
  props: {
    label: {
      type:String,
      required: true
    },
    error: {
      type:String,
      required: true
    },
    subject: {
      type:String,
      required: true
    },
  },
  setup(props, {emit}) {
    const onInput = (e) => {
      emit('update:subject', e.target.value)
    }

    return {
      onInput
    }
  }
}
</script>

<style scoped> 
  .text-color {
    color:red;
  }
</style>