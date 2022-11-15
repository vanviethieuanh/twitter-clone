import axios from './api'

export const UserInfo = async function (userId) {
  return await axios.get('/auth/user-info', {
    params: { id: userId }
  })
}

export const CheckUsedEmail = async function (email) {
  return await axios.post('used/email', {
    email: email
  })
}
