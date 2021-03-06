/* eslint-disable */
import { request } from './api'
import { config } from '../config'

const API_HOST = config.API_HOST;

export function postRegist(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/client/register`;
    try {
        const res = request({
            uri,
            method: 'POST',
            data: {
                username: payload.username,
                passwd: payload.password,
                name: payload.fullname,
                phone: payload.phone,
                email: payload.email,
                is_launch_company: (payload.permission === "company" ? true : false),
            },
            auth:false,
        });
        res.then(function(response) {
            switch(response.data.code){
                case 200:
                    onSuccess();
                    break;
                case 401:
                    onFailed();
                    break;
            }
        })
    } catch (e) {
        console.log(e);
    }
}