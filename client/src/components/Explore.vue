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
    <v-container v-if="!posts.length" class="d-flex mx-auto justify-center">
      <p>Let's be the first people there!</p>
    </v-container>
  </div>
</template>

<script>
import Post from '@/components/Post'
import { AllPost } from '@/services/post.js'

export default {
  name: 'Explore',
  components: {
    Post,
  },
  data() {
    return {
      user: {},
      posts: [],
      page: 1,
    }
  },

  methods: {
    getTime() {},

    getPosts() {
      AllPost(this.page ?? 1)
        .then((res) => {
          this.posts = [...this.posts, ...res.data.results]
          this.page++
        })
        .catch((err) => {
          if (err.response.status === 401) {
            this.$router.push('/')
          }
          if (err.response.status === 404) {
            // Stop listen event when end
            window.removeEventListener('scroll', this.onScroll)
          }
        })
    },
    onScroll(e) {
      // this.windowTop = window.top.scrollY
      const listElement = e.target.documentElement
      if (
        listElement.scrollTop + listElement.clientHeight >=
        listElement.scrollHeight
      ) {
        this.getPosts()
      }
    },
  },
  mounted() {
    this.getPosts()
    window.addEventListener('scroll', this.onScroll)
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.onScroll)
  },
}
</script>

<style></style>
