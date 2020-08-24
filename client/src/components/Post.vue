<template>
  <v-card class="mx-auto pa-1" max-width="600" outlined>
    <v-card-text>
      <v-container class="d-flex ma-0 pa-0 align-center"
        ><a @click="authorInfo">
          <p color="grey darken-4">{{ author }}</p>
        </a>
        <p class="text-caption ml-2 text--disabled">{{ calcTime }}</p>
      </v-container>
      <p class="ma-0">{{ post }}</p>
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
  computed: {
    calcTime() {
      const postTime = new Date(this.time)
      const diff = Date.now() - postTime

      let time = 'now'

      const minutes = Math.round(diff / 60000)
      const hours = Math.round(diff / (60000 * 60))
      const days = Math.round(diff / (60000 * 60 * 24))

      if (minutes == 1) time = `${minutes} min`
      if (minutes > 1) time = `${minutes} mins`
      if (hours == 1) time = `${hours} hour`
      if (hours > 1) time = `${hours} hours`
      if (days == 1) time = `${days} day`
      if (days > 1) time = `${days} days`

      return time
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
    },
    time: {
      type: String,
      default: 'now'
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
