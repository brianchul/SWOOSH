<template>
    <div>
        <div class='center'>
            <div class='title'>-Super Rocket-</div>
        </div>
        <div class='separate center'>
            <div class='separate2'></div>
        </div>
        <div class='main'>
            <div class='motive'>
                動機
            </div>  
            <div class='purpose'>
                目的
            </div> 
            <div class='team'>
                團隊
            </div>
        </div>       
    </div>
</template>

<script>
export default {
    name: 'AboutUs',
}
</script>

<style scoped>
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}
.separate {
    width: 100%;
    height: 5px;
}
.separate2 {
    width: 70%;
    height: 5px;
    border-bottom: 2px solid #fff;
}
.title {
    width: 70%;
    color: #fff;
    font-size: 60px;
    border-bottom: 2px solid #fff;
    padding-bottom: 10px;
    text-align: center;
}
.main {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 900px;
}
.motive {
    width: 100%;
    height: 300px;
    background-color: green;
}
.purpose {
    width: 100%;
    height: 300px;
    background-color: yellow;
}
.team {
    width: 100%;
    height: 300px;
    background-color: red;
}
</style>