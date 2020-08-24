<template>
  <v-card class="mx-auto pa-1" max-width="600" outlined>
    <v-card-text>
      <a @click="authorInfo">
        <p color="grey darken-4">{{ author }}</p>
      </a>
      <p class="mb-0">{{ post }}</p>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  model: {
    event: 'view-author'
  },
  methods: {
    authorInfo() {
      this.$parent.$emit('view-author', this.author_id)
    }
  },
  props: {
    author: {
      type: String,
      default: 'Author'
    },
    author_id: {
      type: Number,
      default: -1
    },
    post: {
      type: String,
      default: `Lorem ipsum dolor sit amet consectetur adipisicing elit. Sunt, commodi
        quo. Neque cumque ut quas omnis ex eligendi animi doloribus facere sit
        suscipit mollitia, officiis est, et minus earum architecto.`
    }
  }
}
</script>

<style lang="scss" scoped>
a {
  p {
    color: #424242 !important;
    font-weight: bold;
  }
}
</style>
