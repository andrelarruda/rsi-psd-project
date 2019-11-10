import React,{Component} from 'react';
const axios = require('axios')
import { StyleSheet, Text, View,TouchableOpacity,TextInput } from 'react-native';

type Props={};
export default class App extends Component<Props>{
  constructor(props){
    super(props)
     this.state={resultado:"2",lat ,lon};
    this.estacao= this.estacao.bind(this)
  }

  estado={
    resultado:""
  }
  
   estacao(){
  
   
  axios.get('http://192.168.0.101:3333/-8.054293/-34.913951')
  .then( (response => {
    var r= this.state
    r.resultado=response.data
    this.setState(r)

})) .catch(function (error) {
    // handle error
    console.log(error);
  })
 
}


  


  


render(){
  
  return (
    <View  style={styles.container}>
      <Text style={styles.h1Text}>Calculador de IH</Text>
      <View style={styles.inputBox}>
      <TextInput style={styles.input} placeholder="Longitude" placeholderTextColor="black"></TextInput>
      <TextInput style={styles.input} placeholder="Latitude" placeholderTextColor="black"></TextInput>
      
      </View>
      <TouchableOpacity onPress={this.estacao} style={styles.button}><Text style={styles.textButton}>Calcular</Text></TouchableOpacity>
      <Text style={styles.txtResult}>{this.state.resultado}</Text>



    </View>
  );
}
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent:"center"
  },
  inputBox:{
      marginTop:10,
     flexDirection:"row",
     height:200,
     backgroundColor:"#fff"
     
  },
  input:{
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#d6d7da',
    height:50,
    textAlign:"center",
    width:"50%",
    fontSize:15,
    marginTop:50,
    backgroundColor:"gray"
  },
  h1Text:{
    fontSize:50
  },
  txtResult:{
    fontSize:20,
    marginTop:70
  },
  textButton:{
    fontSize:15,
    
  },
  button:{
    width:"50%",
    alignItems:"center",
    justifyContent:"center",
    backgroundColor:"blue",
    borderRadius:5,
    borderWidth:2,
    height:50,
    marginBottom:100
    
  }

})
