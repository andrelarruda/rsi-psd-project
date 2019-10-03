import paho.mqtt.client as mqtt
class Devices():
    def __init__(self):
        self._broker = "localhost"
        self._port   = 1883
        self._tokens = {A301: "f4bCXGwj9Mk6cArVwJSc", A307: "ngC1wVtcAS6eRDxjmLjF"}



def publicador(topico, dados):
    cidades = ["A301", "A307", "A309", "A322", "A328", "A329", "A341", "A349", "A350", 
    "A351", "A357", "A366", "A370"]
    clients = []
    mqtt.Client.connected_flag = False
    
    #create clients
    for i  in cidades:
    cname="Client_"+str(i)
    client= mqtt.Client(cname)
    clients.append(client)
    for client in clients:
    client.connect(broker)
    client.loop_start()