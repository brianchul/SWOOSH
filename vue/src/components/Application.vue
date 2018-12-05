<template>
   
    <div>
      <div class="title font-stytle"> 發射申請 </div>
      
        <form class="fields ">
          <div class="field_third">
            <label class="label-font" >申請單位</label>
            <input type="text" class="input"> </input>
          </div>
          <div class="field_third">
            <label class="label-font" >電話號碼</label>
            <input type="text" class="input"> </input>
          </div>
          <div class="field_third">
            <label class="label-font" >E-MAIL</label>
            <input type="text" class="input"> </input>
          </div>
          <div class="field_four">
            <label class="label-font" >衛星名稱</label>
            <input type="text" class="input"> </input>
          </div>
          <div class="field_four">
            <label class="label-font" >衛星重量（KG）</label>
            <input type="text" class="input"> </input>
          </div>
          <div class="field_four">
            <label class="label-font" >發射高度</label>
            <form>
                <select name="height" class="dropdown">
                　<option value="Taipei">台北</option>
                　<option value="Taoyuan">桃園</option>
                　<option value="Hsinchu">新竹</option>
                　<option value="Miaoli">苗栗</option>
                　...
                </select>
            </form>
          </div>
          <div class="field_four">
            <label class="label-font" >傾角-inclination</label>
            <input type="text" class="input"> </input>
          </div>
          <div class="field_third">
            <label class="label-font" >發射日期</label>
            <input type="text" class="input"> </input>
          </div>
          <div class="field_third">
            <label class="label-font" >進場日期</label>
            <input type="text" class="input"> </input>
          </div>
          <div class="field_third">
            <label class="label-font" >此次預算</label>
            <input type="text" class="input"> </input>
          </div>
          <div class="purpose ">
            <label class="label-font" >目的</label>
            <textarea type=text class="input"style="height:200px;" >
            </textarea>
          </div>
          <div class="button_function" >
            <button class="submit">提交</button>
            <button class="submit" >清除</button>
          </div>
        </form>
      </div>
    </div>
    

</template>

<script>
export default {
    name: 'Application',
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
    background-color:transparent;
    font-size:20px;
    color:#ffffff;
    border-radius: 4px;
    border: solid 1px #ffffff;
    
}
</style>