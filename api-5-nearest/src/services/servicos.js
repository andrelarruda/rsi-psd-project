const axios = require('axios');
const devicesID = require('../db/devices');
const data = require('../db/data.json')

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

	for (let i = 0 ; i < cidades.length ; i++){
		distancias[i] = cidades[i];
		distancias[i].distancia = getDistance(lat, lon, cidades[i].lat, cidades[i].long);
	}

	distancias.sort( function(a, b){
		return a.distancia-b.distancia;
	});

	return distancias.slice(0, 5);
}

async function getToken(){
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

async function consultarTB(listaCidades){
	TOKEN = await getToken();

	const proximos = get5Nearest(-8.11278, -35.01472, data.cities);
	
	for (let i = 0; i < listaCidades.length; i++){
		cidade = listaCidades[i];

		//setar o id do Device
		let idDevice = devicesID[cidade.nome];
		// const deviceID = "77f00580-0a58-11ea-bd97-470d24539586" //device 'another'
	}

	return proximos;

	


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
}

module.exports = { get5Nearest, getDistance, getToken, consultarTB }
