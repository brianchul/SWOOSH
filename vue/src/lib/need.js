import { request } from './api'
import { config } from '../config/'

const API_HOST = config.API_HOST;

export function postNeed(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/clientOrder/add`;
    try {
        const res = request({
            uri,
            method: 'POST',
            data: payload,
            auth:false,
        });
        res.then(function(response) {
            let data = response.data.data
            console.log(response);
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

export function getAllNeeds(onSuccess,onFailed) {
    let uri = `${API_HOST}/clientOrder`;
    try {
        const res = request({
            uri,
            method: 'GET',
            auth:false,
        });
        res.then(function(response) {
            let data = response.data.data
            console.log(response.data);
            switch(response.data.code){
                case 200:
                    onSuccess(data);
                    break;
                case 404:
                    onFailed();
                    break;
            }
        })
    } catch (e) {
        console.log(e);
    }
}