const routes = require('express').Router();
const servicos = require('./services/servico');
const data = require('./db/data.json');


routes.post('/cities', (req, res) => {
	var resultado=servicos.idw(req.body)
	return res.send(String(resultado))
});

module.exports = routes;
