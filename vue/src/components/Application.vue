<template>
    <div  v-if="use_status.user">
      <div class="title font-stytle"> 發射申請 </div>
        <form class="fields ">
            <div class="field_four">
                <div class="test">
                    <label class="label-font" >衛星名稱</label>
                    <div v-if="valid.satellite_name" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>
                <input  v-model="form.satellite_name" placehilder="請輸入" class="input"> 
            </div>
            <div class="field_four">
                <div class="test">
                    <label class="label-font" >衛星重量（KG）</label>
                    <div v-if="valid.weight" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>    
                <input  v-model="form.weight" placehilder="請輸入" class="input">
            </div>
            <div class="dropdown">
                <div class="test">
                    <label class="label-font" >發射高度 </label>
                    <div v-if="valid.height" class="valid_warn">
                        <span  >*此欄位不能空</span>
                    </div>
                </div>    
                <select v-model="form.height" class="input" style="height:60px; width:250px;" >
                    <option value="LEO"> 低軌道LEO </option>
                    <option value="MEO"> 中軌道MEO </option>
                    <option value="GEO"> 高軌道HEO </option>
                </select>
            </div>
            <div class="dropdown">
                <div class="test">  
                    <label class="label-font" >傾角</label>
                    <div v-if="valid.inclination" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>
                <select v-model="form.inclination" class="input" style="height:60px; width:250px;" >
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
            <div class="field_four">
                <div class="test">
                    <label class="label-font" >發射日期</label>
                    <div v-if="valid.launchDate" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>
                <input  v-model="form.launchDate" placehilder="請輸入" class="input"> 
            </div>
            <div class="field_four">
                <div class="test">    
                    <label class="label-font" >此次預算</label>
                    <div v-if="valid.budget" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>    
                <input  v-model="form.budget" placehilder="請輸入" class="input"> 
            </div>
            <div class="purpose ">
                <label class="label-font" >目的</label>
                <textarea v-model="form.purpose" type=text class="input" style="height:200px;" >
                </textarea>
            </div>
            <div class="button_function" >
                <button @click.prevent="submit" class="submit">提交</button>
                <button class="submit" >清除</button>
            </div>
        </form>
    </div>
</template>

<script>
import api from '../lib/' 
export default {
    name: 'Application',
    props: {
        userInfo: Object,
    },
    data() {
        return {
            apiStatus: true,
            use_status:{
                user:true,
            },
            form: {
                purpose:null,
                weight: null,
                height: null,
                inclination: null,
                launchDate: null,
                budget:null,
                satellite_name:null,
            },
            form_company:{
                rocketName: null,
                height: null,
                inclination: null,
                totalWeight: null,
                launchDate:null,
            },
            form_sale:{
                rocketName:null,
                price:null,
                toFactoryDate:null,
                limitWeight:null,
            },
            valid_company:{
                rocketName:null,
                height: null,
                inclination: null,
                tatalWeight: null,
                launchDate:null,
            },
            valid_sale:{
                limitWeight:null,
                price:null,
                IDe:null,
                toFactoryDate:null,
                rocketName:name,
            },
            
        }
    },
    methods:{
        onSuccess: function() {
            this.$message({
                type: 'success',
                message: '成功',
                center: true,
            })
        },
        onFailed: function() {
            this.$message({
                type: 'error',
                message: '失敗',
                center: true,
            })
        },
        submit: function() {
            for(var key in this.form) {
                if(this.form[key] === null) {
                    this.apiStatus = false
                }
            }
            if(this.apiStatus) {
                const info = JSON.parse(localStorage.getItem('userInfo'))
                api.postNeed({
                    request_by: info.id,
                    satellite_name: this.form.satellite_name,
                    weight_kg: parseInt(this.form.weight),
                    purpose: this.form.purpose,
                    eta_height_km: this.form.height,
                    arrival_date: this.form.launchDate,
                    inclination: this.form.inclination,
                    budget_billion: parseInt(this.form.budget),
                },this.onSuccess,this.onFailed)
            }
        },
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
.fields_col{
  display:flex;
  flex-direction :column;
  flex-wrap:wrap;
}


.field_two{
  display:flex;
  flex-direction :column;
  width:40%;
  height:100px;
  margin-right:100px;
  margin-bottom:50px;
}


.field_third{
  display:flex;
  flex-direction :column;
  width: calc(33% - 20px);
  height:100px;
  margin-right:20px;
  margin-bottom:30px;
 
}
.field_four{
  display:flex;
  flex-direction :column;
  width: calc(25% - 30px);
  height:100px;
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
    margin-top:20px;
    
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

.valid_warn{
    color:red;
    font-size:14px;
    margin-top:15px;
    
 }
 .test{
     
  display:flex;
  flex-direction :row;
  flex-wrap:wrap;

 }



</style>