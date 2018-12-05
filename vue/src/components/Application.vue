<template>
   
    <div>
      <div class="title font-stytle"> 發射申請 </div>
      
        <form class="fields ">
            <div class="field_third">
                <label class="label-font" >申請單位</label>
                <input  v-model="form.applier" placehilder="請輸入" class="input"> 
            
                
            </div>
            <div class="field_third">
                <label class="label-font" >電話號碼</label>
                <input  v-model="form.phone" placehilder="請輸入" class="input"> 
            </div>
            <div class="field_third">
                <label class="label-font" >E-MAIL</label>
                <input  v-model="form.email" placehilder="請輸入" class="input"> 
                
            </div>
            <div class="field_four">
                <label class="label-font" >衛星名稱</label>
                <input  v-model="form.satellite_name" placehilder="請輸入" class="input"> 
                
            </div>
            <div class="field_four">
                <label class="label-font" >衛星重量（KG）</label>
            <input  v-model="form.weight" placehilder="請輸入" class="input"> 
            
            </div>
            <div class="dropdown">
                <label class="label-font" >發射高度-height </label>
                <select v-model="form.height" class="input" style="height:46px; width:250px;" >
                    <option value="LEO"> 低軌道LEO </option>
                    <option value="MEO"> 中軌道MEO </option>
                    <option value="GEO"> 高軌道HEO </option>
                </select>
            </div>
            <div class="dropdown">
                <label class="label-font" >傾角-inclination</label>
                <select v-model="form.inclination" class="input" style="height:46px; width:250px;" >
                    <option value="5~14">5~14度</option>
                    <option value="15~24">15~24度</option>
                    <option value="25~34">25~34度</option>
                    <option value="35~44">35~44度</option>
                    <option value="45~54">45~54度</option>
                    <option value="55~64">55~64度</option>
                    <option value="65~74">65~74度</option>
                    <option value="75~85">75~85度</option>
                </select>
            </div>
            <div class="field_third">
                <label class="label-font" >發射日期</label>
                <input  v-model="form.launchDate" placehilder="請輸入" class="input"> 
            </div>
            <div class="field_third">
                <label class="label-font" >進場日期</label>
                <input  v-model="form.toFactoryDate" placehilder="請輸入" class="input"> 
            </div>
            <div class="field_third">
                <label class="label-font" >此次預算</label>
                <input  v-model="form.weight" placehilder="請輸入" class="input"> 
            </div>
            <div class="purpose ">
                <label class="label-font" >目的</label>
                <textarea v-model="form.purpose" type=text class="input" style="height:200px;" >
                </textarea>
            </div>
            <div class="button_function" >
                <button v-on:click="submit" class="submit">提交</button>
                <button class="submit" >清除</button>
            </div>
        </form>
      
    </div>
    

</template>

<script>
export default {
    name: 'Application',
    data() {
        return {
            form: {
                applier:null,
                phone: null,
                porpose:null,
                weight: null,
                height: null,
                inclination: null,
                launchDate: null,
                toFactoryDate:null,
                email:null,
                budget:null,
                satellite_name:null,

            },
        }
    },
}
</script>

<style scoped>
.application{

background-color: Gray;
border-radius:10px;
width:70%;
height:700px;


}
.title {
  position:relative;
  height:50px;
  color:white;
  font-size:30px;
  margin-bottom: 20px;
}

.contentWrapper {
  width: 80%;
  height:90%;
}

.center {
    display: flex;
    justify-content: center;
    align-items: center;
}

.fields{
  display:flex;
  flex-direction :row;
  flex-wrap:wrap;
}

.field_third{
  display:flex;
  flex-direction :column;
  width: calc(33% - 20px);
  height:80px;
  margin-right:20px;
  margin-bottom:30px;
 
}
.field_four{
  display:flex;
  flex-direction :column;
  width: calc(25% - 30px);
  height:80px;
  margin-right:30px;
  margin-bottom:30px;
 
 
}
.input{
    background-color:transparent;
    font-size:20px;
    color:#ffffff;
    border-radius: 4px;
    border: solid 1px #ffffff;
    padding:10px;
    
    
}
.label-font{
  color:white;
  font-size:18px;
  margin:10px;
 
  
}
.purpose{
  display:flex;
  flex-direction :column;
  width:97%;
  
}
.button_function{
  display:flex;
  flex-direction :row;
}
.submit{
    text-align: center;
    border-radius: 4px;
    display: inline-block;
    font-size: 14px;
    padding: 10px 30px;
    cursor: pointer;
    margin-top:30px;
    margin-right:40px;
}
.dropdown{

  display:flex;
  flex-direction :column;
  width: calc(25% - 30px);
  height:100px;
  margin-right:30px;
 
  
}

</style>