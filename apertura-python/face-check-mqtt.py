# python 3.6
import random
import time
import pandas as pd

from paho.mqtt import client as mqtt_client
from deepface import DeepFace

# broker = '3.122.69.139'
broker = '127.0.0.1'
port= 1883
topic='codigoIoT/mqtt/python'
topic2='codigoIoT/mqtt/index'
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client




def publish(client,mensaje):
    #while True:
    time.sleep(1)
    msg = mensaje
    result = client.publish(topic, msg)
    time.sleep(1)
    # result2 = client.publish(topic2, indice)
    # time.sleep(1)
    print (result)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

print("Buscando rostro...")

df = DeepFace.find(img_path="/home/dafne/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/faces/persona3.png", db_path="/home/dafne/Documents/GitHub/apertura-puertas-reconocimiento-facial/deepface/mydb", enforce_detection="false")

print("Resultado...")
print(df)
json_view= df.to_json(orient="index")
print("La expresion en JSON de los resultados es: ...")
# (df.identity[0])
print(json_view)


def run():
    client = connect_mqtt()
    client.loop_start()
    #publish(client)
    #publish2(client,df.identity[0])
    publish(client,json_view)

if __name__ == '__main__':
    run()
