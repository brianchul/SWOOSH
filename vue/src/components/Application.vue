<template>
    <div v-if='userInfo.permission === "user"' >
      <div class="title font-stytle"> 發射申請 </div>
            <form class="fields ">
                <div class="field_four">
                    <div class="test">
                        <label class="label-font" >衛星名稱</label>
                        <div v-if="form.need.satellite_name==null" class="valid_warn">
                            <span >*此欄位不能空</span>
                        </div>
                    </div>
                    <input  v-model="form.need.satellite_name" placeholder="請輸入" class="input"/> 
                </div>
                <div class="field_four">
                    <div class="test">
                        <label class="label-font" >衛星重量（KG）</label>
                        <div v-if="form.need.weight==null" placeholder="請輸入" class="valid_warn">
                            <span >*此欄位不能空</span>
                        </div>
                    </div>    
                    <input  v-model="form.need.weight" placeholder="請輸入" class="input"/>
                </div>
                <div class="dropdown">
                    <div class="test">
                        <label class="label-font" >發射高度 </label>
                        <div v-if="form.need.height==null"  placeholder="請輸入" class="valid_warn">
                            <span  >*此欄位不能空</span>
                        </div>
                    </div>    
                    <select v-model="form.need.height" class="input" style="height:60px; width:250px;" >
                        <option value="LEO"> 低軌道LEO </option>
                        <option value="MEO"> 中軌道MEO </option>
                        <option value="GEO"> 高軌道HEO </option>
                    </select>
                </div>
                <div class="dropdown">
                    <div class="test">  
                        <label class="label-font" >傾角</label>
                        <div v-if="form.need.inclination==null" class="valid_warn">
                            <span >*此欄位不能空</span>
                        </div>
                    </div>
                    <select v-model="form.need.inclination" class="input" style="height:60px; width:250px;" >
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
                        <div v-if="form.need.launchDate==null" class="valid_warn">
                            <span >*此欄位不能空</span>
                        </div>
                    </div>
                    <input  v-model="form.need.launchDate" placeholder="請輸入" class="input"/> 
                </div>
                <div class="field_four">
                    <div class="test">
                        <label class="label-font" >進場日期</label>
                        <div v-if="form.need.toFactoryDate==null" class="valid_warn">
                            <span >*此欄位不能空</span>
                        </div>
                    </div>
                    <input  v-model="form.need.toFactoryDate" placeholder="請輸入" class="input"/> 
                </div>
                <div class="field_four">
                    <div class="test">    
                        <label class="label-font" >此次預算</label>
                        <div v-if="form.need.budget==null" class="valid_warn">
                            <span >*此欄位不能空</span>
                        </div>
                    </div>    
                    <input  v-model="form.need.budget" placeholder=" 請輸入" class="input"/> 
                </div>
                <div class="purpose ">
                    <label class="label-font" >目的</label>
                    <textarea v-model="form.need.purpose" type=text class="input" style="height:200px;" >
                    </textarea>
                </div>
                <div class="button_function" >
                    <button @click.prevent="submit" class="submit">提交</button>
                    <button class="submit" >清除</button>
                </div>
            </form>
        </div>
    </div>

    <div v-else-if='userInfo.permission="company"'>
        <div class="title font-stytle center"> {{(change === "mission") ? "任務": "機位"}} </div>
            <button @click.prevent="change = 'mission'">任務</button>
            <button @click.prevent="change = 'sale'">機位</button>
        
        <div v-if='change === "mission"'>
            <form class="fields ">
                <div class="field_third" >
                    <div>    
                        <label class="label-font" >火箭名稱</label>
                        <div v-if="form.mission.rocketName==null" class="valid_warn">
                            <span >*此欄位不能空</span>
                        </div>
                    </div>
                    <input  v-model="form.mission.rocketName" placeholder="請輸入" class="input" style="height:55px;"/>    
                </div>
                <div class="field_third">
                    <div >
                        <label class="label-font" >發射高度</label>
                        <div v-if="form.mission.height==null" class="valid_warn">
                            <span >*此欄位不能空</span>
                        </div>
                    </div>
                    <select v-model="form.mission.height" class="input" style="height:60px; " >
                        <option value="LEO"> 低軌道LEO </option>
                        <option value="MEO"> 中軌道MEO </option>
                        <option value="GEO"> 高軌道HEO </option>
                    </select>
                </div>
                <div class="field_third" >
                    <div>    
                        <label class="label-font" >總負重量</label>
                        <div v-if="form.mission.totalWeight==null" class="valid_warn">
                            <span >*此欄位不能空</span>
                        </div>
                    </div>
                    <input  v-model="form.mission.totalWeight" placeholder="請輸入" class="input" style="height:55px;"/>    
                </div>
                <div class="field_third" >
                    <div >  
                        <label class="label-font" >傾角</label>
                        <div v-if="form.mission.inclination==null" class="valid_warn">
                            <span >*此欄位不能空</span>
                        </div>
                    </div>
                    <select v-model="form.mission.inclination" class="input" style="height:60px; "  >
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
                <div class="field_third" >
                    <div>    
                        <label class="label-font" >發射日期</label>
                        <div v-if="form.mission.launchDate==null" class="valid_warn">
                            <span >*此欄位不能空</span>
                        </div>
                    </div>
                    <input  v-model="form.mission.launchDate" placeholder="請輸入" class="input" style="height:55px;"/>    
                </div>
            </form>
        </div>
        <div v-else-if='change === "sale"'>
            <form class="fields">
                <div class="field_two">
                    <label class="label-font">發射計畫名稱</label>
                    <input  v-model="form.sale.rocketName" placeholder="請輸入" class="input" style="height:55px;"/>  
                    <select v-model="hello" class="input" style=" height:600px;padding:0px; ">
                        <option value="">請選擇火箭</option>
                    </select>
                </div>
                <div class="field_two ">    
                    <label class="label-font" >限制重量</label>
                    <input  v-model="form.sale.limitWeight" placeholder="請輸入" class="input" style="height:55px;"/>  
                </div>
                <div class="field_two">    
                    <label class="label-font" >最後進場日期</label>
                    <input  v-model="form.sale.toFactoryDate" placeholder="請輸入" class="input" style="height:55px;"/>  
                </div>
                <div class="field_two ">    
                    <label class="label-font" >價錢</label>
                    <input  v-model="form.sale.price" placeholder="請輸入" class="input" style="height:55px;"/>  
                </div>
            </form>
        </div>
        <div class="button_function" style="margin-left:10px" >
            <button @click.prevent="submit" class="submit">提交</button>
            <button class="submit" >清除</button>
        </div>
    </div>
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
            change: "mission",
            apiStatus: {
                need: true,
                mission: true,
                sale: true,
            },
            apply_status:false,
            use_status:{
                user:true,
            },
            form: {
                need: {
                    purpose:null,
                    weight: null,
                    height: null,
                    inclination: null,
                    launchDate: null,
                    toFactoryDate:null,
                    budget:null,
                    satellite_name:null,
                },
                mission: {
                    rocketName: null,
                    height: null,
                    inclination: null,
                    totalWeight: null,
                    launchDate:null,
                },
                sale: {
                    rocketName:null,
                    price:null,
                    toFactoryDate:null,
                    limitWeight:null,
                },
            },
            hello: null,
        }
    },
    methods:{
        
        
        onSuccess: function() {
            this.$message({
                type: 'success',
                message: '成功',
                center: true,
            })
            this.apply_status=true;
        },
        onFailed: function() {
            this.$message({
                type: 'error',
                message: '失敗',
                center: true,
            });
            this.apply_status=false;
        },
        submit: function(){
            for(var key in this.apiStatus) {
                this.apiStatus[key] = true;
                for(var formKey in this.form[key]) {
                    if(this.form[key][formKey] === null || this.form[key][formKey] === '') {
                        this.apiStatus[key] = false;
                    }
                }
            }
            const info = JSON.parse(localStorage.getItem('userInfo'))
            let payload = {}
            if(this.userInfo.permission === 'user') {
                if(this.apiStatus.need) {
                    var data = this.form.need  
                    payload = {
                        request_by: info.id,
                        satellite_name: data.satellite_name,
                        weight_kg: parseInt(data.weight),
                        purpose: data.purpose,
                        eta_height_km: data.height,
                        arrival_date: data.toFactoryDate,
                        inclination: data.inclination,
                        launch_day: data.launchDate,
                        budget_billion: parseInt(data.budget),
                        status:this.apply_status,
                    }
                    api.postNeed(payload,this.onSuccess,this.onFailed);
                } else {
                    this.$message({
                        type: 'error',
                        message: '欄位不得為空',
                        center: true,   
                    })
                }  
            } else if(this.userInfo.permission === 'company' && this.change === "mission") {
                if(this.apiStatus.mission) {
                    var data = this.form.mission
                    payload = {
                        create_by: info.id,
                        launch_rocket: data.rocketName,
                        target_height_km: data.height,
                        launch_date: data.launchDate,
                        target_inclination: data.inclination,
                        status:this.apply_status,
                        rocket_max_payload_weight: data.totalWeight,
                    }
                    api.postMission(payload,this.onSuccess,this.onFailed);
            } else {
                    this.$message({
                        type: 'error',
                        message: '欄位不得為空',
                        center: true,   
                    })
                }  
            } else if(this.userInfo.permission === 'company' && this.change === "sale") {
                if(this.apiStatus.sale) {
                    var data = this.form.sale
                    // payload = {
                    //     limit_weight: data.limitWeight,
                    //     mission_arrival_deadline: data.toFactoryDate,
                    //     seat_price:data.price,
                    //     status:this.apply_status,
                    // }
                } else {
                    this.$message({
                        type: 'error',
                        message: '欄位不得為空',
                        center: true,   
                    })
                }  
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
    height: 60px;
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

select {
     height: 60px;
 }



</style>