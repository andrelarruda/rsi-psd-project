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
  







}


console.log(cities.Recife)


app.get('/:lat/:long',(req,res)=>{

    const {lat,long}=req.params
    return res.send(long)

})

app.listen('3333')