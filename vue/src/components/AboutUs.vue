<template>
    <div>
        <div class='center'>
            <div class='title'>-Super Rocket-</div>
        </div>
        <div class='separate center'>
            <div class='separate2'></div>
        </div>
        <div class='main'>
            <div>
                <h2>動機</h2>
                <div class='contents'>
                    - 據英國學者研究指出，每5個人就有一個人擁有太空夢。<br/>
                    - 據美國華爾街商周雜誌分析，小衛星的市場價值預期超過 300 億美元，<br/>
                    &nbsp;&nbsp;&nbsp;未來 10 年內全球將發射超過 6,200 顆小衛星。<br/><br/>
                    有別於由 NASA 及主流航太公司把持的舊太空，人類未來將迎接小衛星大量發射的新商業時代，<br/>
                    也就是「新太空」
                </div>
            </div>  
            <div>
                <h2>目的</h2>
                <div class='contents'>
                    有鑒於需求的大幅提升，能供應的火箭數量卻有限且費用昂貴<br/>
                    近年來興起的”共享經濟“可謂解決之道<br/>
                    本團隊看準先機，切入這塊市場，旨為顧客帶來前所未有的體驗<br/>
                    攤提成本之下，以最低的價格享受尊榮服務<br/>
                    漫遊太空絕對不是夢!!!
                </div>
            </div> 
            <div class='team'>
                <h2>團隊</h2>
                <div class='members center'>
                    <div class='member center'>
                        <div>
                            <img src="../assets/team1.jpg" width="100%" height="200px">
                        </div>
                        <div class='center'>超級箭前端長 許明欣</div>    
                    </div>
                    <div class='member'>
                        <div>
                            <img src="../assets/team2.jpg" width="100%" height="200px">
                        </div>
                        <div>
                            <div class='center'>超級箭後端長 邱穎雋</div>
                        </div>    
                    </div>
                    <div class='member'>
                        <div>
                            <img src="../assets/team3.jpg" width="100%" height="200px">
                        </div>
                        <div>
                            <div class='center'>超級箭秘書長 龎虞蓁</div>
                        </div>    
                    </div>
                    <div class='member'>
                        <div>
                            <img src="../assets/team4.jpg" width="100%" height="200px">
                        </div>
                        <div>
                            <div class='center'>超級箭中鋒 李宗轅</div>
                        </div>    
                    </div>
                    <div class='separatePic'></div>
                    <div class='member'>
                        <div>
                            <img src="../assets/team5.jpg" width="100%" height="200px">
                        </div>
                        <div>
                            <div class='center'>超級箭前鋒 葉哲欣</div>
                        </div>    
                    </div>
                    <div class='member'>
                        <div>
                            <img src="../assets/team6.png" width="100%" height="200px">
                        </div>
                        <div>
                            <div class='center'>超級箭後衛 林志軒</div>
                        </div>    
                    </div>
                    <div class='member'>
                        <div>
                            <img src="../assets/team7.jpg" width="100%" height="200px">
                        </div>
                        <div>
                            <div class='center'>超級箭後衛 陳家輔</div>
                        </div>    
                    </div>
                    <div class='member'>
                        <div>
                            <img src="../assets/team8.jpg" width="100%" height="200px">
                        </div>
                        <div>
                            <div class='center'>超級箭自衛 黃耀德</div>
                        </div>    
                    </div>
                </div>    
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
    color: #fff;
}
.team {
    display: flex;
    flex-direction: column;
}
.members {
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}
.member {
    margin-left: 25px;
    margin-right: 25px; 
    width: 18%;
    display: flex;
    flex-direction: column;
}
.separatePic {
    width: 100%;
    height: 25px;
}
.contents {
    margin-left: 80px;
}
</style>