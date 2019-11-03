import paho.mqtt.client as mqtt
import time
import json
class Devices():
    def __init__(self):
        self._broker        = "localhost"
        self._port          = 1883
        self._clients       = []
        self._tokens        = {'A301': "f4bCXGwj9Mk6cArVwJSc", 'A307': "ngC1wVtcAS6eRDxjmLjF", 
        'A309': "7W00vXj4nqYvzhrB1y3J", 'A322': "au7bVNpWPgho0jEEQSZ5", 'A328': "AWTccpmlqqvtsuDcC9ma", 
        'A329': "6VYmn1TgkIurtYwf6BTm", 'A341': "rZJ3TWbrt3iOgkThdRpA", 'A349': "yk64ImmTFJGCR5vNXdVH", 
        'A350': "TIcmOFfzFzCI70LHbmAj", 'A351': "UPGYIzI32XoEEJ3sZ0Pt", 'A357': "jxs9mO0ZUwzFMi1JXiLs", 
        'A366': "trVoVWjZVZDmvQmidTd9", 'A370': "oxI6WhQeVvQBmDR2YZa0"}
        
        self.connect()
    
    def on_publish(self, client, userdata, result):
        print("data published to thingsboard \n")
        pass

    def publicar(self, payload):
        thingsboard = "v1/devices/me/telemetry"
        code = json.loads(payload)
        
        for client in self._clients:
            current_client = str(client._client_id, "UTF8")
            if current_client == code["values"]["stationCode"]:
                #client.loop_start()
                ret = client.publish(thingsboard, str(payload), retain= True)
                print(ret)
                break
        
    def connect(self):

        for i  in self._tokens.keys():
            cname= str(i)
            client= mqtt.Client(cname)
            client.connect(self._broker,self._port, keepalive=60)
            client.on_publish = self.on_publish
            client.username_pw_set(self._tokens[i])
            client.loop_start()
            self._clients.append(client)