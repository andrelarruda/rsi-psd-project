const routes = require('express').Router();
const data = require('./db/data.json');
const servicos = require('./services/servicos');
const axios = require('axios').default;
const instance = axios.create({
	baseURL: 'http://localhost:9090'
});
let TOKEN = null;

routes.get('/', (req, res) => {
	res.json({ message: 'This is just the entry point. For data, you must make a get request to the following URL: localhost:3001/api/5nearest/:lat/:long' });
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

	let cidades = servicos.get5Nearest(-8.05928, -34.959239, data.cities);

	let result = await servicos.determinaHICadaCidade(cidades);

	return res.send(result);

});

module.exports = routes;

// http://localhost:9090/swagger-ui.html#!/telemetry-controller/getTimeseriesKeysUsingGET
// https://thingsboard.io/docs/reference/rest-api/
// https://thingsboard.io/docs/user-guide/telemetry/#data-query-api
