import paho.mqtt.client as mqtt
import json

with open('config.json', 'r') as f:
    config = json.load(f)

broker_address = config['broker']['host']
broker_port = config['broker']['port']
broker_user = config['broker']['user']
broker_password = config['broker']['password']
broker_topic = config['broker']['topic']

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(broker_topic)

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client(client_id="subscriber")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(broker_user,broker_password)
client.connect(broker_address)
client.loop_start()

try:
    while True:
        pass
except KeyboardInterrupt:
        print("Shutting down...")
finally:
    client.disconnect()
    client.loop_stop()
