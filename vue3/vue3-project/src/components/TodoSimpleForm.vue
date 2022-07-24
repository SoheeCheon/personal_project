<template>
  <form @submit.prevent="onSumbit">
    <div class="d-flex">
      <div class="flex-grow-1 mr-2">
        <input classs="form-control" type="text" v-model="todo" placeholder="Type new To-do">
      </div>
      <div class>
        <button class="btn btn-primary" type="submit">Add</button>
      </div>
    </div>
    <div v-if="hasError" style="color:red">This field cannot be empty</div>
  </form>
</template>

<script>
import {ref} from 'vue'

export default {
  emits: ['add-todo'],
  setup(props, {emit}) {
    const hasError = ref(false)
    const todo = ref('')

    const onSumbit = () => {
      if (todo.value == "") {
        hasError.value = true
      } else {
        hasError.value = false
        emit('add-todo', {
          id: Date.now(),
          subject: todo.value,
          completed: false,
        })
        todo.value = ''
      }
    }

    return {
      todo,
      hasError,
      onSumbit
    }
  }
}
</script>

<style>

</style>