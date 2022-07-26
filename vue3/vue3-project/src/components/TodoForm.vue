<template>
  <div v-if="loading">
    Loading...
  </div>
  <form v-else @submit.prevent="onSave">
    <div class="row">
      <div class="col-6">
          <!-- <div class="form-group">
            <label>Subject</label>
            <input type="text" class="form-control" v-model="todo.subject">
            <div v-if="subjectError" style="color:red" class="mb-3"> {{subjectError}}</div>
          </div> -->
          <Input v-model:subject="todo.subject" label="Subject" :error="subjectError"/>
      </div>
      <div v-if="editing" class="col-6">
        <div class="form-group">
          <label>Status</label>
          <div>
            <button type="button" @click="toggleTodoStatus" class="btn" :class="todo.completed ? 'btn-success' : 'btn-danger' ">{{ todo.completed ? 'Completed' : 'Incompleted' }}</button>
          </div>
        </div>
      </div>
      <div class="col-12 mb-3">
        <div class="form-group">
          <label>Body</label>
          <textarea v-model="todo.body" class="form-control" cols="30" rows="10">

          </textarea>
        </div>
      </div>
    </div>
    
    <button type="submit" class="btn btn-primary m-2" :disabled="!todoUpdated">{{ editing ? 'Update' : 'Create' }}</button>
    <button @click="moveToTodoListPage" class="btn btn-outline-dark" >Cancel</button>
  </form>
  <transition name="fade">
    <ToastAlert v-show="showToast" :message="toastMessage" :type="toastAlertType"/>
  </transition>
</template>

<script>
import {ref, computed, onUpdated } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from '@/axios.js'
import _ from 'lodash'
import ToastAlert from '@/components/ToastAlert.vue'
import { useToast } from '@/composables/toast'
import Input from '@/components/TodoInput.vue'

export default {
  components: {
    ToastAlert,
    Input
  },
  props: {
    editing: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    const route = useRoute()
    const router = useRouter()
    const todo = ref({
      subject: '',
      completed: false,
      body: ''
    })
    const subjectError = ref('')
    const loading = ref(false)
    const todoId = route.params.id
    const originalTodo = ref(null)

    const {
      toastMessage,
      toastAlertType,
      showToast,
      tiggerToast
    } = useToast()

    onUpdated(() => {
      console.log(todo.value.subject)
    })

    const getTodo = async () => {
      loading.value = true
      try {
        const res = await axios.get('todos' + todoId)
        
        todo.value = {...res.data}
        originalTodo.value = {...res.data}

        loading.value = false
      } catch(error) {
        loading.value = false
        console.log(error)
        tiggerToast('Something went wrong', 'danger')
      }
    }

    const todoUpdated = computed(() => {
      return !_.isEqual(todo.value, originalTodo.value)
    })

    const toggleTodoStatus = () => {
      todo.value.completed = !todo.value.completed
    }

    const moveToTodoListPage = () => {
      router.push({
        name: 'Todos'
      })
    }

    const onSave = async () => {
      subjectError.value = ''
      if (!todo.value.subject) {
        subjectError.value = 'Subject is required'
        return
      } 
      try {
        let res
        const data = {
          subject: todo.value.subject,
          completed: todo.value.completed,
          body: todo.value.body
        }
        if (props.editing) {
          res = await axios.put('todos' + todoId, data)
          // 갱신 
          originalTodo.value = {...res.data}
        } else {
          res = await axios.post('todos' , data)
          // 초기화
          todo.value.subject = ''
          todo.value.body = ''
        }

        const message = `SuccessFully` + (props.editing ? ' Updated!' : ' Created!')
       
        tiggerToast(message)
      } catch(error) {
        console.log(error)
        tiggerToast('Something went wrong', 'danger')
      }
      
    }
    
    if (props.editing) {
      getTodo()
    }
    
    return {
      todo,
      loading,
      toggleTodoStatus,
      moveToTodoListPage,
      onSave,
      todoUpdated,
      showToast,
      toastMessage,
      toastAlertType,
      subjectError,
    }
  }
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-30px);
}

.fade-enter-to,
.fade-leave-from {
  opacity: 1;
  transform: translateY(0px);
}
</style>