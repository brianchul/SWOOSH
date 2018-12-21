import { request } from './api'
import { config } from '../config/'

const API_HOST = config.API_HOST;

export function postLogin(payload,setLogin,setAlert) {
    let uri = `${API_HOST}/client/login`;
    try {
        const res = request({
            uri,
            method: 'POST',
            data: {
                username: payload.username,
                passwd: payload.password,
            },
            auth:false,
        });
        res.then(function(response) {
            console.log(response.data.code)
            let data = response.data.data
            switch(response.data.code){
                case 200:
                    localStorage.setItem('userProfile',JSON.stringify(data))
                    localStorage.setItem('userInfo',JSON.stringify({
                        isLoggedIn: true,
                        userId: 1,
                        fullname: data.name,
                        permission: (data.is_launch_company) ? 'company' : 'user',
                    }))
                    setLogin();
                    break;
                case 401:
                    localStorage.setItem('alert',JSON.stringify({
                        hook: true,
                        status: 'fail',
                        title: '登入失敗：',
                        message: '帳號或密碼錯誤，請重新輸入',
                    }))
                    setAlert();
                    break;
            }
        })
    } catch (e) {
        console.log(e);
    }
}