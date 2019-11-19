const express = require('express');
const routes = express.Router();
const  cities  = require('./services/data')
const servicos= require('./services/servicos')


routes.get('/:lat/:long', (req, res) => {

	const { lat, long } = req.params
	const resposta = servicos.getCidadeMenorDistancia(parseFloat(lat), parseFloat(long), cities)
	return res.send(resposta)


});

module.exports = routes;
