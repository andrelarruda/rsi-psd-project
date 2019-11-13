const routes = require('express').Router();
const cities = require('./data/cities.json');
const servicos = require('./services/servicos');

routes.get('/', (req, res) => {
	res.json({message: 'hello world!'});
});

routes.get('/api/cities', (req, res)=> {
	res.json(cities);
});

routes.post('/api/5nearest', (req, res) => {
	cityList = cities.cities;
	let cidade = {}
	const { nome, lat, long } = req.body;

	const recife = {
		nome: "Recife",
		lat: -8.05428,
		long: -34.8813,
	}

	const distancia = servicos.getDistance(lat, long, recife.lat, recife.long);
	
	// for (let i = 0 ; i < cityList.length ; i++){
		
	// }

	return res.json({distancia});
});

module.exports = routes;
