<template>
  <div>
    <div class="d-flex justify-content-between m-3">
      <h2>To-Do List</h2>
      <button class="btn btn-primary" @click="moveToCreatePage">Create Todo</button>
    </div>
  <div class="flex-grow-1 mr-2">
    <input classs="form-control" type="text" v-model="searchText" placeholder="Search" @keyup.enter="searchTodo">
  </div>
  <hr>
  
  <div v-if="!todos.length">
    조건에 맞는 할일이 없습니다.
  </div>
  <TodoList :todos="todos" @toggle-todo="toggleTodo" @delete-todo="deleteTodo"/>
  <hr>
  <PaginationBar v-if="todos.length" :numberOfPages="numberOfPages" :currentPage="currentPage" @click="getTodos"/>
</div>
</template>

<script>
import { ref, computed, watch } from 'vue'
import TodoList from '@/components/TodoList.vue'
import axios from '@/axios'
import { useToast } from '@/composables/toast'
import { useRouter } from 'vue-router'
import PaginationBar from '@/components/PaginationBar.vue'

// import { reactive } from 'vue'

export default {
  components: {
    TodoList,
    PaginationBar
  },
  setup() {
    const todos = ref([])
    const error = ref('')
    const numberOfTodos = ref(0)
    const limit = 5
    const currentPage = ref(1)
    const router = useRouter()
    const searchText = ref('')
    let timeout = null

    const {
      toastMessage,
      toastAlertType,
      showToast,
      tiggerToast
    } = useToast()

    const searchTodo = () => {
      clearTimeout(timeout)
      getTodos(1)
    }

    watch(searchText, () => {
      clearTimeout(timeout)
      timeout = setTimeout(() => {
        getTodos(1)
      }, 2000)
    })

    const numberOfPages = computed(() => {
      // 올림을 하기위해 사용
      return Math.ceil(numberOfTodos.value / limit)
    })


    const getTodos = async (page = currentPage.value) => {
      try {
        const res = await axios.get(`todos?_sort=id&_order=desc&subject_like=${searchText.value}&_page=${page}&_limit=${limit}`)
        numberOfTodos.value = res.headers['x-total-count']
        todos.value = res.data
        currentPage.value = page
      } catch(err) {
        tiggerToast('Something went wrong', 'danger')
      } 
    }

    getTodos()

    const addTodo = async (todo) => {
      // 데이터베이스에 저장
      error.value = ""
      try{
        await axios.post('todos', {
          subject: todo.subject,
          completed: todo.completed,
        })
        getTodos(1)
        // todos.value.push(res.data)
      } catch (err) {
        tiggerToast('Something went wrong', 'danger')
      }
    }
    
    const toggleTodo = async (index, checked) => {
      console.log(checked)
      error.value = ""
      const id = todos.value[index].id
      try {
        await axios.patch('todos/' + id, {
          completed: checked
        })
        todos.value[index].completed = checked
      } catch (err) {
        console.log(err)
        tiggerToast('Something went wrong', 'danger')
      }
    }
    
    const deleteTodo = async (id) => {
      error.value = ""
      try {
        await axios.delete('todos/' + id)
        getTodos(1)
      } catch (err) {
        console.log(err)
        tiggerToast('Something went wrong', 'danger')
      }
    }

    const moveToCreatePage = () => {
      router.push({
        name: 'TodoCreate',
      })
    }

    return {
      todos,
      searchText,
      getTodos,
      addTodo,
      toggleTodo,
      deleteTodo,
      searchTodo,
      error,
      numberOfPages,
      currentPage,
      toastMessage,
      toastAlertType,
      showToast,
      moveToCreatePage
    }
  },
}
</script>

<style>
.todo {
  color: gray;
  text-decoration: line-through;
}
</style>