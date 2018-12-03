import { request } from './api'
import { config } from '../config/'

const API_HOST = config.API_HOST;

export function postUser(payload) {
    let uri = `${API_HOST}/api/user`;
    try {
        const res = request({
            uri,
            method: 'POST',
            data: {
                studentNumber: payload.studentNumber,
            },
            auth:false,
        });
    } catch (e) {
        console.log(e);
    }
}