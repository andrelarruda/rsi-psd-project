#!/usr/bin/env python
from kafka import KafkaProducer
import json
from time import sleep
from datetime import datetime
import pandas as pd
import os
import time
import variaveis

taxa = int(input("Digite a taxa de velocidade: "))

producer = KafkaProducer(bootstrap_servers='localhost:9092', 
value_serializer=lambda v: str(v).encode('utf-8'))

arquivos = ["A301.csv", "A307.csv", "A309.csv", "A322.csv", "A328.csv", "A329.csv", "A341.csv", "A349.csv", "A350.csv", 
"A351.csv", "A357.csv", "A366.csv", "A370.csv"]

csv1_path = variaveis.csv1_path

for file in arquivos:
    #dataframe = pd.read_csv("F:/sample.csv", usecols=['id', 'First Name', 'Last Name', 'Email', 'Desciption', 'Role', 'Boss ID', 'Phone'], sep=',')

    #dataframe de empenhos
    dataframe = pd.read_csv(csv1_path + os.sep + file,
                            #Colunas que serão lidas
                            usecols=['timestamp', 'stationCode', 'stationName', 'latitude', 'longitude', 'umid_max',
                                        'umid_min', 'temp_max', 'pressao', 'pressao_min', 'pto_orvalho_inst',
                                        'pto_orvalho_max', 'radiacao', 'temp_min', 'pressao_max', 'pto_orvalho_min',
                                        'temp_inst', 'umid_inst', 'precipitacao'],
                            sep=',',
                            #Tipo das colunas
                            dtype={'timestamp': str, 'stationCode': str, 'stationName': str, 'latitude': float, 'longitude': float, 'umid_max': float,
                                        'umid-min': float, 'temp_max': float, 'pressao': float, 'pressao_min': float, 'pto_orvalho_inst': float,
                                        'pto_orvalho_max': float, 'radiacao': float, 'temp_min': float, 'pressao_max': float, 'pto_orvalho_min': float,
                                        'temp_inst': float, 'umid_inst': float, 'precipitacao': float})

    for element in dataframe.values:
        mensagem = element[0] + " " + str(element[17]) + " " + str(element[16])
        print(mensagem)
        producer.send(element[1] +".timestamp.humidade.temperatura", mensagem )
        time.sleep(1 / taxa)


#    dataframe.to_sql('intermediaria_empenho', conn, if_exists='replace')