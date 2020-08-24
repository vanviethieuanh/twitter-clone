import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  strict: process.env.NODE_ENV !== 'production',
  state: {
    JWTtoken: null,
    userFullName: null,
    userEmail: null,
    userId: null
  },
  mutations: {
    setToken(state, token) {
      state.JWTtoken = token
    },
    setUserInfo(state, { fullName, email, id }) {
      state.userFullName = fullName
      state.userEmail = email
      state.userId = id
    }
  },
  actions: {
    setToken({ commit }, token) {
      commit('setToken', token)
    }
  },
  modules: {},
  getters: {
    isLoggedin(state) {
      return state.JWTtoken !== null
    },
    getToken(state) {
      return state.JWTtoken
    },
    getUserFullName(state) {
      return state.userFullName
    },
    getUserEmail(state) {
      return state.userEmail
    },
    getUserId(state) {
      return state.userId
    }
  }
})
