<template>
  <div>
    <div v-for="post in posts" :key="post.id">
      <Post v-bind:author="post.author" v-bind:post="post.post" class="mb-4" />
    </div>
    <v-container v-if="!posts.length" class="d-flex mx-auto justify-center">
      <p>Follow more people to get more post!</p>
    </v-container>
  </div>
</template>

<script>
import Post from '@/components/Post'
import Api from '@/services/api.js'

export default {
  name: 'FollowingTweet',
  components: {
    Post
  },
  data() {
    return {
      posts: []
    }
  },
  methods: {
    getPosts() {
      Api.JWTAuth()
        .get('posts/following')
        .then(res => {
          console.log(res.data)
          this.user = res.data.user
          this.posts = res.data.posts

          const fullName =
            res.data.user.first_name + ' ' + res.data.user.last_name

          this.$store.commit('setUserInfo', {
            fullName: fullName,
            email: res.data.user.username
          })
        })
        .catch(err => {
          if (err.response.status === 401) {
            this.$router.push('/')
          }
        })
    }
  },
  mounted() {
    this.getPosts()
  }
}
</script>

<style></style>
