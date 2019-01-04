/* eslint-disable */
import { request } from './api'
import { config } from '../config/'

const API_HOST = config.API_HOST;

export function getAllMission(onSuccess,onFailed) {
    let uri = `${API_HOST}/mission`;
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
                case 400:
                    onFailed();
                    break;
            }
        })
    } catch (e) {
        console.log(e);
    }
}

export function patchMission(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/mission/patch`;
    try {
        const res = request({
            uri,
            method: 'POST',
            data: {
                id: parseInt(payload.id),
                launch_date:payload.launch_date,
                launch_rocket:payload.launch_rocket,
                status:payload.status,
                target_inclination: payload.target_inclination,
                target_height_km:payload.target_height_km,
                rocket_max_payload_weight: parseInt(payload.rocket_max_payload_weight),
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

export function getAllMissionOrder(onSuccess,onFailed) {
    let uri = `${API_HOST}/missionOrder`;
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
                case 400:
                    onFailed();
                    break;
            }
        })
    } catch (e) {
        console.log(e);
    }
}

export function postMissionOrder(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/missionOrder/add`;
    try {
        const res = request({
            uri,
            method: 'POST',
            data: payload,
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

export function patchMissionOrder(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/missionOrder/patch`;
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

export function getMission(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/mission/findOne`;
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

export function getMissionOrderById(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/missionOrder/findOne`;
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

export function deleteMissionById(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/mission/delete`;
    try {
        const res = request({
            uri,
            method: 'POST',
            data: {
                id: parseInt(payload.id),
            },
            auth:false,
        });
        res.then(function(response) {
            let data = response.data.data
            console.log(data)
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

export function deleteMissionOrderById(payload,onSuccess,onFailed) {
    let uri = `${API_HOST}/missionOrder/delete`;
    try {
        const res = request({
            uri,
            method: 'POST',
            data: {
                id: parseInt(payload.id),
            },
            auth:false,
        });
        res.then(function(response) {
            let data = response.data.data
            console.log(data)
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
