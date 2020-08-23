<template>
  <div class="page">
    <v-app-bar fixed flat color="white" dense>
      <v-container grid-list-xs max-width="900">
        <v-row>
          <h1>Twitter Clone</h1>
          <v-spacer></v-spacer>
          <v-btn text @click="show_home()">Home</v-btn>
          <v-btn text @click="show_explore()">Explore</v-btn>
          <v-btn text @click="go_user()">example@user.com</v-btn>
        </v-row>
      </v-container>
    </v-app-bar>
    <div class="content pt-8 mt-14">
      <v-container class="mx-auto"
        ><v-row justify="center" dense>
          <v-col cols="column">
            <v-form max-width="600">
              <v-textarea
                class="mb-5"
                maxlength="280"
                hide-details="auto"
                label="What's happening?"
                auto-grow
                rows="1"
                outlined
                row-height="15"
                counter
                clearable
                append-icon="mdi-send"
                @click:append="send"
              ></v-textarea>
            </v-form>

            <Explore />
          </v-col>
          <v-col cols="4" class="hidden-sm-and-down">
            <v-card
              class="infomation"
              flat
              color="grey lighten-5"
              width="300"
              fixed
            >
              <v-card-text>
                <a @click="go_user()">
                  <div class="font-weight-black">
                    example@user.com
                  </div>
                  <div class="font-weight-normal">Example User</div>
                </a>
                <div class="project-des text--disabled text-caption mt-5">
                  This project is for educational purposes. The target is
                  learning Vue framework, and technique of backend to implement
                  a SPA website. For the source code, check out the
                  <a href="https://github.com/vanviethieuanh/twitter-clone"
                    >repo</a
                  >
                  .
                </div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import Explore from '@/components/Explore'
export default {
  components: {
    Explore
  },
  methods: {
    send() {
      console.log('sent')
    },
    go_user() {
      console.log('this_user')
    }
  },
  computed: {
    column() {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs':
          return 12
        case 'sm':
          return 12
        case 'md':
          return 8
        case 'lg':
          return 8
        case 'xl':
          return 8
      }
      return 12
    }
  }
}
</script>

<style lang="scss" scoped>
.page {
  background-color: #fafafa;

  h1 {
    color: #262626;
    text-align: left;
    font-size: 1.5rem;
    font-family: 'Pacifico', cursive;
    font-weight: normal;
  }
  header {
    border-bottom: #e0e0e0 1px solid !important;
  }

  button {
    text-transform: none;
  }

  .infomation {
    position: fixed;
    a {
      text-decoration: none;
      color: unset;
    }
    .project-des {
      a {
        font-weight: bold;
      }
    }
  }
}
</style>
