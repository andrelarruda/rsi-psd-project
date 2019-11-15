const routes = require('express').Router();
const servicos = require('./services/servico');
const data = require('./db/data.json');


routes.get('/', (req, res) => {
	var resultado=servicos.idw(data.cities)
	return res.send(String(resultado))
});

module.exports = routes;
