<template>
  <div id='app center'>
    <div class='bg'></div>
    <Homepage @openWindow='windowView = true' @closeWindow='windowView = false' :windowView='windowView'/>
    <div v-if="loginStatus" class="loginArea center">
      <div class="loginDiv">
        
      </div>
    </div>
    <div v-if="regStatus" class="regArea center">
      <div class="regDiv">

      </div>
    </div>
    <transition name='windowTransition'>
      <div v-if='windowView' class='window'>
        <div class='box'>
          <div class='box1 center' @click='regStatusHandler'>註冊</div>
          <div class='box2 center' @click='logStatusHandler'>登入</div>
        </div>
      </div>
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
      regStatus: false,
      loginStatus: false,
    } 
  },
  methods: {
    regStatusHandler: function() {
      this.regStatus = !this.regStatus;
    },
    logStatusHandler: function() {
      this.loginStatus = !this.loginStatus;
    }
  }
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
.box {
  color: #fff;
  pointer-events: auto;
  display: flex;
  position: fixed;
  top: 130px;
  margin-left: 68.6vw;
  height: 50px;
  width: 150px;
  font-family: Colfax,sans-serif;
}
.box1 {
  height: 50px;
  width: 75px;
}
.box2 {
  height: 50px;
  width: 75px;
}
.regArea {
  position: absolute;
  top: 0px;
  width: 100vw;
  height: 100vh;
}
.regDiv {
  height: 70vh;
  width: 100%;
  background-color: black;
}
.loginArea {
  position: absolute;
  top: 0px;
  width: 100vw;
  height: 100vh;
}
.loginDiv {
  height: 70vh;
  width: 100%;
  background-color: black;
}
</style>
