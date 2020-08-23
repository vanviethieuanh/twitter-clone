<template>
  <div>
    <div v-for="post in posts" :key="post.id">
      <Post v-bind:author="post.author" v-bind:post="post.post" class="mb-4" />
    </div>
  </div>
</template>

<script>
import Post from '@/components/Post'
import GetPosts from '@/services/posts.js'

export default {
  name: 'Explore',
  components: {
    Post
  },
  data() {
    return {
      posts: []
    }
  },
  methods: {
    async getPosts() {
      const response = await GetPosts.All()
      this.posts = response.data
    }
  },
  mounted() {
    this.getPosts()
  }
}
</script>

<style></style>
