mainFunction2();

function mainFunction2(){
    Promise.all([downloadCat('cats.com'),cropCatPhoto('^()^'),printPhoto('^()^-')]).then((results)=>{
        console.log(results);
    });
}

function mainFunction(){
    downloadCat('cats.com').then((downloadResults) =>{
        cropCatPhoto(downloadResults).then((cropCatPhotoResults) =>{
            printPhoto(cropCatPhotoResults).then((printPhotoResults) =>{
                console.log(printPhotoResults);
            }, (printError) =>{
                console.log(printError);
            });
        }, (cropCatPhotoError) =>{
            console.log(cropCatPhotoError);
        });
    }, (downloadError) =>{
        console.log(downloadError);
    });
}


function downloadCat(url){
    return new Promise((resolve, reject)=>{
        console.log(`retrieving cat phone from ${url}`);
        var catPhoto = `^()^`;
        if (true){
            resolve(catPhoto);
        } else {
            reject('error retrieving photo, bad url');
        }
    });
}

function cropCatPhoto(photo){
    return new Promise((resolve, reject) => {
        console.log("cropping photo");
        photo += '-';
        if (true){
            resolve(photo);
        } else {
            reject('error cropping photo');
        }
    });
}

function printPhoto(photo){
    return new Promise((resolve, reject) => {
        console.log(`printing photo: ${photo}`);
        if(true){
            resolve("printed");
        } else {
            reject("error");
        }
    });
}

/*
mainFunction();
// typeing 
// go through cat example. then refactor
function mainFunction(){
    downloadCat('cats.com', (photo)=>{
        console.log(photo);
        cropCatPhot(photo, (photo) => {
            console.log(photo);
            displayPhoto(photo, (home) =>{
                console.log(`sending back home: ${home}`);

            })
        })
    })
}

function downloadCat(url, callback){
    console.log(`Fetching url: ${url}`);
    var photo = '^()^';
    callback(photo);
}

function cropCatPhot(photo, callback){
    console.log(`cropping photo`);
    photo += '-';
    callback(photo);
}

function displayPhoto(photo, callback){
    console.log(photo);
    var home = "home";
    callback(home);
}



var p1 = Promise.resolve(3);
var p2 = 1337;
var p3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, 'foo');
}); 

Promise.all([p1, p2, p3]).then(values => { 
  console.log(values[0]); // [3, 1337, "foo"] 
  console.log(values[2]); // [3, 1337, "foo"] 
});



*/


