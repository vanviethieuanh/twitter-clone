<template>
  <v-container grid-list-xs>
    <v-card> </v-card>
  </v-container>
</template>

<script>
// "username": "accodius@vanviet.clan",
// "first_name": " de Van",
// "last_name": "Accodius",
// "posts": 2,
// "followers": 1,
// "followings": 0
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

<style></style>
