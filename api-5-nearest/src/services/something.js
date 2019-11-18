const axios = require('axios').default;

async function something(){
    const TOKEN = await axios({
        method: 'post',
        url: 'http://localhost:9090/api/auth/login',
        data: { 
            username: "tenant@thingsboard.org", password: "tenant"
        },
	})
	return null;
}

module.exports = something;
