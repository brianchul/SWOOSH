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

export function postMission(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/mission/add`;
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

