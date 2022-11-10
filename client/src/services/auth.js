import Api from '@/services/api.js'

export default{
  Login(username, password)
  {
      return Api.Public()
      .post('auth/token', {
        username: username,
        password: password
      })
  },

  CheckUsedEmail(email)
  {
    return Api.Public()
    .post('used/email', {
      email: email
    })
  },

  Register({last_name, first_name,email, password, username}){
    return Api.Public()
    .post('auth/register', {
      last_name: last_name,
      first_name: first_name,
      email: email,
      password: password,
      username: username
    })
  }
} 