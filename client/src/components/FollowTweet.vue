<template>
  <div>
    <div v-for="post in posts" :key="post.id">
      <Post
        v-bind:author="post.author_email"
        v-bind:post="post.post"
        v-bind:author_id="post.author"
        v-bind:time="post.post_date"
        class="mb-4"
      />
    </div>
    <v-container v-if="!posts.count" class="d-flex mx-auto justify-center">
      <p>Follow more people to get more post!</p>
    </v-container>
  </div>
</template>

<script>
import Post from '@/components/Post'
import { FollowingPost } from '@/services/post.js'

export default {
  name: 'FollowingTweet',
  components: {
    Post,
  },
  data() {
    return {
      user: {},
    }
  },
  computed: {
    posts() {
      return this.$store.getters.getFollowingPosts
    },
  },
  methods: {
    getPosts() {
      FollowingPost()
        .then((res) => {
          this.$store.commit('setFollowingPosts', res.data.results)
        })
        .catch((err) => {
          console.log(err.response)
          if (err.response.status === 401) {
            this.$router.push('/')
          }
        })
    },
  },
  mounted() {
    this.getPosts()
  },
}
</script>

<style></style>
