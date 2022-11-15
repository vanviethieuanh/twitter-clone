import axios from './api'

export const Login = async function (username, password) {
  return await axios.post('auth/token', {
    username: username,
    password: password
  })
}

export const Register = async function ({ last_name, first_name, email, password, username }) {
  return await axios.post('auth/register', {
    last_name: last_name,
    first_name: first_name,
    email: email,
    password: password,
    username: username
  })
}
