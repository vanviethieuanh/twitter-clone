import axios from 'axios'
import store from '@/store'

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'

// const baseURL = process.env.BACKEND_SERVER

export default {
  Public() {
    return axios.create({
    })
  },
  JWTAuth() {
    return axios.create({
      headers: { Authorization: `Bearer ${store.getters.getToken}` }
    })
  }
}
