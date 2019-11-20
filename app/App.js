import React,{Component} from 'react';
const servicos = require('./src/services/servicos')
const axios = require('axios')
import { StyleSheet, Text, View,TouchableOpacity,TextInput } from 'react-native';

type Props={};
export default class App extends Component<Props>{
  constructor(props){
    super(props)
     this.state={resultado:"" , lat:"",long:"",json:""};
     
    this.mediaHI= this.mediaHI.bind(this)
    this.nearest= this.nearest.bind(this)

  }

  estado={
    resultado:""
  }


  async nearest(){
   await axios.get(`http://172.16.205.131:3001/api/5nearest/${this.state.lat}/${this.state.long}`)
    .then( (response => {
      var j= this.state
      j.json=response.data
      this.setState(j)
  })) .catch(function (error) {
      // handle error
      console.log(error);
    })
    this.mediaHI()
  }
  async mediaHI(){
    await axios({
      method: 'post', // verbo http
      url: 'http://172.16.205.131:3003/cities', // url
      data:this.state.json,
    })
    .then(response => {
      var r = this.state
      r.resultado= JSON.stringify(response.data)
      this.setState(r)   
    })
    .catch(error => {
        console.log(error)
    })
  }
render(){
  return (
    <View  style={styles.container}>
      <Text style={styles.h1Text}>Calculador de IH</Text>
      <View style={styles.inputBox}>
      <TextInput style={styles.input} placeholder="Longitude" placeholderTextColor="black" onChangeText={(lat=>{this.setState({lat})})} ></TextInput>
      <TextInput style={styles.input} placeholder="Latitude" placeholderTextColor="black" onChangeText={(long=>{this.setState({long})})}></TextInput>
      
      </View>
      <TouchableOpacity onPress={this.nearest} style={styles.button}><Text style={styles.textButton}>Calcular</Text></TouchableOpacity>
      <Text style={styles.txtResult}>Resultado</Text>

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
