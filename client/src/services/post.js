import axios from './api'

export const AllPost = async function () {
  return await axios.get('posts/all')
}

export const FollowingPost = async function () {
  return await axios.get('posts/following')
}

export const Post = async function (post) {
  return await axios.post('posts', {
    post: post
  })
}
