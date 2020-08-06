import paho.mqtt.client as mqtt
import time

HOST = "100.0.0.3"
PORT = 1883
# git clone https://github.com/eclipse/paho.mqtt.python
# cd paho.mqtt.python
# python setup.py install


def client_loop():
    client_id = time.strftime('claa%Y%m%d%H%M%S',time.localtime(time.time()))
    client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
    client.username_pw_set("admin", "public")  # 必须设置，否则会返回「Connected with result code 4」
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("dissun")


def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode("utf-8"))


if __name__ == '__main__':
    client_loop()
