from kafka  import KafkaConsumer
from json   import loads

import paho.mqtt.client as paho 
import time
from identificador import Devices

topicos = []
dados   = None

# Thingsboard log
def on_publish(client, userdata, result):
    print("data published to thingsboard \n")
    pass

# Paho Config const
CLIENT_NAME     = "control1"
ACCESS_TOKEN    = "kgWZAdFuWLc8DJRpjkfG"  
BROKER          = "localhost"
PORT            = 1883 

# Kafka Config const

SERVER          = "172.16.205.131:9092"
AUTO_OFFSET     = "latest"
MY_GROUP        = "my-group"

client1 = paho.Client(CLIENT_NAME)  
client1.connect(BROKER, PORT, keepalive=60)
client1.username_pw_set(ACCESS_TOKEN)
client1.on_publish = on_publish 

# Consumer Config
consumer = KafkaConsumer(
     bootstrap_servers  = [SERVER]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ,
     auto_offset_reset  = AUTO_OFFSET,
     enable_auto_commit = True,
     group_id           = MY_GROUP,
     value_deserializer = lambda v: v.decode('utf-8'))

consumer.subscribe(pattern="^.*timestamp.umidade.temperatura")

dev = Devices()

while True:
    for message in consumer:
        temp    = message.topic
        topicos = temp.split(".")
        dados   = message.value
        dados   = dados.split(" ")
        print(message)
        
        # Thingsboard's messages
        payload = '{"ts":' + str(dados[0]) + ', "values": {"umidade":' + str(dados[1]) + ', "temperatura":' + str(dados[-1]) + '}}'
        print(payload)
        dev.publicar(topicos, message)#payload)
        


