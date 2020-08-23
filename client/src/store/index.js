import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    JWTtoken: ''
  },
  mutations: {
    setToken(state, token) {
      state.JWTtoken = token
    }
  },
  actions: {},
  modules: {},
  getters: {
    isLoggedin(state) {
      return state.JWTtoken === ''
    },
    getToken(state) {
      return state.JWTtoken
    }
  }
})
