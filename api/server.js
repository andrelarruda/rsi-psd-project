const express= require('express')
const app= express()
const axios = require('axios')

const cities={

  Recife:{
    lat:-8.05928,
    long:-34.959239
  },
  Petrolina:{
    lat:-9.388323,
    long:-40.523262

  },
  Arco_Verde:{
    lat:-8.433544,
    long:-37.055477
  },
  Garanhuns:{
    lat:-8.91095,
    long:-36.493381,
  },
  Surubim:{
    lat:-7.839628,
    long:-35.801056
  },

  Cabrobo:{
    lat:-8.504,
    long:-39.31528
  },
  Caruaru:{
    lat:-8.236069,
    long:-35.98555
  },
  Ibimirim:{
    lat:-8.509552,
    long:-37.711591
  },
  Serra_Talhada:{
    lat:-7.954277,
    long:-38.295082
  },
  Floresta:{
    lat:-8.598785,
    long:-38.584062
  },
  Palmares:{
    lat:-8.666667,
    long:-35.567921
  },
  Ouricuri:{
    lat:-7.885833,
    long:-40.102683
  },
  Salgueiro:{
    lat:-8.0580556,
    long:-39.096111
  },
}




function getDistance(lat1,lat2,lon1,lon2){

  Number.prototype.toRad = function() {
    return this * Math.PI / 180;
 }
 
 
 var R = 6371; // km 
 //has a problem with the .toRad() method below.
 var x1 = lat2-lat1;
 var dLat = x1.toRad();  
 var x2 = lon2-lon1;
 var dLon = x2.toRad();  
 var a = Math.sin(dLat/2) * Math.sin(dLat/2) + 
                 Math.cos(lat1.toRad()) * Math.cos(lat2.toRad()) * 
                 Math.sin(dLon/2) * Math.sin(dLon/2);  
 var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
 var d = R * c; 
 
return d

}


let resposta= getDistance(-8.1617581,-34.920084,-8.1627533,-34.9172833)
console.log(resposta)

app.get('/:lat/:long',(req,res)=>{

    const {lat,long}=req.params
    return res.send(long)

})

app.listen('3333')