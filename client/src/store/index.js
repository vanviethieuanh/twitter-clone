import Vue from 'vue'
import Vuex from 'vuex'

import base64 from 'base-64'

Vue.use(Vuex)

export default new Vuex.Store({
  strict: process.env.NODE_ENV !== 'production',
  state: {
    JWTtoken: null,
    userFullName: null,
    userEmail: null,
    userId: null,

    explorePosts: [],
    followingPosts: []
  },
  mutations: {
    setToken(state, token) {
      state.JWTtoken = token
      
      const payload_string = base64.decode(token.split('.')[1])
      const payload = JSON.parse(payload_string)

      console.log(payload)
      state.userEmail = payload.email
      state.userFullName = payload.first_name + payload.last_name
      state.userId = payload.user_id
    },
    setUserInfo(state, { fullName, email, id }) {
      state.userFullName = fullName
      state.userEmail = email
      state.userId = id
    },
    logOut(state) {
      state.JWTtoken = null
      state.userEmail = null
      state.userFullName = null
      state.userId = null
    },
    addPost(state, post) {
      state.explorePosts.unshift(post)
    },
    setExplorePosts(state, posts) {
      state.explorePosts = posts
    },
    setFollowingPosts(state, posts) {
      state.followingPosts = posts
    }
  },
  actions: {
    setToken({ commit }, token) {
      commit('setToken', token)
    }
  },
  modules: {},
  getters: {
    getExplorePosts(state) {
      return state.explorePosts
    },
    getFollowingPosts(state) {
      return state.followingPosts
    },

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
