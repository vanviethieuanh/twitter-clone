import Api from '@/services/api.js'

export default {
  AllPost() {
    return Api.JWTAuth().get('posts/all')
  },

  FollowingPost() {
    return Api.JWTAuth().get('posts/following')
  },

  Post(post) {
    return Api.JWTAuth().post('posts', {
      post: post
    })
  }
}
