const express = require ('express');
const request = require('superagent');
var path = require('path');
const app = express.Router();
app.use('/static', express.static(path.join(__dirname, 'public')));
app.use('/node_modules', express.static(path.join(__dirname, 'node_modules')));

const server = app.listen('8081', () =>{
    console.log(`Server running at address: ${server.address().address} on port: ${server.address().port}`)
})

app.get('/getLatLng',(req, res)=>{
    console.log('back at server calling AerFrame');
    request.get('https://www.google.com/', (err, data) =>{
        console.log(data); 
        // just here for testing
        // send request "request sent"  or AerFrame response
        var response = { lat: 41.8993837, lng: -87.6641918 }; 
        res.send(response);
    })
})

app.post('/diplayLatLng', (req, res)=>{
    console.log(req)
})

app.get('/', (req, res) =>{
    res.sendFile( __dirname + "/" + "public/index.html" );
})