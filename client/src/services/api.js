import axios from 'axios'
import store from '@/store'

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'

const baseURL = `http://127.0.0.1:8000`

export default {
  Public() {
    return axios.create({
      baseURL: baseURL
    })
  },
  JWTAuth() {
    return axios.create({
      baseURL: baseURL,
      headers: { Authorization: `Bearer ${store.getters.getToken}` }
    })
  }
}
