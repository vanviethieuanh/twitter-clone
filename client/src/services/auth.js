import Api from '@/services/api.js'

export default{
    register (credentials)
    {
        return Api().post('register', credentials)
    },
    logIn (credentials)
    {
        return Api().post('login/token', credentials)
    }
}