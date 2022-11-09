import axios from 'axios'
import store from '@/store'

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'

var env = process.env.NODE_ENV || 'development';
const domain =  env == 'production' ? 'http://api.local.twitter-clone.vn' : 'http://localhost:8000'

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
