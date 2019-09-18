from kafka import KafkaConsumer
from json import loads
import faust
import paho.mqtt.client as paho 
import time

# Faust
class Total(faust.Record):
     total: str

app = faust.App('myapp', broker='kafka://localhost:9092')
click_topic = app.topic(key_type=str, value_type=Total)
@app.agent(click_topic)
async def hello(totals):
    async for line in totals:
        print(f'Hello from {line.total}')

if __name__ == '__main__':
    app.main()
'''
#Paho
ACCESS_TOKEN = 'RJJLwCPZxdn7yuon6FhA'  
broker = "localhost" 
port = 1883 

def on_publish(client, userdata, result):
    print("data published to thingsboard \n")
    pass

client1 = paho.Client("control1")  
client1.connect(broker, port, keepalive=60)
client1.username_pw_set(ACCESS_TOKEN)
client1.on_publish = on_publish 
client1.loop_start() 

lista= [1000, 2000, 3000, 4000]

for i in range(len(lista)): 
    payload = '{"temperature":' + str(lista[i]) + ', "humidity":5000, "teste": Gabriel}'
    ret = client1.publish("v1/devices/me/telemetry", payload)  
    print("Please check LATEST TELEMETRY field of your device")
    print(ret)
    print(payload)
    time.sleep(5)

client1.loop_stop()
'''
'''
consumer = KafkaConsumer(
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda v: str(v).encode('utf-8'))

consumer.subscribe(pattern=".+")

for message in consumer:
    print(message.topic)
    message = message.value
    print('received: ' + str(message))

'''