import Api from '@/services/api.js'

export default {
  UserInfo(userId) {
    return Api.JWTAuth().get('/auth/user-info', {
      params: { id: userId }
    })
  },
  CheckUsedEmail(email) {
    return Api.Public().post('used/email', {
      email: email
    })
  }
}
