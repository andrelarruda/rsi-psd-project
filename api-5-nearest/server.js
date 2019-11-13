const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const PORT = 3000;

const routes = require('./src/routes');

app.use(bodyParser.urlencoded({extended: true}));

app.use(routes);

app.listen(PORT, () => console.log(`Server listening on port ${PORT}...`));


