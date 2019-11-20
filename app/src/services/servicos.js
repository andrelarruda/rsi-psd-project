const axios = require('axios')
  function fivenearest(lat,long){

       axios.get(`http://192.168.0.107:3001/api/5nearest/${lat}/${long}`)

    .then(function(response) {
      var array= []

     array.push(response.data)
  
  }) .catch(function (error) {
      // handle error
      console.log(error);
    })
    return array
}


function idw(fivelist){
  
  function axiosTest () {
    var strr = [];
       axios.get(url)
      .then(function(response){
              strr.push(response.data);
       })


       .catch(function(error){
              console.log(error);
          });
       return strr;
}   


}







module.exports={fivenearest,idw}