import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import sys


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client("claa00_03")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("admin", "public")  # 必须设置，否则会返回「Connected with result code 4」
client.connect(host="100.0.0.3", port=1883, keepalive=60)

while True:
    try:
        # 发布MQTT信息
        sensor_data = "测试数据"
        print("发送成功!")
        client.publish("dissun", "测试数据", qos=0,retain=False)
        time.sleep(5)
    except KeyboardInterrupt:
        print("EXIT")
        client.disconnect()
        sys.exit(0)
