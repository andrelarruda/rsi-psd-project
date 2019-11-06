from kafka  import KafkaConsumer
from json   import loads

import time
import sys
from identificador import Devices

# Thingsboard log
def on_publish(client, userdata, result):
    print("data published to thingsboard \n")
    pass

# Kafka Config const
SERVER          = "172.16.205.131:9092"
AUTO_OFFSET     = "latest"
MY_GROUP        = "my-group"

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
        #print(message.value)
        dev.publicar(message.value)

