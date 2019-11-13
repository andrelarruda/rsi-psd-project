const routes = require('express').Router();

routes.get('/', (req, res) => {
	res.json({message: 'hello world!'});
});

module.exports = routes;
