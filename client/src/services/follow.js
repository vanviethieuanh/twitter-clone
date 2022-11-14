import axios from './api'


export const CheckFollowing = async function (userId) {
  return await axios.get('follow', {
    params: { following_id: userId }
  })
}

export const Follow = async function (userId) {
  return await axios.post('follow', null, {
    params: { id: userId }
  })
}

export const Unfollow = async function (userId) {
  return await axios.delete('follow', {
    params: { id: userId }
  })
}
