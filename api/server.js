const express= require('express');
const app= express();
const PORT = 3333;
const axios = require('axios');

const routes = require('./routes');

app.use(express.json());

app.use(routes);

app.listen(PORT, () => console.log(`Listening on port ${PORT}...`));
