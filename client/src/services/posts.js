import Api from '@/services/api.js'

export default {
  All() {
    return Api.Public().get('/posts/all')
  },
  Following() {
    return Api.JWTAuth().get('/posts/following')
  }
}
