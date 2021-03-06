const axios = require('axios');
const devicesID = require('../db/devices');
const instance = axios.create({
	baseURL: 'http://localhost:9090'
});

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

function get5Nearest(lat, lon, cidades) {
	// cidades - JSON Array
	let distancias = []

	for (let i = 0; i < cidades.length; i++) {
		distancias[i] = cidades[i];
		distancias[i].distancia = getDistance(lat, lon, cidades[i].lat, cidades[i].long);
	}

	distancias.sort(function (a, b) {
		return a.distancia - b.distancia;
	});

	return distancias.slice(0, 5);
}

async function getToken() {
	// FAZ REQUISIÇÃO DO TOKEN - OK
	const requisicaoToken = await axios({
		method: 'post',
		url: 'http://localhost:9090/api/auth/login',
		data: {
			username: "tenant@thingsboard.org", password: "tenant"
		},
	})

	return requisicaoToken.data.token;
}

async function consultarDeviceTB(authToken, idDevice) {
	instance.defaults.headers.common['X-Authorization'] = 'Bearer ' + authToken;
	
	let response = null;
	try{
		const consultaTB = await instance.get(`/api/plugins/telemetry/DEVICE/${idDevice}/values/timeseries`);
		response = consultaTB.data;
	}
	catch(err){
		response = err;
	}
	
	return response;
}

async function determinaHICadaCidade(listaCidades) {
	TOKEN = await getToken();
	
	for (let i = 0; i < listaCidades.length; i++) {
		cidade = listaCidades[i];

		//obtem o id do Device de acordo com o nome da cidade
		const idDevice = devicesID[cidade.nome];

		const consultaDevice = await consultarDeviceTB(TOKEN, idDevice);

		// para pegar apenas o valor do HI daquela cidade que tá no TB
		const hiDevice = consultaDevice["hi"][0]["value"];

		listaCidades[i].hi = Number(hiDevice);
	}

	return listaCidades;
}

module.exports = { get5Nearest, getDistance, getToken, determinaHICadaCidade, consultarDeviceTB }
