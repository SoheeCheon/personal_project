import { computed, onUnmounted } from 'vue'
import { useStore } from 'vuex'

export const useToast = () => {
  const store = useStore()
  const showToast = computed(() => store.state.showToast)
  const toastMessage = computed(() => store.state.toastMessage)
  const toastAlertType = computed(() => store.state.toastAlertType)
  const toastTimeOut = computed(() => store.state.toastTimeOut)

  const tiggerToast = (message,type = 'success') => {
    showToast.value = true
    toastMessage.value = message
    toastAlertType.value = type
    toastTimeOut.value = setTimeout(() => {
      toastMessage.value = false
      toastMessage.value = ''
      toastAlertType.value = ''
    },3000)

    onUnmounted(() => {
      clearTimeout(toastTimeOut.value)
    })
  }

  return {
    toastMessage,
    toastAlertType,
    showToast,
    tiggerToast
  }
}