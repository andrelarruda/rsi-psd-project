const routes = require('express').Router();
const data = require('./db/data.json');
const servicos = require('./services/servicos');

routes.get('/', (req, res) => {
	res.json({message: 'This is the entry point. For data, you must make a post request to the following URL: localhost:3001/api/5nearest/:lat/:long'});
});

routes.get('/api/cities', (req, res)=> {
	res.json(data);
});

routes.get('/api/5nearest/:lat/:long', (req, res) => {
	const { lat, long } = req.params

	const result = servicos.get5Nearest(parseFloat(lat),parseFloat(long), data.cities);
	
	return res.json(result);
});

module.exports = routes;
