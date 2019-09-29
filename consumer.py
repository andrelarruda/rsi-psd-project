from kafka  import KafkaConsumer
from json   import loads
import paho.mqtt.client as paho 
import time

topicos = []
dados   = None

# Thingsboard log
def on_publish(client, userdata, result):
    print("data published to thingsboard \n")
    pass

# Paho Config const
ACCESS_TOKEN    = "p4Uj97oCe9JSHaGtLMRz"  
BROKER          = "localhost"
PORT            = 1883 

# Kafka Config const
CLIENT_NAME     = "control1"
SERVER          = "localhost:9092"
AUTO_OFFSET     = "earliest"
MY_GROUP        = "my-group"

client1 = paho.Client(CLIENT_NAME)  
client1.connect(BROKER, PORT, keepalive=60)
client1.username_pw_set(ACCESS_TOKEN)
client1.on_publish = on_publish 

# Consumer Config
consumer = KafkaConsumer(
     bootstrap_servers  = [SERVER],
     auto_offset_reset  = AUTO_OFFSET,
     enable_auto_commit = True,
     group_id           = MY_GROUP,
     value_deserializer = lambda v: v.decode('utf-8'))

consumer.subscribe(pattern="^.*timestamp.humidade.temperatura")

client1.loop_start()

for message in consumer:
    temp    = message.topic
    topicos = temp.split(".")
    dados   = message.value
    dados   = dados.split(" ")
    
    # Logs
#     print(topicos)
#     print(dados)
    
    # Thingsboard's messages
    payload = '{"ts":' + str(dados[0]) + ', "values": {"humidade":' + str(dados[1]) + ', "temperatura":' + str(dados[-1]) + '}}'
    print(payload)
    ret = client1.publish("v1/devices/me/telemetry", payload)  
    #print(ret)
    time.sleep(5)
client1.loop_stop()