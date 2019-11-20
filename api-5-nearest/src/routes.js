const routes = require('express').Router();
const data = require('./db/data.json');
const servicos = require('./services/servicos');



routes.get('/api/5nearest/:lat/:long', async (req, res) => {
	const { lat, long } = req.params

	let estacoesProximas = servicos.get5Nearest(parseFloat(lat), parseFloat(long), data.cities);

	let estacoesProximasComHI = await servicos.determinaHICadaCidade(estacoesProximas);

	return res.json(estacoesProximasComHI);
});




module.exports = routes;