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
	// const deviceID = "77f00580-0a58-11ea-bd97-470d24539586" //device 'another'

	TOKEN = await servicos.getToken();

	instance.defaults.headers.common['X-Authorization'] = 'Bearer ' + TOKEN;
	// instance.get(`/api/plugins/telemetry/DEVICE/${deviceID}/values/timeseries?keys=umidade,temperatura,lat,long`)
	instance.get(`/api/plugins/telemetry/DEVICE/${deviceID}/values/timeseries?keys=umidade,temperatura&startTs=1555200&endTs=1574121600&agg=AVG`)
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
