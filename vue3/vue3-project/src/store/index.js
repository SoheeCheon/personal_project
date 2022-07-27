import { createStore } from "vuex";

export default createStore({
    state: {
        showToast: false,
        toastMessage: '',
        toastAlertType: '',
        toastTimeOut: null
    }
})