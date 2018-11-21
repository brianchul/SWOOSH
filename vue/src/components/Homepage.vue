<template>
  <div class='homepageRoot center'>
    <div class='contentWrapper center'>
      <transition name='contentTransition' @after-leave='openBoard = true'>
        <div v-if='windowView' class='content'>
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
          <div v-for='(item,index) in menuItems' :key='index' @click='onClick'
          :class='(windowView)? (index === 0)? "leftMenu" : (index === 4 )? "rightMenu" : "" : ""'>
            {{ item }}
          </div>
        </div>
        <transition name='boardTransition' @after-enter='afterOpen = true'>
          <div v-if='openBoard' class='board center'
          :class='(afterOpen) ? "boardAfter" : ""'>
            <div class='close' @click='closeBoard'></div>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Homepage',
  props: {
    windowView: Boolean,
  },
  data() {
    return {
      menuItems: [
        'ABOUT US',
        'HISTORY',
        'APPLICATION',
        'CASE LIST',
        'COMPANY',
      ],
      openBoard: false,
      afterOpen: false,
    }
  },
  methods: {
    onClick: function() {
      this.$emit('closeWindow');
    },
    closeBoard: function() {
      this.openBoard = false;
    },
  }
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
.leftMenu {
  padding-left: 100px;
}
.rightMenu {
  padding-right: 100px;
}
.title {
  height: 300px;
  font-size: 50px;
}
.intro { 
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
  transition: all 2s;
}
.boardTransition-enter, .boardTransition-leave-to, .boardBefore {
  height: 0px;
  opacity: 0;
}
.boardTransition-enter-to, .boardTransition-leave, .boardAfter {
  height: 60vh;
  opacity: 1;
}
.board {
  position: relative;
  width: 90%;
  background-color: rgba(227,239,244,0.7);
  border-radius: 20px;
  margin-bottom: 30px;
}
.close {
  position: absolute;
  right: 32px;
  top: 32px;
  width: 32px;
  height: 32px;
  opacity: 0.3;
}
.close:hover {
  opacity: 1;
}
.close:before, .close:after {
  position: absolute;
  left: 15px;
  content: ' ';
  height: 33px;
  width: 2px;
  background-color: #333;
}
.close:before {
  transform: rotate(45deg);
}
.close:after {
  transform: rotate(-45deg);
}
</style>
