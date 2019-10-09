from kafka  import KafkaConsumer
from json   import loads

import paho.mqtt.client as paho 
import time

#from __future__ import print_function

import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

topicos = []
dados   = None

# Spark Config
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("""
        Usage: consumer.py <bootstrap-servers> <subscribe-type> <topics>
        """, file=sys.stderr)
        sys.exit(-1)

    bootstrapServers = sys.argv[1]
    subscribeType = sys.argv[2]
    topics = sys.argv[3]

    spark = SparkSession\
        .builder\
        .appName("StructuredKafkaWordCount")\
        .getOrCreate()

    # Create DataSet representing the stream of input lines from kafka
    lines = spark\
        .readStream\
        .format("kafka")\
        .option("kafka.bootstrap.servers", bootstrapServers)\
        .option(subscribeType, topics)\
        .load()\
        .selectExpr("CAST(value AS STRING)")

    # Split the lines into words
    words = lines.select(
        # explode turns each item in an array into a separate row
        explode(
            split(lines.value, ' ')
        ).alias('word')
    )
# bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.3 /home/rsi-psd-vm/Documents/rsi-psd-project/consumer.py localhost:9092 subscribe A301.umidade.temperatura
'''
# Thingsboard log
def on_publish(client, userdata, result):
    print("data published to thingsboard \n")
    pass

# Paho Config const
ACCESS_TOKEN    = "kgWZAdFuWLc8DJRpjkfG"  
BROKER          = "localhost"
PORT            = 1883 

# Kafka Config const
CLIENT_NAME     = "control1"
SERVER          = "localhost:9092"
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

client1.loop_start()

for message in consumer:
    temp    = message.topic
    topicos = temp.split(".")
    dados   = message.value
    dados   = dados.split(" ")
    
    # Thingsboard's messages
    payload = '{"ts":' + str(dados[0]) + ', "values": {"humidade":' + str(dados[1]) + ', "temperatura":' + str(dados[-1]) + '}}'
    print(payload)
    ret = client1.publish("v1/devices/me/telemetry", payload)
    time.sleep(5)

client1.loop_stop()

'''