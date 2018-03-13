'use strict'

const service = require('../server/service');
const http = require('http');
const request = require('superagent');


const server = http.createServer(service);
server.listen();
server.on('listening', function(){
    console.log(`IRIS-Time is listening on ${server.address().port} in ${service.get('env')} mode.`);

    const announce = () => {
        request.put(`http://127.0.0.1:3000/service/time/${server.address().port}`, (err, res) =>{
            if (err){
                console.log(err);
                console.log("error connecting to iris");
            }
            console.log(res.body);
        });
    };
    announce();
    setInterval(announce, 15*1000);

});

