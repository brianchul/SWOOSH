<template>
  <div id='app center'>
    <div class='bg'></div>
    <Homepage @openWindow='windowView = true' @closeWindow='windowView = false' :windowView='windowView'/>
    <transition name='windowTransition'>
      <div v-if='windowView' class='window'></div>
    </transition>
  </div>
</template>

<script>
import Homepage from './components/Homepage.vue'

export default {
  name: 'app',
  components: {
    Homepage
  },
  data() {
    return {
      windowView: true,
    } 
  },
}
</script>

<style>
body {
  margin: 0px;
  font-family: Colfax,sans-serif;
}
.bg {
  position: absolute;
  top: 0px;
  width: 100%;
  height: 100%;
  background-image: linear-gradient(rgba(19, 21, 25, 0.65)) , url('./assets/earth.jpg') ;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}
.window {
  position: fixed;
  top: 0px;
  width: 100vw;
  height: 100vh;
  background-image: url('./assets/window.png') ;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  pointer-events: none;
}
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}
.homepageWrapper {
  width: 70%;
  overflow: hidden;
}
.windowTransition-enter-active, .windowTransition-leave-active {
  transition: opacity .5s;
}
.windowTransition-enter, .windowTransition-leave-to {
  opacity: 0;
}
</style>
