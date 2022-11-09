<template>
  <div>
    <div v-for="post in posts" :key="post.id">
      <Post
        v-bind:author="post.author_username"
        v-bind:post="post.post"
        v-bind:author_id="post.author"
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
          this.$store.commit('setExplorePosts', res.data.results)
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
