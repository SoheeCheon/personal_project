import { ref, onUnmounted } from 'vue'

export const useToast = () => {
  const showToast = ref(false)
  const toastMessage = ref('')
  const toastAlertType = ref('')
  const toastTimeOut = ref(null)

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