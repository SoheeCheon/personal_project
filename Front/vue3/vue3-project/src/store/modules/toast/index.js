export default {
  namespaced: true,
  state: {
    toasts:[],
    // showToast: false,
    // toastMessage: '',
    // toastAlertType: '',
  },
  mutations: {
    UPDATE_TOAST_MESSAGE(state, payload) {
        state.toastMessage = payload
    },
    UPDATE_TOAST_ALERT_TYPE(state, payload) {
        state.toastAlertType = payload
    },
    UPDATE_TOAST_STATUS(state, payload) {
        state.showToast = payload
    },
    ADD_TOAST(state, payload) {
      state.toasts.push(payload)
    },
    REMOVE_TOAST(state) {
      // 첫번째 값이 먼저 추가되었기에 먼저 삭제해준다.
      state.toasts.shift()
    },
  },
  actions: {
    tiggerToast({commit}, payload){
      // commit('UPDATE_TOAST_MESSAGE', message)
      // commit('UPDATE_TOAST_ALERT_TYPE', type)
      // commit('UPDATE_TOAST_STATUS', true)
      commit('ADD_TOAST', {
        id: Date.now(),
        message: payload.message,
        type: payload.type,
      })
      setTimeout(() => {
        // commit('UPDATE_TOAST_MESSAGE', '')
        // commit('UPDATE_TOAST_STATUS', false)
        // commit('UPDATE_TOAST_ALERT_TYPE', '')
        commit('REMOVE_TOAST')
      }, 3000)
    }
  },
  getters: {
      toastMessageWithSmile (state) {
          return state.toastMessage + '^^'
      }
  },
}