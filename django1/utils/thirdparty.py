import datetime
import os
import time
import json
import base64
import requests

from smtplib import SMTP, SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
def send_email(receivers,alert_context, send_email = "", api_key = ""):
    if send_email == "" and api_key == "":
        from app1.models import TextKeyVal
        send_email_api = TextKeyVal.objects.filter(keyname="email_api")
        if send_email_api: 
            send_email, api_key = send_email_api[0].value.split(",")
    # 请自行修改下面的邮件发送者和接收者
    sender = send_email  # 发送者的邮箱地址
    # receivers = [receiver]  # 接收者的邮箱地址
    message = MIMEText('Alert:'+str(alert_context), _subtype='plain', _charset='utf-8')
    message['From'] = sender #Header(sender, 'utf-8')  # 邮件的发送者
    message['To'] = Header('Hello', 'utf-8')  # 邮件的接收者
    message['Subject'] = Header(alert_context, 'utf-8')  # 邮件的标题
    # smtper = SMTP('smtp.qq.com',465)
    smtper = SMTP_SSL("smtp.qq.com", 465)
    # 请自行修改下面的登录口令
    smtper.login(sender, api_key)  # QQ邮箱smtp的授权码
    smtper.sendmail(sender, receivers, message.as_string())
    #print('邮件发送完成!')

#########################
# onenet
#cmd
def send_onenet_cmd(device_id, api_key, key_name = "data0", action = "t_off", period = 1):
    url = "http://api.heclouds.com/cmds?device_id=" + device_id
    headers={'api-key': api_key}
    downdata = {
        "key_name": key_name,
        "action": action,
        "period": period
    }
    res = requests.post(url, headers=headers, data=json.dumps(downdata))
    cnt = 0
    while json.loads(res.text).get('errno', 0) != 0 and cnt < 3:
        print("error: {}, resent waiting...".format(json.loads(res.text)))
        time.sleep(3)
        res = requests.post(url, headers=headers, data=json.dumps(downdata))
        cnt += 1

#status
def check_status(device_id, headers):
    url = "http://api.heclouds.com/devices/" + device_id
    res = requests.get(url, headers=headers)
    name = res.json()['data']['auth_info']
    online_status = res.json()['data']['online']
    last_time = res.json()['data']['last_ct']
    return res.json()['data']

def check_latest_datapoints(device_id, headers):
    #datapoints
    url="http://api.heclouds.com/devices/{}/datapoints".format(device_id)
    r=requests.get(url,headers=headers)
    latest_val = r.json()['data']['datastreams'][0]['datapoints'][0]['value']
    last_time = r.json()['data']['datastreams'][0]['datapoints'][0]['at']
    return r.json()['data']['datastreams'][0]['datapoints']

def check_datastream(device_id, headers, stream_id, limit = 1):
    url="http://api.heclouds.com/devices/{}/datapoints?datastream_id={}&limit={}".format(device_id, stream_id, limit)
    r=requests.get(url,headers=headers)
    # print(r.json()['data']['datastreams'][0]['datapoints'])
    return r.json()['data']['datastreams'][0]['datapoints']

# dis
from math import sin, asin, cos, radians, fabs, sqrt
def hav(theta):
    s = sin(theta / 2)
    return s * s
def get_distance_hav(lat0, lng0, lat1, lng1):
    """用haversine公式计算球面两点间的距离。"""
    EARTH_RADIUS = 6371  # 地球平均半径，6371km
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)
    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))
    return distance 
# print(get_distance_hav(30.28708, 120.12802999999997, 28.7427, 115.86572000000001))
#########################




def onenet_check(request):
    #浏览器来访
    # print("html")
    # print(request.GET.dict())
    recv = request.GET.dict()
    # print(recv)
    limit_num = recv["limit_num"]
    id = recv["id"]
    password = recv["password"]
    url = "http://api.heclouds.com/devices/"+str(id)+"/datapoints"
    headers = { "api-key":password}
    data={'limit':limit_num}
    receive = requests.get(url,headers = headers,params = data).text
    data = (json.loads(receive))['data']
    # print(data)
    return data


#写入
def onenet_write(request):
    #浏览器来访
    # print("html")
    # print(request.GET.dict())
    recv = request.GET.dict()
    # print(recv)
    id = recv["id"]
    password = recv["password"]
    
    data_name = recv['data_name']     #js端要用JSON.stringify([val]) 代替直接字典映射数组[val]
    data_name = json.loads(data_name)
    data_value = recv['data_value']
    data_value = json.loads(data_value)
    
    print(data_name)
    print(data_value)
    
    url = "http://api.heclouds.com/devices/"+str(id)+"/datapoints"
    headers = { "api-key":password}
    temp_list = []
    for ii in range(len(data_name)):
        temp_list.append({'id':data_name[ii],'datapoints':[{'value':data_value[ii]}]} )
        
    data = {'datastreams':temp_list}
    requests.post(url, headers=headers, data=json.dumps(data))

    return True
        