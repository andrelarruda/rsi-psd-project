const axios = require('axios').default;

async function getToken(){
    const TOKEN = await axios({
        method: 'post',
        url: 'http://localhost:9090/api/auth/login',
        data: { 
            username: "tenant@thingsboard.org", password: "tenant"
        },
    })
    return TOKEN
}

module.exports = getToken;