const express = require ('express');
const request = require('superagent');
const app = express();

const server = app.listen('8081', () =>{
    console.log(`Server running at address: ${server.address().address} on port: ${server.address().port}`)
})

app.get('/makeRequest',(req, res)=>{
    console.log('back at server');
    request.get('https://www.google.com/', (err, res) =>{
        console.log(res);
    })
    //make reqeuset to google
})

app.get('/', (req, res) =>{
    // user presses button
    // call (localhost/makeRequest);
    console.log('here')
    request.get('http://localhost:8081/makeRequest', (err, res) =>{
        console.log('ok')
    })
    // res.send('hello');
})