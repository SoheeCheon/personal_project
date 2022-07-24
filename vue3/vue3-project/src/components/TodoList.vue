<template>
  <div class="card mt-2" v-for="(todo, index) in todos" :key="todo.id">
    <div class="card-body p-2 d-flex align-items-center" style="cursor: pointer" @click="moveToPage(todo.id)">
      <div class="flex-grow-1">
        <input class="mx-2" :checked="todo.completed" type="checkbox" @change="toggleTodo(index, $event)" @click.stop>
        <span :class="{ todo: todo.completed}">{{ todo.subject }}</span>
      </div>
      <div>
        <button class="btn btn-danger btn-sm" @click.stop="openModal(todo.id)">Delete</button>
      </div>
    </div>
  </div>
  <teleport to="#modal">
    <Modal v-if="showModal" @close="closeModal" @delete="deleteTodo"/>
  </teleport>
</template>

<script>
import { useRouter } from 'vue-router'
import Modal from '@/components/DeleteModal.vue'
import { ref } from 'vue'

export default {
  components: {
    Modal
  },
  props: {
    todos: {
      type: Array,
      required: true,
    }
  },
  emits: ['toggle-todo', 'delete-todo'],
  setup(props, {emit}) {
    const router = useRouter()
    const todoDeleteId = ref(null)
    const showModal = ref(false)
    
    const openModal = (id) => {
      showModal.value = true
      todoDeleteId.value = id
    }

    const closeModal = () => {
      showModal.value = false
      todoDeleteId.value = null
    }

    const deleteTodo = () => {
      emit('delete-todo', todoDeleteId.value);
      showModal.value = false
      todoDeleteId.value = null
    }

    const toggleTodo = (index, event) => {
      emit('toggle-todo', index, event.target.checked);
    }

    const moveToPage = (todoId) => {
      router.push('/todos/' + todoId)
    }

    return {
      deleteTodo,
      toggleTodo,
      moveToPage,
      showModal,
      openModal,
      closeModal
    }
  }
}
</script>

<style>

</style>