<template>
  <div class='homepageRoot center'>
    <div class='contentWrapper center'>
      <transition name='contentTransition' @after-leave='boardView = true'>
        <div v-show='windowView' class='content'>
          <div class='boxWrapper'>
            <div class='box center' @click='status = "home"' v-if='status !== "home"' >
              <div class='close'></div>
            </div>
            <div class='box center' @click='logout' v-if='userInfo.isLoggedIn'>登出</div>
            <div class='box center' @click='status = "regist"' v-if='status !== "regist" && !userInfo.isLoggedIn'>註冊</div>
            <div class='box center' @click='status = "login"' v-if='status !== "login" && !userInfo.isLoggedIn'>登入</div>
            <div class='box center' v-if='userInfo.isLoggedIn'> {{userInfo.fullname}}</div>
          </div>
          <div v-if="status === 'home'">
            <div class='title center'>Super Rocket</div>
            <div class='intro center'>
              IF YOU DON'T HAVE ENOUGH MONEY TO LAUNCH THE SATELLITE.
              <br/>
              WE OFFER SATELLITE CO-LAUNCHING SEARCH HELP TO REDUCE YOUR COSTS.
            </div>
          </div>
          <div v-else class="formArea center">
            <Form :status='status' @closeForm='status = "home"' @setLogin='login'/>
          </div>
        </div>
      </transition>
      <div class='menuWrapper center'>
        <div class='menu center'>
          <div v-for='(item,index) in menuItems' :key='item.component' @click='changeWindow(item.component)'
          :id='(!windowView && (selectedMenuItem === item.component))? "selectedMenu" : ""'
          :class='(windowView && (index === 0))? "leftMenu" : (windowView && (index === 4 ))? "rightMenu" : ""'>
            {{ item.text }}
          </div>
        </div>
        <transition name='boardTransition'
        @before-enter='contentRoot = selectedMenuItem'
        @after-enter='boardHeightHandler = true'
        @before-leave='boardHeightHandler = false'>
          <div v-show='boardView' class='board center'
          :class='(boardHeightHandler) ? "boardAfter" : ""'>
            <div class='close cross' @click='closeBoard'></div>
            <div class='componentWrapper'>
              <component :is='contentRoot'
              @setAlert='$emit("setAlert")'
              :userInfo='userInfo'></component>
            </div>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import AboutUs from './AboutUs.vue'
import History from './History.vue'
import Application from './Application.vue'
import CaseList from './CaseList.vue'
import Order from './Order.vue'
import Form from './Homepage/Form.vue'

export default {
  name: 'Homepage',
  components: {
    AboutUs,
    History,
    Application,
    CaseList,
    Order,
    Form,
  },
  props: {
    windowView: Boolean,
    alert: Object,
  },
  data() {
    return {
      status: 'home', // login, regist, home
      menuItems: [
        {text:'ABOUT US', component:'AboutUs'},
        {text:'HISTORY', component:'History'},
        {text:'APPLICATION', component:'Application'},
        {text:'CASE LIST', component:'CaseList'},
        {text:'ORDER', component:'Order'},
      ],
      selectedMenuItem: 'AboutUs',
      contentRoot: 'AboutUs',
      boardView: false,
      boardHeightHandler: false,
      userInfo: {
        isLoggedIn: false,
        userId: null,
        fullname: '',
        permission: 'guest',
      },
    }
  },
  methods: {
    changeWindow: function(index) {
      if(!this.userInfo.isLoggedIn && index !== 'AboutUs' && index !== 'History') {
        localStorage.setItem('alert',JSON.stringify({
          hook: true,
          status: 'fail',
          title: '操作失敗',
          message: '請先登入',
        }))
        this.$emit('setAlert')
      } else {
        this.$emit('closeWindow');
        this.selectedMenuItem = index;
        this.boardView = false;
        setTimeout(() => this.boardView = true,850);
      }
    },
    closeBoard: function() {
      this.boardView = false;
      this.$emit('openWindow');
    },
    logout: function() {
      this.userInfo = {
        isLoggedIn: false,
        userId: null,
        fullname: '',
        permission: 'guest',
      }
      localStorage.setItem('userInfo',JSON.stringify(this.userInfo))
    },
  },
  created() {
    this.userInfo = JSON.parse(localStorage.getItem('userInfo'))
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.homepageRoot {
  display: flex;
  position: relative;
  width: 100%;
  height: 100vh;
}
.contentWrapper {
  display: flex;
  flex-direction: column;
  width: 100%;
  overflow: hidden;
}
.content {
  position: relative;
  width: 100%;
  color: #fff;
  font-size: 30px;
  overflow: hidden;
  border-top: 2px solid #fff;
  text-align: center;
  height: calc(70vh - 100px);
}
.menuWrapper {
  flex-direction: column;
  width: 100%;
  border-top: 2px solid #fff;
  border-bottom: 2px solid #fff;
}
.menu {
  width: 100%;
  height: 100px;
}
.menu div {
  width: 160px;
  height: 100px;
  line-height: 100px;
  font-size: 20px;
  text-align: center;
  color: #fff;
}
.menu div:hover {
  background-color: rgba(255, 255, 255, 0.3);
}
#selectedMenu {
  background-color: rgba(255, 255, 255, 1);
  color: #000;
}
.leftMenu {
  padding-left: 100px;
}
.rightMenu {
  padding-right: 100px;
}
.content .title {
  height: 300px;
  font-size: 50px;
}
.content .intro { 
  height: 150px;
  font-size: 20px;
}
.contentTransition-enter-active, .contentTransition-leave-active {
  transition: height 1s;
}
.contentTransition-enter, .contentTransition-leave-to {
  height: 0px;
}
.contentTransition-enter-to, .contentTransition-leave {
  height: calc(70vh - 100px);
}
.boardTransition-enter-active, .boardTransition-leave-active {
  transition: all .8s;
}
.boardTransition-enter, .boardTransition-leave-to, .boardBefore {
  height: 0px;
  margin-bottom: 0px;
}
.boardTransition-enter-to, .boardTransition-leave, .boardAfter {
  height: 80vh;
  margin-bottom: 30px;
}
.board {
  position: relative;
  width: 90%;
  border: 2px solid #fff;
  border-radius: 20px;
  background-color: rgba(227,239,244,0.4);
  overflow: hidden;
}
.componentWrapper {
  width: 85%;
  height: 85%;
  color: #000;
  overflow: scroll;
}
.cross {
  top: 20px;
  right: 20px;
}
.formArea {
  position: fixed;
  height: 70vh;
  width: 100vw;
}
.boxWrapper {
  z-index: 5;
  position: absolute;
  top: 10px;
  right: 10px;
  font-size: 18px;
  color: #fff;
  pointer-events: auto;
  display: flex;
  flex-direction: row-reverse;
  margin-right: 20vw;
  height: 50px;
  font-family: Colfax,sans-serif;
}
.box {
  height: 50px;
  width: 75px;
}
</style>
