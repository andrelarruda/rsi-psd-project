#!/usr/bin/env python
from kafka import KafkaProducer
import json
from time import sleep
import pandas as pd
import os
import time
import variaveis

def inputInit(exit, speedupFactor):
    delta = 0
    
    if exit:
        return speedupFactor
    else:
        try:
            speedupFactor = int(input("Digite o fator de aceleração: "))
            #speedupFactor = 720 #Para fins de teste, este valor será fixo.
            delta = 3600/speedupFactor #delta = interval/speedup factor
            exit = True
            return inputInit(exit, delta)
            
        except ZeroDivisionError:
            print("Zero Division error!")
            return(inputInit(False, delta))
        except ValueError:
            print("Invalid input format!")
            return(inputInit(False, delta))
        
# Main Program
speedupFactor       = inputInit(False, 0)    
producer            = KafkaProducer(bootstrap_servers='localhost:9092', 
value_serializer    = lambda v: str(v).encode('utf-8'))

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
        "ts": str(element[0]),
        "values": {
        "umidade": str(element[17]),
        "temperatura": str(element[16]),
        "stationCode": str(element[1]),
        "stationName": str(element[2]),
        "latitude": str(element[3]),
        "longitude": str(element[4])
        }
    }
    mensagem = json.dumps(formatJson)
    producer.send(element[1] +".timestamp.umidade.temperatura", mensagem )
    print("Sent: " + (mensagem))
    time.sleep(speedupFactor)