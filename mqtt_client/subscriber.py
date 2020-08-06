import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # 在这里处理业务逻辑
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client("claa_01")
client.username_pw_set("admin", password="public")
client.on_connect = on_connect
client.on_message = on_message
client.connect(host="100.0.0.3", port=1883, keepalive=60)  # 订阅频道
client.subscribe("paho/temperature")
client.loop_forever()
