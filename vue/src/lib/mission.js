import { request } from './api'
import { config } from '../config/'

const API_HOST = config.API_HOST;

export function getAllMission(onSuccess,onFailed) {
    let uri = `${API_HOST}/client/mission`;
    try {
        const res = request({
            uri,
            method: 'GET',
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

export function getOneMission(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/client/mission`;
    try {
        const res = request({
            uri,
            method: 'POST',
            data: {
                // create_by: ,
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


export function getMission(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/client/mission`;
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