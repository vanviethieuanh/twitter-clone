import Api from '@/services/api.js'

export default {
  CheckFollowing(userId) {
    return Api.JWTAuth().get('/follow', {
      params: { following_id: userId }
    })
  },
  Follow(userId) {
    return Api.JWTAuth().post('follow', null, {
      params: { id: userId }
    })
  },
  Unfollow(userId) {
    return Api.JWTAuth().delete('follow', {
      params: { id: userId }
    })
  }
}
