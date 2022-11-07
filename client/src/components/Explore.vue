<template>
  <div>
    <div v-for="post in posts" :key="post.id">
      <Post
        v-bind:author="post.author"
        v-bind:post="post.post"
        v-bind:author_id="post.author_id"
        v-bind:time="post.post_date"
        class="mb-4"
      />
    </div>
    <v-container v-if="!posts.length" class="d-flex mx-auto justify-center">
      <p>Let's be the first people there!</p>
    </v-container>
  </div>
</template>

<script>
import Post from '@/components/Post'
import Api from '@/services/api.js'

export default {
  name: 'Explore',
  components: {
    Post
  },
  data() {
    return {
      user: {}
    }
  },
  computed: {
    posts() {
      return this.$store.getters.getExplorePosts
    }
  },
  methods: {
    getTime() {},

    getPosts() {
      Api.JWTAuth()
        .get('posts/all')
        .then(res => {
          // console.log(res.data)
          // this.user = res.data.user
          this.$store.commit('setExplorePosts', res.data.results)

          // const fullName =
          //   res.data.user.first_name + ' ' + res.data.user.last_name

          // this.$store.commit('setUserInfo', {
          //   fullName: fullName,
          //   email: res.data.user.username,
          //   id: res.data.user.id
          // })
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
