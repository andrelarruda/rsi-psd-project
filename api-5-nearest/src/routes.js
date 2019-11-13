const routes = require('express').Router();
const data = require('./db/data.json');
const servicos = require('./services/servicos');

routes.get('/', (req, res) => {
	res.json({message: 'This is the entry point. For data, you must make a post request to the following URL: localhost:3001/api/5nearest/:lat/:long'});
});

routes.get('/api/cities', (req, res)=> {
	res.json(data);
});

routes.post('/api/5nearest/', (req, res) => {
	const cidade = req.body;

	const result = servicos.get5Nearest(cidade.lat, cidade.long, data.cities);
	
	return res.json(result);
});

module.exports = routes;
