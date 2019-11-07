import requests
import time
import json
class Devices():
    def __init__(self):
        self._broker        = "localhost"
        self._port          = 1883
        self._tokens        = {'A301': "f4bCXGwj9Mk6cArVwJSc", 'A307': "ngC1wVtcAS6eRDxjmLjF", 
        'A309': "7W00vXj4nqYvzhrB1y3J", 'A322': "au7bVNpWPgho0jEEQSZ5", 'A328': "AWTccpmlqqvtsuDcC9ma", 
        'A329': "6VYmn1TgkIurtYwf6BTm", 'A341': "rZJ3TWbrt3iOgkThdRpA", 'A349': "yk64ImmTFJGCR5vNXdVH", 
        'A350': "TIcmOFfzFzCI70LHbmAj", 'A351': "UPGYIzI32XoEEJ3sZ0Pt", 'A357': "jxs9mO0ZUwzFMi1JXiLs", 
        'A366': "trVoVWjZVZDmvQmidTd9", 'A370': "oxI6WhQeVvQBmDR2YZa0"}
    
    def on_publish(self, client, userdata, result):
        print("data published to thingsboard \n")
        pass

    def publicar(self, payload):
        payload = json.loads(payload)
        token = self._tokens[payload["values"]["stationCode"]]
        url = "http://localhost:9090/api/v1/"+token+"/telemetry"
        retorno = requests.post(url, json.dumps(payload))
        print(retorno)