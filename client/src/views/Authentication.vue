<template>
  <div class="page">
    <h1>Twitter Clone</h1>

    <transition name="bounce">
      <Register
        v-if="isRegister"
        class="justify-center"
        v-on:log-in="isRegister = false"
        transition="fade-transition"
      />
      <LogIn v-else class="justify-center" v-on:register="isRegister = true" />
    </transition>
  </div>
</template>

<script>
// @ is an alias to /src
import Register from '@/components/Register.vue'
import LogIn from '@/components/LogIn.vue'

export default {
  name: 'Authentication',
  components: {
    Register,
    LogIn
  },
  data: () => ({
    isRegister: false
  })
}
</script>
<style lang="scss" scoped>
$switch-animation-time: 0.3s;

.bounce-enter-active {
  animation: bounce-in $switch-animation-time;
}
.bounce-leave-active {
  animation: bounce-in $switch-animation-time reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0.5);
    opacity: 0.3;
  }
  80% {
    opacity: 1;
  }
  100% {
    transform: scale(1);
  }
}

.page {
  background-color: #fafafa;
  display: flex;
  height: 100vh;
  align-items: center;
  justify-content: center;

  & > * {
    position: absolute;
    width: 100%;
  }

  h1 {
    position: absolute;
    color: #eeeeee;
    font-size: 13rem;
    white-space: nowrap;
    font-weight: normal;
    font-family: 'Pacifico', cursive;
    padding: 0;
    margin: 0;
    width: 100%;
    text-align: center;
  }
}
</style>
