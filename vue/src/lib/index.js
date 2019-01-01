import * as user from './user'
import * as login from './login'
import * as regist from './regist'
import * as need from './need'
import * as mission from './mission'

export default {
    ...login,
    ...user,
    ...regist,
    ...need,
    ...mission,
}
