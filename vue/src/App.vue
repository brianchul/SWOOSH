<template>
  <div id='app center'>
    <div class='bg'></div>
    <Homepage
      @openWindow='windowView = true'
      @closeWindow='windowView = false'
      :windowView='windowView'
      @setAlert='setAlert'/>
    <transition name='windowTransition'>
      <div v-if='windowView' class='window'></div>
    </transition>
    <div class='alertWrapper center' :class='alert.hook ? "alertEnter" : "alertOut"'>
      <div class='alertBox center' :class='alert.status+"Style"'>
        <div>{{alert.title}}</div>
        <div>{{alert.message}}</div>
      </div>
    </div>
  </div>
</template>

<script>
import Homepage from './components/Homepage.vue'

export default {
  name: 'app',
  components: {
    Homepage,
  },
  data() {
    return {
      windowView: true,
      alert: {
        hook: false,
        status: '', // 'success', 'fail', 'warning', ''
        title: '',
        message: '',
      },
    } 
  },
  methods: {
    initAlert: function() {
      localStorage.setItem('alert',JSON.stringify({
        hook: false,
        status: '',
        title: '',
        message: '',
      }))
    },
    resetAlert: function() {
      this.alert = JSON.parse(localStorage.getItem('alert'))
    },
    setAlert: function() {
      this.resetAlert();
      setTimeout(() => {
        this.alert.hook = false;
      },3000);
      setTimeout(() => {
        this.initAlert();
        this.resetAlert();
      },3500);
    },
  },
  created() {
    this.initAlert();
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
::-webkit-scrollbar { 
    display: none; 
}
.close {
  position: absolute;
  width: 32px;
  height: 32px;
}
.close:before, .close:after {
  position: absolute;
  left: 15px;
  content: ' ';
  height: 33px;
  width: 2px;
  background-color: #333;
}
.close:hover:before, .close:hover:after{
  background-color: #fff;
}
.close:before {
  transform: rotate(45deg);
}
.close:after {
  transform: rotate(-45deg);
}
.alertWrapper {
  position: fixed;
  width: 100%;
  height: 100px;
  color: #000;
  transition: bottom .5s;
}
.alertEnter {
  bottom: 10px;
}
.alertOut {
  bottom: -200px;
}
.alertBox {
  flex-direction: column;
  width: 400px;
  height: 100px;
  border-radius: 20px;
  background-color: rgba(255,255,255,0.7);
}
.successStyle {
  box-shadow: 0 0 1em green;
}
.failStyle {
  box-shadow: 0 0 1em red;
}
</style>
