import { defineStore } from 'pinia'

export const useLogin = defineStore('isLogin', {
  state: () => {
    return { isLogin: false }
  },

  actions: {
    signIn() {
        this.isLogin = true;
    },
    signOut() {
        this.isLogin = false;
    },

  },
})

export const useStore = defineStore('authStore', {
    state: () => ({
        username: '',
        access: '',
        refresh: '',
    }),
    getters: {
        isAuthenticated(state) {
            return Boolean(state.access);
        },
    },
    actions: {
        signOut() {
            this.username = '';
            this.access = '';
            this.refresh = '';
        },
    },
});
