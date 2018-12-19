<template>
   
   
    
    
    <div  v-if="use_status='user' ">
      <div class="title font-stytle"> 發射申請 </div>
      
        <form class="fields ">
            <div class="field_third">
                
                    <div class="test">
                        <label class="label-font"  >申請單位</label>
                        <div v-if="valid.applier" class="valid_warn">
                            <span >*此欄位不能空</span>
                        </div>
                    </div>
                    <input  v-model="form.applier"   placehilder="請輸入" class="input"  > 
                
            </div>
            <div class="field_third">
                <div class="test">
                    <label class="label-font" >電話號碼</label>
                    <div v-if="valid.phone" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>
                <input  v-model="form.phone" placehilder="請輸入" class="input"> 
            </div>
            <div class="field_third">
                <div class="test">
                    <label class="label-font" >E-MAIL</label>
                    <div v-if="valid.email" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>
                <input  v-model="form.email" placehilder="請輸入" class="input"> 
                
            </div>
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
            <div class="field_third">
                <div class="test">
                    <label class="label-font" >發射日期</label>
                    <div v-if="valid.launchDate" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>
                <input  v-model="form.launchDate" placehilder="請輸入" class="input"> 
            </div>
            <div class="field_third">
                <div class="test">
                    <label class="label-font" >進場日期</label>
                    <div v-if="valid.toFactoryDate" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>    
                <input  v-model="form.toFactoryDate" placehilder="請輸入" class="input"> 
            </div>
            <div class="field_third">
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


     <div v-else-if='use_status.company'>
        <div class="title font-stytle"> 任務清單 </div>
         
        <form class="fields ">
                
            <div class="field_third" >
                
                <div>    
                    <label class="label-font" >火箭名稱</label>
                    <div v-if="valid_company.rocketName" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>
            
                <input  v-model="form_company.rocketName" placehilder="請輸入" class="input" style="height:55px;">    
            </div>
        
            <div class="field_third">
                <div >
                    <label class="label-font" >發射高度</label>
                    <div v-if="valid_company.height" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>
                <select v-model="form_company.height" class="input" style="height:60px; " >
                    <option value="LEO"> 低軌道LEO </option>
                    <option value="MEO"> 中軌道MEO </option>
                    <option value="GEO"> 高軌道HEO </option>
                </select>
            </div>

            <div class="field_third" >
                
                <div>    
                    <label class="label-font" >總負重量</label>
                    <div v-if="valid_company.totalWeight" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>
            
                <input  v-model="form_company.totalWeight" placehilder="請輸入" class="input" style="height:55px;">    
            </div>
            
            <div class="field_third" >
                <div >  
                    <label class="label-font" >傾角</label>
                    <div v-if="valid_company.inclination" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>
                <select v-model="form_company.inclination" class="input" style="height:60px; "  >
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
                    <div v-if="valid_company.launchDate" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>
                </div>
            
                <input  v-model="form_company.launchDate" placehilder="請輸入" class="input" style="height:55px;">    
            </div>
            

        </form>
        <div class="button_function" style="margin-left:10px" >
                <button @click.prevent="submit" class="submit">提交</button>
                <button class="submit" >清除</button>
            </div>
        
    </div>

    <div v-else-if='use_status.sale'>
        <div class="title font-stytle center"> 火箭詳細資料 </div>
        <form class="fields">
            <div class="field_two">
              
                 <label class="label-font"  >發射計畫名稱</label>
                <select v-model="form_sale.rocketName" class="input" style=" height:600px;padding:0px; "  >
                    <option value="">請選擇火箭</option>
                </select>
                
            </div>

            <div class="field_two ">    
                    <label class="label-font" >限制重量</label>
                    <div v-if="valid_sale.limitWeight" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>

                     <input  v-model="form_sale.limitWeight" placehilder="請輸入" class="input" style="height:55px;">  
            </div>
            <div class="field_two">    
                    <label class="label-font" >最後進場日期</label>
                    <div v-if="valid_sale.toFactoryDate" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>

                     <input  v-model="form_sale.toFactoryDate" placehilder="請輸入" class="input" style="height:55px;">  
            </div>
            
            <div class="field_two ">    
                    <label class="label-font" >價錢</label>
                    <div v-if="valid_sale.price" class="valid_warn">
                        <span >*此欄位不能空</span>
                    </div>

                     <input  v-model="form_sale.price" placehilder="請輸入" class="input" style="height:55px;">  
            </div>
        </form>
        <div class="button_function" style="margin-left:10px" >
                <button @click.prevent="submit" class="submit">提交</button>
                <button class="submit" >清除</button>
        </div>
        
    </div>

  
</template>

<script>
export default {
    name: 'Application',
    props: {
        userInfo: Object,
    },
    data() {
        return {
            use_status:{
                user:true,
                company:false,
                sale:false,
            },
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
            valid:{
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
        submit:function(){
            if (this.form.applier==null){
                this.valid.applier = true;
            }
            else this.valid.applier =false;
            
            if (this.form.phone==null){
                this.valid.phone = true;
            }
            else this.valid.phone =false;
            
            if (this.form.email==null){
                this.valid.email = true;
            }
            else this.valid.email =false;
            
            if (this.form.satellite_name==null){
                this.valid.satellite_name = true;
            }
            else this.valid.satellite_name =false;
            

            if (this.form.weight==null){
                this.valid.weight = true;
            }
            else this.valid.weight =false;

            if (this.form.height==null){
                this.valid.height = true;
            }
            else this.valid.height =false;

            if (this.form.inclination==null){
                this.valid.inclination = true;
            }
            else this.valid.inclination =false;

            if (this.form.launchDate==null){
                this.valid.launchDate = true;
            }
            else this.valid.launchDate =false;
            
            if (this.form.toFactoryDate==null){
                this.valid.toFactoryDate = true;
            }
            else this.valid.toFactoryDate =false;
            
            if (this.form.budget==null){
                this.valid.budget = true;
            }
            else this.valid.budget =false;
            
           
        }
       

    },
    created() {
        console.log(this.userInfo)
    }
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