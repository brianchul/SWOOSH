<template>
    <form @submit.prevent="afterSubmit($event)" class="formWrapper center">
        <div class='formItem'>
            <label>帳號</label>
            <input type="text" v-model="form.username" required/>
        </div>
        <div class='formItem'>
            <label>密碼</label>
            <input type="password" v-model="form.password" required/>
        </div>
        <div v-if='status === "regist"'>
            <div class='formItem'>
                <label>再次輸入密碼</label>
                <input type="password" v-model="form.checkPassword" required/>
            </div>
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
        <button type="submit" @click='apiTest(form)'>{{(status === 'login') ? '登入' : '註冊'}}</button>
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
        apiTest: function(payload) {
            switch(this.status) {
                case 'login':
                    localStorage.setItem('userInfo',JSON.stringify({
                        isLoggedIn: true,
                        userId: null,
                        fullname: 'Super Rocket',
                        permission: payload.username,
                    }))
                    this.$emit('setLogin')
                    // api.postLogin({
                    //     username: payload.username,
                    //     password: payload.password,
                    // });
                    break;
                case 'regist':
                    // api.postRegist(payload);
                    break;
            }
        },
        afterSubmit: function(event) {
            event.preventDefault();
            this.$emit('closeForm');
        } 
    }
}
</script>

<style scoped>
.formWrapper {
  flex-direction: column;
  height: 70vh;
  width: 100%;
  background-color: black;
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
  color: #fff;
  font-size: 18px;
}
.formItem input {
  width: 180px;
  height: 20px;
  border-radius: 10px;
  padding: 10px;
}
.formItem select {
  width: 200px;
  height: 40px;
  border-radius: 10px;
}
form button {
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