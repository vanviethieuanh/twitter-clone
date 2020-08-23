import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

export default () =>{
    return axios.create({
        baseURL: `http://127.0.0.1:8000`
    })
}