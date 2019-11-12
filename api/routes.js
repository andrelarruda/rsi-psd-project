const express = require('express');
const routes = express.Router();

const cities = {

	Recife: {
		lat: -8.05928,
		long: -34.959239
	},
	Petrolina: {
		lat: -9.388323,
		long: -40.523262

	},
	Arco_Verde: {
		lat: -8.433544,
		long: -37.055477
	},
	Garanhuns: {
		lat: -8.91095,
		long: -36.493381,
	},
	Surubim: {
		lat: -7.839628,
		long: -35.801056
	},

	Cabrobo: {
		lat: -8.504,
		long: -39.31528
	},
	Caruaru: {
		lat: -8.236069,
		long: -35.98555
	},
	Ibimirim: {
		lat: -8.509552,
		long: -37.711591
	},
	Serra_Talhada: {
		lat: -7.954277,
		long: -38.295082
	},
	Floresta: {
		lat: -8.598785,
		long: -38.584062
	},
	Palmares: {
		lat: -8.666667,
		long: -35.567921
	},
	Ouricuri: {
		lat: -7.885833,
		long: -40.102683
	},
	Salgueiro: {
		lat: -8.0580556,
		long: -39.096111
	},
}

function getDistance(lat1, lon1, lat2, lon2) {
	Number.prototype.toRad = function () {
		return this * Math.PI / 180;
	}
	var R = 6371;
	var x1 = lat2 - lat1;
	var dLat = x1.toRad();
	var x2 = lon2 - lon1;
	var dLon = x2.toRad();
	var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
		Math.cos(lat1.toRad()) * Math.cos(lat2.toRad()) *
		Math.sin(dLon / 2) * Math.sin(dLon / 2);
	var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
	var d = R * c;

	return d

}

function getCidadeMenorDistancia(lat, lon, cidades) {
	var cidadeMaisProxima
	let distancia = 1000000000;


	for (cidade in cidades) {
		let resultado = getDistance(cities[cidade].lat, cities[cidade].long, lat, lon)
		if (resultado < distancia) {
			distancia = resultado
			cidadeMaisProxima = cidade

		}

	}
	return cidadeMaisProxima
}


routes.get('/:lat/:long', (req, res) => {

	const { lat, long } = req.params
	const resposta = getCidadeMenorDistancia(parseFloat(lat), parseFloat(long), cities)
	return res.send(resposta)

});

module.exports = routes;
