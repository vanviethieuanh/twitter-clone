<template>
  <v-container class="container">
    <v-container class="d-flex  pa-0 mt-10 align-center">
      <p class="font-weight-light text-h5 mb-0 mr-5">
        {{ userInfo.first_name }} {{ userInfo.last_name }}
      </p>
      <v-btn
        depressed
        small
        color="blue darken-1 white--text"
        class="ma-0"
        :disabled="isDisableFollowButton"
        @click="follow"
        :outlined="userInfo.is_following"
        >{{ followButtonText }}</v-btn
      >
    </v-container>
    <p class="font-weight-medium text-subtitle-1 pt-0">
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
  computed: {
    isDisableFollowButton() {
      const isThisUser = this.userId === this.$store.getters.getUserId

      return isThisUser
    },
    followButtonText() {
      const isThisUser = this.userId === this.$store.getters.getUserId
      const isFollowing = this.userInfo.is_following
      if (!isThisUser && isFollowing) return 'Unfollow'
      else return 'Follow'
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
    },
    follow() {
      const isFollowing = this.userInfo.is_following
      if (!isFollowing) {
        Api.JWTAuth()
          .post('follow/follow', {
            follow_id: this.userId
          })
          .then(() => {
            this.userInfo.is_following = true
            this.userInfo.followers++
          })
          .catch(error => {
            if (error.response.status === 401) {
              this.$router.push('/')
            }
          })
      } else {
        Api.JWTAuth()
          .post('follow/unfollow', {
            follow_id: this.userId
          })
          .then(() => {
            this.userInfo.is_following = false
            this.userInfo.followers--
          })
          .catch(error => {
            if (error.response.status === 401) {
              this.$router.push('/')
            }
          })
      }
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
