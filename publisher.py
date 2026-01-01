import paho.mqtt.client as mqtt

# MQTT服务器地址
broker_address = "broker.hivemq.com"
# 设置回调函数

def on_publish(client, userdata, result):  # 当消息被发送出去后，会调用这个函数
    print("消息发布成功")

# 创建MQTT客户端实例
client = mqtt.Client("Python-MQTT-Publisher")

# 设置回调函数

# 连接到MQTT服务器
client.connect(broker_address, port=1883)  # 默认端口是1883，除非你更改了服务器的端口配置

# 定义要发布的主题和消息内容
topic = "test/topic"
message = "Hello MQTT!"

# 发布消息到MQTT服务器
client.publish(topic, message)

# 断开连接
client.disconnect()
