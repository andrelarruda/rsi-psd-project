from kafka  import KafkaConsumer
from json   import loads

import paho.mqtt.client as paho 
import time
from identificador import Devices

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


