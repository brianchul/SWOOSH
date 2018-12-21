import { request } from './api'
import { config } from '../config'

const API_HOST = config.API_HOST;

export function postRegist(payload) {
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
        console.log(res)
    } catch (e) {
        console.log(e);
    }
}