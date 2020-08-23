<template>
  <v-card class="mx-auto pa-1" max-width="600" outlined>
    <v-card-text>
      <p class="mb-3 font-weight-bold">{{ author }}</p>
      <p class="mb-0">{{ post }}</p>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    author: {
      type: String,
      default: 'Author'
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

<style></style>
