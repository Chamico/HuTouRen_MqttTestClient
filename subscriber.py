import paho.mqtt.client as mqtt

# MQTT代理地址
broker_address = "mqtt.example.com"
# 端口号，默认为1883
port = 1883
# 订阅的主题
topic = "test/topic"

# 创建一个MQTT客户端实例
client = mqtt.Client("Python_MQTT_Client")

# 定义当连接建立时的回调函数
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    # 订阅主题
    client.subscribe(topic)

# 定义当收到消息时的回调函数
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

# 设置回调函数
client.on_connect = on_connect
client.on_message = on_message

# 连接到MQTT代理
client.connect(broker_address, port=port)

# 启动客户端的网络循环，这样它才能持续运行并处理连接、消息等事件
client.loop_forever()
