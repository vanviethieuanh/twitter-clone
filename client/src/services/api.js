import axios from 'axios'
import store from '@/store'

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'

const domain = 'http://api.local.twitter-clone.vn' 

export default {
  Public() {
    return axios.create({
      baseURL: domain,
    })
  },
  JWTAuth() {
    return axios.create({
      baseURL: domain,
      headers: { Authorization: `Bearer ${store.getters.getToken}` }
    })
  }
}
