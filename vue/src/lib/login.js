/* eslint-disable */
import { request } from './api'
import { config } from '../config/'

const API_HOST = config.API_HOST;

export function postLogin(payload,onSuccess,onFailed) {
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
            let data = response.data.data
            switch(response.data.code){
                case 200:
                    onSuccess(data);
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

export function getClientById(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/client/findOne`;
    try {
        const res = request({
            uri,
            method: 'POST',
            data: {
                id: parseInt(payload),
            },
            auth:false,
        });
        res.then(function(response) {
            let data = response.data.data
            switch(response.data.code){
                case 200:
                    onSuccess(data);
                    break;
                case 400:
                    onFailed();
                    break;
            }
        })
    } catch (e) {
        console.log(e);
    }
}