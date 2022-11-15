import axios from './api'

export const AllPost = async function (page = 1) {
  return await axios.get('posts/all',
    {
      params: {
        page: page
      }
    })
}

export const FollowingPost = async function (page = 1) {
  return await axios.get('posts/following', {
    params: {
      page: page
    }
  })
}

export const Post = async function (post) {
  return await axios.post('posts', {
    post: post
  })
}
