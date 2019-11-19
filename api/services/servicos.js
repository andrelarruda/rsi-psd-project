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
		let resultado = getDistance(cidades[cidade].lat, cidades[cidade].long, lat, lon)
		if (resultado < distancia) {
			distancia = resultado
			cidadeMaisProxima = cidade

		}

	}
	return cidadeMaisProxima
}

module.exports = {getCidadeMenorDistancia,getDistance}