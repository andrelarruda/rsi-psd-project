import pandas as pd
import os
import time

csv1_path = os.path.join(os.path.expanduser('~'), 'Documents', 'rsi-psd-project', 'data', 'A3.csv')
#dataframe = pd.read_csv("F:/sample.csv", usecols=['id', 'First Name', 'Last Name', 'Email', 'Desciption', 'Role', 'Boss ID', 'Phone'], sep=',')

#dataframe de empenhos
dataframe = pd.read_csv(csv1_path,
                        #Colunas que serão lidas
                        usecols=['timestamp', 'stationCode', 'stationName', 'latitude', 'longitude', 'umid_max',
                                    'umid_min', 'temp_max', 'pressao', 'pressao_min', 'pto_orvalho_inst',
                                    'pto_orvalho_max', 'radiacao', 'temp_min', 'pressao_max', 'pto_orvalho_min',
                                    'temp_inst', 'umid_inst', 'precipitacao'],
                        sep=',',
                        #Tipo das colunas
                        dtype={'timestamp': int, 'stationCode': str, 'stationName': str, 'latitude': float, 'longitude': float, 'umid_max': int,
                                    'umid-min': int, 'temp_max': float, 'pressao': float, 'pressao_min': float, 'pto_orvalho_inst': float,
                                    'pto_orvalho_max': float, 'radiacao': float, 'temp_min': float, 'pressao_max': float, 'pto_orvalho_min': float,
                                    'temp_inst': float, 'umid_inst': int, 'precipitacao': float})

for element in dataframe.values:
    print(element)
    time.sleep(1)


#    dataframe.to_sql('intermediaria_empenho', conn, if_exists='replace')