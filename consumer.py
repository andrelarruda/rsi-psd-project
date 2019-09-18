from kafka import KafkaConsumer
from json import loads

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