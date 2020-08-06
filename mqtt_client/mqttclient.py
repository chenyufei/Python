#!/usr/bin/env python
# coding=utf-8

import json
import sys
import os
import paho.mqtt.client as mqtt
import time

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")

TASK_TOPIC = 'test'  # 客户端发布消息主题

client_id = time.strftime('claa_%Y%m%d%H%M%S', time.localtime(time.time()))

client = mqtt.Client(client_id, transport='tcp')
client.username_pw_set("admin", "public")  # 必须设置，否则会返回「Connected with result code 4」
client.connect("100.0.0.3", 1883, 60)  # 此处端口默认为1883，通信端口期keepalive默认60
client.loop_start()


def clicent_main(message: str):
    """
    客户端发布消息
    :param message: 消息主体
    :return:
    """
    time_now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    payload = {"msg": "%s" % message, "data": "%s" % time_now}
    # publish(主题：Topic; 消息内容)
    client.publish(TASK_TOPIC, json.dumps(payload, ensure_ascii=False))
    print("Successful send message!")
    return True


if __name__ == '__main__':
    msg = "我是一条测试数据！"
    clicent_main(msg)