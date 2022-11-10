<template>
  <v-container class="container">
    <v-container class="d-flex pa-0 mt-10 align-center">
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
      {{ userInfo.email }}
    </p>
    <v-container class="d-flex justify-space-between pa-0">
      <p>
        <b>{{ userInfo.post_count }}</b> posts
      </p>
      <p>
        <b>{{ userInfo.follower_count }}</b> followers
      </p>
      <p>
        <b>{{ userInfo.following_count }}</b> following
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
      type: String,
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
        .get('/auth/user-info', {
          params: { id: this.userId }
        })
        .then(response => {
          this.userInfo = { ...this.userInfo, ...response.data }
        })
        .catch(error => {
          if (error.response.status === 401) {
            this.$router.push('/')
          }
        })
    },
    checkFollow() {
      Api.JWTAuth()
        .get('/follow', {
          params: { following_id: this.userId }
        })
        .then(() => {
          this.userInfo.is_following = true
        })
        .catch(error => {
          if (error.response.status === 401) {
            this.$router.push('/')
          } else if (error.response.status === 404) {
            this.userInfo.is_following = false
          }
        })
    },

    follow() {
      const isFollowing = this.userInfo.is_following
      if (!isFollowing) {
        Api.JWTAuth()
          .post('follow', null, {
            params: { id: this.userId }
          })
          .then(() => {
            this.userInfo.is_following = true
            this.userInfo.follower_count++
          })
          .catch(error => {
            if (error.response.status === 401) {
              this.$router.push('/')
            }
          })
      } else {
        Api.JWTAuth()
          .delete('follow', {
            params: { id: this.userId }
          })
          .then(() => {
            this.userInfo.is_following = false
            this.userInfo.follower_count--
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
    this.checkFollow()
  }
}
</script>
<style lang="scss" scoped>
.container {
  max-width: 400px;
}
</style>
