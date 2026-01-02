import paho.mqtt.client as mqtt
import json
import time

with open('config.json', 'r') as f:
    config = json.load(f)

broker_address = config['broker']['host']
broker_port = config['broker']['port']
broker_user = config['broker']['user']
broker_password = config['broker']['password']
broker_topic = config['broker']['topic']

client = mqtt.Client(client_id="publisher")

def on_publish(client, userdata, result):  # 当消息被发送出去后，会调用这个函数
    print("消息发布成功")

def init_publisher_client():
    client.on_publish = on_publish
    client.username_pw_set(broker_user,broker_password)
    ret = client.connect(broker_address)

    if 0 == ret:
        print("publisher connect success")
        return True
    else:
        print("publisher connect failed " + ret)
        return False

def send_message():
    for index in range(0,9):
        message = "Hello MQTT!" + str(index)
        client.publish(broker_topic, message)
        time.sleep(2)

def end_publisher_client():
    client.disconnect()
    print("publisher finish, disconnect")

if init_publisher_client():
    send_message()
    end_publisher_client()
else:
    print("publisher fail")
