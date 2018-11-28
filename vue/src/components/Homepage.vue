<template>
  <div class='homepageRoot center'>
    <div class='contentWrapper center'>
      <transition name='contentTransition' @after-leave='boardView = true'>
        <div v-show='windowView' class='content'>
          <div class='title center'>Super Rocket</div>
          <div class='intro center'>
            IF YOU DON'T HAVE ENOUGH MONEY TO LAUNCH THE SATELLITE.
            <br/>
            WE OFFER SATELLITE CO-LAUNCHING SEARCH HELP TO REDUCE YOUR COSTS.
          </div>
        </div>
      </transition>
      <div class='menuWrapper center'>
        <div class='menu center'>
          <div v-for='(item,index) in menuItems' :key='index' @click='closeWindow(index)'
          :id='(windowView)? "" : (selectedMenuIndex === index)? "selectedMenu" : ""'
          :class='(windowView)? (index === 0)? "leftMenu" : (index === 4 )? "rightMenu" : "" : ""'>
            {{ item.text }}
          </div>
        </div>
        <transition name='boardTransition'
        @before-enter='contentRoot = menuItems[selectedMenuIndex].component'
        @after-enter='boardHeightHandler = true'
        @before-leave='boardHeightHandler = false'>
          <div v-show='boardView' class='board center'
          :class='(boardHeightHandler) ? "boardAfter" : ""'>
            <div class='close' @click='closeBoard'></div>
            <div class='componentWrapper'>
              <component :is='contentRoot'></component>
            </div>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
import AboutUs from './AboutUs.vue'
import History from './History.vue'
import Application from './Application.vue'
import CaseList from './CaseList.vue'
import Order from './Order.vue'

export default {
  name: 'Homepage',
  components: {
    AboutUs,
    History,
    Application,
    CaseList,
    Order,
  },
  props: {
    windowView: Boolean,
  },
  data() {
    return {
      menuItems: [
        {text:'ABOUT US', component:'AboutUs'},
        {text:'HISTORY', component:'History'},
        {text:'APPLICATION', component:'Application'},
        {text:'CASE LIST', component:'CaseList'},
        {text:'ORDER', component:'Order'},
      ],
      selectedMenuIndex: 0,
      contentRoot: 'AboutUs',
      boardView: false,
      boardHeightHandler: false,
    }
  },
  methods: {
    closeWindow: function(index) {
      this.$emit('closeWindow');
      this.selectedMenuIndex = index;
      this.boardView = false;
      setTimeout(() => this.boardView = true,850);
    },
    closeBoard: function() {
      this.boardView = false;
      this.$emit('openWindow');
    },
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
.close {
  position: absolute;
  right: 20px;
  top: 20px;
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
.componentWrapper {
  width: 85%;
  height: 85%;
  color: #000;
  overflow: scroll;
}
</style>