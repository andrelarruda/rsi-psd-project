
function idw(listaDeCidades){
    var totalDistancia=0;
    var totalIhXdist=0;
    var resultado=0;

    for (var i = 0 ; i < listaDeCidades.length ; i++){

        totalDistancia+=listaDeCidades[i].distancia
        totalIhXdist+=listaDeCidades[i].hi*listaDeCidades[i].distancia
	
	}

resultado=totalIhXdist/totalDistancia

return resultado.toFixed(3)

}

module.exports = {idw}
