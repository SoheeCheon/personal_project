import { createRouter, createWebHistory } from 'vue-router'
import mainHome from '../pages/mainIndex.vue'
import todosHome from '../pages/todos/todosIndex.vue'
import Todo from '../pages/todos/_id.vue'
import TodoCreate from '../pages/todos/create/createIndex.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: mainHome
    },
    {
      path: '/todos',
      name: 'Todos',
      component: todosHome
    },
    {
      path: '/todos/create',
      name: 'TodoCreate',
      component: TodoCreate
    },
    {
      path: '/todos/:id',
      name: 'Todo',
      component: Todo
    },
  ]
})

export default router