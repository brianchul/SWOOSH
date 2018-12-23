<template>
    <form class="formWrapper center">
        <div class="formItemWrapper">
            <div class='formItem'>
                <label>帳號</label>
                <input type="text" v-model="form.username" required/>
            </div>
            <div class='formItem'>
                <label>密碼</label>
                <input type="password" v-model="form.password" required/>
            </div>
            <div class='formItem' v-if='status === "regist"'>
                <label>再次輸入密碼</label>
                <input type="password" v-model="form.checkPassword" required/>
            </div>
        </div>
        <div class="formItemWrapper" v-if='status === "regist"'>
            <div class='formItem'>
                <label>姓名</label>
                <input type="text" v-model="form.fullname" required/>
            </div>
            <div class='formItem'>
                <label>聯絡電話</label>
                <input type="text" v-model="form.phone" required/>
            </div>
            <div class='formItem'>
                <label>信箱</label>
                <input type="text" v-model="form.email" required/>
            </div>
            <div class='formItem'>
                <label>身份</label>
                <select v-model="form.permission" required>
                    <option value='user'>使用者</option>
                    <option value='company'>公司</option>
                </select>
            </div>
        </div>
        <button type="submit" @click.prevent='api(form)'>{{(status === 'login') ? '登入' : '註冊'}}</button>
    </form>
</template>

<script>
import api from '../../lib/' 

export default {
    name: 'Form',
    props: {
        status: String,
    },
    data() {
        return {
            form: {
                username: '',
                password: '',
                checkPassword: '',
                fullname: '',
                phone: '',
                email: '',
                permission: '',
            },
        }
    },
    methods: {
        loginOnSuccess: function(data) {
            localStorage.setItem('userInfo',JSON.stringify(data))
            this.$emit('setLogin');
            this.$emit('closeForm');
        },
        loginOnFailed: function() {
            this.$message({
                type: 'error',
                message: "帳號或密碼錯誤，請重新輸入",
                center: true
            })
        },
        registOnSuccess: function() {
            this.$message({
                type: 'success',
                message: "註冊成功",
                center: true
            })
            this.$emit('closeForm');
        },
        registOnFailed: function() {
            this.$message({
                type: 'error',
                message: "註冊失敗，帳戶名稱已被註冊",
                center: true
            })
        },
        api: function(payload) {
            switch(this.status) {
                case 'login':
                    api.postLogin(payload,this.loginOnSuccess,this.loginOnFailed);
                    break;
                case 'regist':
                    if(payload.checkPassword != payload.password){
                        this.$message({
                            type: 'error',
                            message: "密碼錯誤，請重新輸入",
                            center: true
                        })
                    } else {
                        api.postRegist(payload,this.registOnSuccess,this.registOnFailed);
                    }
                    break;
            }
        },
    }
}
</script>

<style scoped>
.formWrapper {
  height: 70vh;
  width: 100%;
  background-image: url(../../assets/roc1.jpg);
}
.formItemWrapper {
  display: flex;
  flex-direction: column;
}
.formItem {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 10px;
}
.formItem label {
  text-align: center;
  width: 120px;
  padding-right: 10px;
  color: black;
  font-size: 18px;
}
.formItem input {
  width: 176px;
  height: 16px;
  border-radius: 5px;
  padding: 10px;
  background: transparent;
  border: 2px solid black;
  color: black;
}
.formItem select {
  width: 200px;
  height: 40px;
  background: transparent;
  border: 2px solid black;
  color: black;
  text-indent: 10px;
}
form button {
  position: absolute;
  bottom: 130px;
  width: 100px;
  height: 40px;
  background-color: #fff;
  color: #000;
  border: 2px solid #000;
  border-radius: 10px;
}
form button:hover {
  background-color: #000;
  color: #fff;
  border: 2px solid #fff;
} 
</style>