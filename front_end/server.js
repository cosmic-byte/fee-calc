require("babel-core/register");
require("babel-polyfill");
const express = require("express");
const path = require('path');
const PORT = process.env.PORT || 8080;

// Define Express App
const app = express();

app.use(express.static(__dirname));

//// send the user to index html page inspite of the url
app.get('*', (req, res) => {
  res.sendFile(path.resolve(__dirname, 'public/index.html'));
});

app.listen(PORT, () => {
  console.log("Server connected at:", PORT);
});
