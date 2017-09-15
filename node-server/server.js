const express = require ('express');
const request = require('superagent');
var path = require('path');

// tell node I am serving static files
const app = express();
app.use('/static', express.static(path.join(__dirname, 'public')));
app.use('/node_modules', express.static(path.join(__dirname, 'node_modules')));

const server = app.listen('8081', () =>{
    console.log(`Server running at address: ${server.address().address} on port: ${server.address().port}`)
})

app.get('/makeRequest',(req, res)=>{
    console.log('back at server');
    request.get('https://www.google.com/', (err, res) =>{
        console.log(res);
    })
})

app.get('/', (req, res) =>{
    res.sendFile( __dirname + "/" + "public/index.html" );
})