#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
 Consumes messages from one or more topics in Kafka and does wordcount.
 Usage: structured_kafka_wordcount.py <bootstrap-servers> <subscribe-type> <topics>
   <bootstrap-servers> The Kafka "bootstrap.servers" configuration. A
   comma-separated list of host:port.
   <subscribe-type> There are three kinds of type, i.e. 'assign', 'subscribe',
   'subscribePattern'.
   |- <assign> Specific TopicPartitions to consume. Json string
   |  {"topicA":[0,1],"topicB":[2,4]}.
   |- <subscribe> The topic list to subscribe. A comma-separated list of
   |  topics.
   |- <subscribePattern> The pattern used to subscribe to topic(s).
   |  Java regex string.
   |- Only one of "assign, "subscribe" or "subscribePattern" options can be
   |  specified for Kafka source.
   <topics> Different value format depends on the value of 'subscribe-type'.

 Run the example
    `$ bin/spark-submit examples/src/main/python/sql/streaming/structured_kafka_wordcount.py \
    host1:port1,host2:port2 subscribe topic1,topic2`
    
    172.16.205.48

    bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.3 /home/rsi-psd-vm/Documents/rsi-psd-project/spark.py localhost:9092 subscribe A301.timestamp.umidade.temperatura,A307.timestamp.umidade.temperatura,A309.timestamp.umidade.temperatura,A322.timestamp.umidade.temperatura,A328.timestamp.umidade.temperatura,A329.timestamp.umidade.temperatura,A341.timestamp.umidade.temperatura,A349.timestamp.umidade.temperatura,A350.timestamp.umidade.temperatura,A351.timestamp.umidade.temperatura,A357.timestamp.umidade.temperatura,A366.timestamp.umidade.temperatura,A370.timestamp.umidade.temperatura
"""
from __future__ import print_function

import sys
import json

from identificador          import Devices
from pyspark.sql            import SparkSession
from pyspark.sql.functions  import explode
from pyspark.sql.functions  import split

def calcularHeatIndex(tc, rh):
    t = (1.8*tc) + 32 
    firstHeatIndex = (1.1*t) - 10.3 + (0.047*rh)

    if (firstHeatIndex < 80):
        result = firstHeatIndex
    else:
        firstHeatIndex = -42.379 + (2.04901523 * t) + (10.14333127 * rh) - (0.22475541 * t * rh) - (6.83783 * (10**-3) * (t**2)) - (5.481717 * (10**-2) * (rh**2)) + (1.22874 * (10**-3) * (t**2) * rh) + (8.5282 * (10**-4) * t * (rh**2)) - (1.99 * (10**-6) * (t**2) * (rh**2))
        if ( ((t >= 80) and (t <= 112)) and (rh<=13)):
            result = firstHeatIndex - (3.25 - (0.25 * rh)) * (( (17 - abs(t-95))/17) ** 0.5)
        elif ( ((t >= 80) and (t <= 87)) and (rh > 85)):
            result = firstHeatIndex + (0.02 * (rh - 85) * (87 - 5))
        else:
            result = firstHeatIndex

    return (result-32)/1.8

def processRow(row):
    global dev
    meu_json = eval(row["value"])
    values = meu_json["values"]
    temperatura = float(values["temperatura"])
    umidade = float(values["umidade"])
    heat_index = calcularHeatIndex(temperatura, umidade)
    meu_json["values"]["HI"] = heat_index
    print(json.dumps(meu_json))
    #dev.publicar(meu_json)
    
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("""
        Usage: structured_kafka_wordcount.py <bootstrap-servers> <subscribe-type> <topics>
        """, file=sys.stderr)
        sys.exit(-1)

    dev = Devices()
    bootstrapServers = sys.argv[1] #'172.16.205.131:9092'
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
        .option("startingOffsets", "latest")\
        .option(subscribeType, topics)\
        .load() \
        .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
    
    data = lines.select(lines.value)

    query = data\
        .writeStream\
        .outputMode('update')\
        .foreach(processRow)\
        .start()
    
    print(query)
    query.awaitTermination()