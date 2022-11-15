import Vue from 'vue'
import Vuex from 'vuex'

import base64 from 'base-64'
import axios from '@/services/api.js'

Vue.use(Vuex)

export default new Vuex.Store({
  strict: process.env.NODE_ENV !== 'production',
  state: {
    access_token: null,
    refresh_token: null,
    userFullName: null,
    userEmail: null,
    userId: null,
    tokenExp: null,

    explorePosts: [],
    followingPosts: []
  },
  mutations: {
    setToken(state, {refresh: refresh_token, access: access_token}) {
      state.access_token = access_token
      state.refresh_token = refresh_token

      axios.defaults.headers['Authorization'] = `Bearer ${access_token}`

      const payload_string = base64.decode(access_token.split('.')[1])
      const payload = JSON.parse(payload_string)

      console.log(payload)
      state.userEmail = payload.email
      state.userFullName = payload.first_name + payload.last_name
      state.userId = payload.user_id
      state.tokenExp = payload.exp
    },
    setUserInfo(state, { fullName, email, id }) {
      state.userFullName = fullName
      state.userEmail = email
      state.userId = id
    },
    logOut(state) {
      state.access_token = null
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
    addFollowingPosts(state, posts) {
      state.followingPosts = [...state.followingPosts, ...posts]
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
      return state.access_token !== null
    },
    getAccessToken(state) {
      return state.access_token
    },
    getRefreshToken(state) {
      return state.refresh_token
    },

    getUserFullName(state) {
      return state.userFullName
    },
    getUserEmail(state) {
      return state.userEmail
    },
    getUserId(state) {
      return state.userId
    },
    getTokenExp(state) {
      return state.tokenExp
    }
  }
})
