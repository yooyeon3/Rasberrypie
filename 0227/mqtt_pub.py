import random
import time
from paho.mqtt import client as mqtt_client
from paho.mqtt.client import CallbackAPIVersion

broker = 'broker.emqx.io'
port = 1883
topic = 'python/mqtt'
client_id = f'python.mqtt.{random.randint(0,1000)}'

def connect_mqtt():

    # 2.x 콜백 형식
    def on_connect(client, userdata, flags, reason_code, properties):
        if reason_code == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {reason_code}")

    client = mqtt_client.Client(
        client_id=client_id,
        callback_api_version=CallbackAPIVersion.VERSION2
    )

    client.on_connect = on_connect
    client.connect(broker, port)

    return client


def publish(client):
    msg_count = 1
    while msg_count <= 5:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        client.publish(topic, msg)
        print(f"Send '{msg}' to topic '{topic}'")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == '__main__':
    run()