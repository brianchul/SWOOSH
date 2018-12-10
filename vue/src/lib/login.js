import { request } from './api'
import { config } from '../config/'

const API_HOST = config.API_HOST;

export function postLogin(payload) {
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
    } catch (e) {
        console.log(e);
    }
}