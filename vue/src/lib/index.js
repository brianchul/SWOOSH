import * as user from './user'
import * as login from './login'
import * as regist from './regist'

export default {
    ...login,
    ...user,
    ...regist,
}
