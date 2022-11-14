import axios from 'axios'
import store from '@/store'

axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'

var env = process.env.NODE_ENV || 'development'
const domain =
  env == 'production'
    ? 'http://api.local.twitter-clone.vn'
    : 'http://localhost:8000'

axios.defaults.baseURL = domain
axios.refreshingToken = false

// Authentication interceptor
axios.interceptors.response.use(res => res,
  async (error) => {
    if (error.response.status !== 401)
      return Promise.reject(error);

    let isTokenExpired = store.getters.getTokenExp < Date.now() / 1000
    if (isTokenExpired && !axios.refreshingToken) {
      axios.refreshingToken = true
      const { status, data } = await axios.post(
        'auth/token/refresh',
        {
          "refresh": store.getters.getRefreshToken
        }
      )
      if (status === 200) {
        axios.defaults.headers['Authorization'] = `Bearer ${data.access}`
        return axios(error.config)
      }
      axios.refreshingToken = false
    }

    return error
  })

export default axios