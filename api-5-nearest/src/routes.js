const routes = require('express').Router();
const data = require('./db/data.json');
const servicos = require('./services/servicos');
const axios = require('axios').default;
const instance = axios.create({
	baseURL: 'http://localhost:9090'
});
let TOKEN = null;

routes.get('/', (req, res) => {
	res.json({ message: 'This is the entry point. For data, you must make a post request to the following URL: localhost:3001/api/5nearest/:lat/:long' });
});

routes.get('/api/cities', (req, res) => {
	res.json(data);
});

routes.get('/api/5nearest/:lat/:long', (req, res) => {
	const { lat, long } = req.params

	const result = servicos.get5Nearest(parseFloat(lat), parseFloat(long), data.cities);

	return res.json(result);
});


routes.get('/teste', async (req, res) => {

	//setar o id do Device
	const deviceID = "67f61240-0a2c-11ea-a698-0bc6fc91ecdf"

	// FAZ REQUISIÇÃO DO TOKEN - OK
	const requisicaoToken = await axios({
		method: 'post',
		url: 'http://localhost:9090/api/auth/login',
		data: {
			username: "tenant@thingsboard.org", password: "tenant"
		},
	})

	TOKEN = requisicaoToken.data.token;

	xAuthorization = 'Bearer ' + TOKEN;

	instance.defaults.headers.common['X-Authorization'] = xAuthorization;
	instance.get(`/api/plugins/telemetry/DEVICE/${deviceID}/values/timeseries?keys=HI,umidade,temperatura`)
		.then(response => {
			// console.log(response)
			return res.status(200).json(response.data);
		})
		.catch(err => {
			//console.log(err);
			return res.status(401).json(err)
		});


	// http://localhost:9090/swagger-ui.html#!/telemetry-controller/getTimeseriesKeysUsingGET
	// https://thingsboard.io/docs/reference/rest-api/
	// https://thingsboard.io/docs/user-guide/telemetry/#data-query-api
});

module.exports = routes;
