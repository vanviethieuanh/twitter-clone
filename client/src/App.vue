<template>
  <v-app color="grey lighten-5" class="app">
    <router-view></router-view>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  data: () => ({
    //
  })
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
.app {
  background-color: #fafafa !important;
}
</style>
