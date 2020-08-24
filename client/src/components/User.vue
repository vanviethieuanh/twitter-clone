<template>
  <v-container class="container">
    <p class="font-weight-light text-h4">
      {{ userInfo.first_name }} {{ userInfo.last_name }}
    </p>
    <p class="font-weight-medium text-subtitle-1">
      {{ userInfo.username }}
    </p>
    <v-container class="d-flex justify-space-between pa-0">
      <p>
        <b>{{ userInfo.posts }}</b> posts
      </p>
      <p>
        <b>{{ userInfo.followers }}</b> followers
      </p>
      <p>
        <b>{{ userInfo.followings }}</b> following
      </p>
    </v-container>
    <v-btn
      depressed
      small
      color="blue darken-1 white--text"
      class="ma-0"
      :disabled="userId === this.$store.getters.getUserId"
      >Follow</v-btn
    >
  </v-container>
</template>

<script>
import Api from '@/services/api.js'

export default {
  data() {
    return {
      userInfo: {}
    }
  },
  props: {
    userId: {
      type: Number,
      default: -1
    }
  },
  methods: {
    getInfo() {
      Api.JWTAuth()
        .post('user/info', {
          user_id: this.userId
        })
        .then(response => {
          this.userInfo = response.data
        })
        .catch(error => {
          if (error.response.status === 401) {
            this.$router.push('/')
          }
        })
    }
  },
  mounted() {
    this.getInfo()
  }
}
</script>
<style lang="scss" scoped>
.container {
  max-width: 400px;
}
</style>
