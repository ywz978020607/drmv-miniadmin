# #mqtt_sub2db.py--监控订阅收信息并存到数据库中
# # cmd: > python mqtt_sub2db.py
# ################################################
#如果外部使用此脚本 则需添加此部分 且文件要从manage.py 同级的位置执行
import sys
sys.path.extend(['/src/django1', '/root/docker_nginx_with_manage/django1', '..'])
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django1.settings')
django.setup()
# ################################################
from app1.models import * #引用
# from app1.openapi import send_email #, send_onenet_cmd, get_distance_hav
import _thread
# location
# from app1.models import *
# TextKeyVal.objects.create(keyname="xxxgps_idxxx", value=json.dumps({"name": "xx车","target":[lat,lon], "cmd_id":"xxx", "api_key":"xxx", "dis": 1000}))

import paho.mqtt.client as mqtt #pip install paho-mqtt
import struct
import json
import requests
import datetime
import time


DEV_ID = "110646"
PRO_ID = "6070" #"234533" #产品ID--user
AUTH_INFO = "7KoVc" #"2kJV="  #APIKEY
TOPIC = [("/1106433873/cardid",0), ] #onenet:整个产品下所有设备共享

on_message_come_list = []
# 连接MQTT服务器
def on_mqtt_connect(mqttClient):
    mqttClient.username_pw_set(username=PRO_ID, password=AUTH_INFO)
    mqttClient.connect('183.230.40.39', port=6002, keepalive=10) #onenet
    mqttClient.loop_start()
# publish 消息
def on_publish(mqttClient,topic, payload, qos):
    mqttClient.publish(topic, payload, qos)
# 消息处理函数
def on_message_come(client, userdata, msg):
    on_message_come_list.append([client, userdata, msg])

def one_thread_deal_message_come():
    global on_message_come_list
    while 1:
        if len(on_message_come_list) > 0:
            client, userdata, msg = on_message_come_list.pop(0)
            recv = json.loads(msg.payload)
            print(recv, datetime.datetime.now())
            #########################################################
            ds_id = msg.topic.split("/")[1]
            value_name = msg.topic.split("/")[2]
            print(value_name)
            if value_name == "cardid":
                History.objects.create(dataid = recv['value'], productid = ds_id)
                print("create History")

# subscribe 消息
def on_subscribe(mqttClient):
    mqttClient.subscribe(TOPIC, 1) #topic是整个产品都通用，cmd/$dp是根据设备绑定, 订阅多个主题: TOPIC=[("them/running/121", 0), ("them/command/121", 2)]
    mqttClient.on_message = on_message_come # 消息到来处理函数

def main():
    client = mqtt.Client(client_id=DEV_ID, protocol=mqtt.MQTTv311)

    on_mqtt_connect(client)
    # on_publish(client,TOPIC, "p", 1)
    on_subscribe(client)
    start_run_time = datetime.datetime.now()
    print("ready.", str(start_run_time))
    while True:
        #如果需要下发可以在此处检测如下发表文件/db.sqlite3中的下发需求查删进行处理，注意topic与上传区分，如下文down_cmd2()函数
        result = client.publish("ping", "p")
        if result[0] != 0:
            print("publish fail",str(result))
            break
        # print("ping",result)
        time.sleep(20)
        if datetime.datetime.now() > start_run_time + datetime.timedelta(hours = 6):
        # if datetime.datetime.now() > start_run_time + datetime.timedelta(minutes = 1):
            client.disconnect()
            print("up to 6 hours")
            break

if __name__ == '__main__':
    _thread.start_new_thread(one_thread_deal_message_come,())
    while 1:
        # try:
        main()
        # except:
        #     print("error in main loop")
        time.sleep(15)
