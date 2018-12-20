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
        <button type="submit" @click.prevent='apiTest(form)'>{{(status === 'login') ? '登入' : '註冊'}}</button>
    </form>
</template>

<script>
import api from '../../lib/' 
import Homepage from '../Homepage.vue'

export default {
    name: 'Form',
    props: {
        status: String,
    },
    data() {
        return {
            loginStatus: null, // true(succeed), false(failed), null(not login yet)
            registStatus: null, // true(succeed), false(failed), null(not regist yet)
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
        setLogin: function() {
            this.$emit('setLogin');
            this.$emit('closeForm');
        },
        setAlert: function() {
            this.$emit('setAlert');
        },
        apiTest: function(payload) {
            switch(this.status) {
                case 'login':
                    api.postLogin(payload,this.setLogin,this.setAlert);
                    break;
                case 'regist':
                    if(payload.checkPassword != payload.password){
                        localStorage.setItem('alert',JSON.stringify({
                            hook: true,
                            status: 'fail',
                            title: '操作失敗：',
                            message: '密碼錯誤，請重新輸入',
                        }))
                        this.$emit('setAlert');
                    } else {
                        api.postRegist(payload);
                        this.$emit('closeForm');
                    }
                    // api.postRegist(payload);
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