const routes = require('express').Router();
const data = require('./db/data.json');
const servicos = require('./services/servicos');
const axios = require('axios').default;
const getToken = require('./services/getToken');
const instance = axios.create({
	baseURL: 'http://172.16.206.40:9090'
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
	// FAZ REQUISIÇÃO DO TOKEN - OK
	// const requisicaoToken = await axios({
	// 	method: 'post',
	// 	url: 'http://localhost:9090/api/auth/login',
	// 	data: { 
	// 		username: "tenant@thingsboard.org", password: "tenant"
	// 	},	
	// })

	TOKEN = getToken;

	console.log(TOKEN);

	return res.json()

	// http://localhost:9090/swagger-ui.html#!/telemetry-controller/getTimeseriesKeysUsingGET
	// https://thingsboard.io/docs/reference/rest-api/
	// https://thingsboard.io/docs/user-guide/telemetry/#data-query-api
	




	// instance.defaults.headers.common['X-Authorization'] = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJ1c2VySWQiOiJkNzlmOGYxMC1jZDhhLTExZTktYTAzNC0xNWFlYzhhZjRmMGQiLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiZDc1NWRiZTAtY2Q4YS0xMWU5LWEwMzQtMTVhZWM4YWY0ZjBkIiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNTc0MDg1NDA2LCJleHAiOjE1NzQwOTQ0MDZ9.uKoT3XVAXRsuqHWd3gkoZTbiUaXOsAWAU0-FUWacFFAOyry62AyRomFsSScIJbT9ER-yzU9AUmmrODMxYujtjg'
	// instance.get('/api/plugins/telemetry/DEVICE/75434b80-e5fa-11e9-bebd-e35bcf2d23e2/values/timeseries?keys=HI,umidade,temperatura')
	// 	.then(response => {
	// 		console.log(response)
	// 		return res.status(200).json(response.data);
	// 	})
	// 	.catch(err => {
	// 		//console.log(err);
	// 		return res.status(401).json(err)
	// 	});
});

module.exports = routes;
