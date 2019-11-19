const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const PORT = 3003;

const routes = require('./src/router');

app.use(bodyParser.urlencoded({extended: true}));

app.use(bodyParser.json());

app.use(routes);

app.listen(PORT, () => console.log(`Server listening on port ${PORT}...`));
