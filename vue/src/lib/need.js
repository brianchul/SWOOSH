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

export function patchNeed(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/clientOrder/patch`;
    try {
        const res = request({
            uri,
            method: 'POST',
            data: {
                id: parseInt(payload.id),
                satellite_name:payload.satellite_name,
                weight_kg: parseInt(payload.weight_kg),
                purpose:payload.purpose,
                request_by: parseInt(payload.request_by),
                eta_height_km:payload.eta_height_km,
                arrival_date:payload.arrival_date,
                inclination:payload.inclination,
                budget_billion:payload.budget_billion,
                launch_day:payload.launch_day,
                status:payload.status 
            },
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

