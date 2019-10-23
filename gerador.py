#!/usr/bin/env python
from kafka import KafkaProducer
import json
from time import sleep
from datetime import datetime
import pandas as pd
import os
import time
import variaveis

# speedupFactor = int(input("Digite o fator de aceleração: "))
speedupFactor = 3600 #Para fins de teste, este valor será fixo.
delta = 3600/speedupFactor #delta = interval/speedup factor

producer = KafkaProducer(bootstrap_servers='localhost:9092', 
value_serializer=lambda v: str(v).encode('utf-8'))

arquivos = ["A301.csv", "A307.csv", "A309.csv", "A322.csv", "A328.csv", "A329.csv", "A341.csv", "A349.csv", "A350.csv", 
"A351.csv", "A357.csv", "A366.csv", "A370.csv"]

csv1_path = variaveis.csv1_path
dataframe = []

for file in arquivos:
    
    dataframe.append(pd.read_csv(csv1_path + os.sep + file,
                            
                            usecols=['timestamp', 'stationCode', 'stationName', 'latitude', 'longitude', 'umid_max',
                                        'umid_min', 'temp_max', 'pressao', 'pressao_min', 'pto_orvalho_inst',
                                        'pto_orvalho_max', 'radiacao', 'temp_min', 'pressao_max', 'pto_orvalho_min',
                                        'temp_inst', 'umid_inst', 'precipitacao'],
                            sep=',',
                            dtype={'timestamp': int, 'stationCode': str, 'stationName': str, 'latitude': float, 'longitude': float, 'umid_max': float,
                                        'umid-min': float, 'temp_max': float, 'pressao': float, 'pressao_min': float, 'pto_orvalho_inst': float,
                                        'pto_orvalho_max': float, 'radiacao': float, 'temp_min': float, 'pressao_max': float, 'pto_orvalho_min': float,
                                        'temp_inst': float, 'umid_inst': float, 'precipitacao': float}))
big_frame = pd.concat(dataframe, ignore_index=True, sort=False )
big_frame = big_frame.sort_values('timestamp')

for element in big_frame.values:
    formatJson = {
        "timestamp": str(element[0]),
        "umidade": str(element[17]),
        "temperatura": str(element[16])
    }
    mensagem = json.dumps(formatJson)
    #mensagem = str(element[0]) + " " + str(element[17]) + " " + str(element[16])
    print(mensagem)
    producer.send(element[1] +".timestamp.umidade.temperatura", mensagem )
    time.sleep(delta)