# apt install sshpass
# crontab -e
# */5 * * * * python3 /root/syncproj1/dnsdbsync.py > /root/syncproj1_update.log 2>&1

import requests
import os, json
import datetime
# import time

from smtplib import SMTP, SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#######################################################################
local_id = "machine1" #机器标识

port_passwd_config = {
    "example": [22, "yourpasswd"],
    "default": [22, "yourpasswd"],
}
cf_dict = {}
remote_name_noproxy = ""

file_path = "/root/syncproj1/django1"
local_file_path = file_path

# cloudfare-settings
IP_API = 'https://api.ipify.org?format=json'
# Get CF API Key: https://support.cloudflare.com/hc/en-us/articles/200167836-Where-do-I-find-my-Cloudflare-API-key-
CF_API_KEY = 'fc7xxxxxxxxxxxxxxxxxxxxxxxxxx'
# Your cloudflare email address
CF_EMAIL = 'ywzsunny2012@163.com'
# Your zone id is located on the main cloudflare domain dashboard
ZONE_ID = 'bxxxxxxxxxxxxxxxxxxxxxx'
# Run script once without this set and it'll retrive a list of records for you to find the ID to update here
RECORD_ID = 'e1cxxxxxxxxxxxxxxxxxx' # ''
RECORD_NAME = "xxx.xxxx.top" # record-id path - notice: proxy ip

email_api = ['978020607@qq.com', 'xxxxxxx']
#######################################################################

def get_local_ipv6():
    info = os.popen('ifconfig').read()
    ipv6_addr = None
    for row in info.split("\n"):
        if 'inet6 2' in row:
            ipv6_addr = '2' + info.split('inet6 2')[1].split(' ')[0].strip()
            break
    return ipv6_addr

def stat_info_to_datestamp(temp_time):
    # 'Modify: 2023-09-28 14:19:30.154385776 +0800\n'
    temp_time = temp_time.split(": ")[-1].strip("\n").split(" ")
    temp_time[1] = temp_time[1].split(".")[0]
    temp_time = " ".join(temp_time)
    return datetime.datetime.strptime(temp_time, "%Y-%m-%d %H:%M:%S %z")

def update_cf_dns(ipaddr, RECORD_NAME):
    resp = requests.put(
        'https://api.cloudflare.com/client/v4/zones/{}/dns_records/{}'.format(
            ZONE_ID, RECORD_ID),
        json={
            'type': 'AAAA' if ":" in ipaddr else 'A',
            'name': RECORD_NAME,
            'content': ipaddr,
            'proxied': True
        },
        headers={
            'X-Auth-Key': CF_API_KEY,
            'X-Auth-Email': CF_EMAIL
        })
    # print(resp.status_code)
    return resp.status_code == 200

def get_cf_dns(RECORD_ID=""):
    global remote_name_noproxy
    resp = requests.get(
        'https://api.cloudflare.com/client/v4/zones/{}/dns_records/{}'.format(
            ZONE_ID, RECORD_ID),
        headers={
            'X-Auth-Key': CF_API_KEY,
            'X-Auth-Email': CF_EMAIL
        })
    for item in resp.json()['result']:
        if item['type'] == 'AAAA':
            cf_dict[item['name']] = item["content"]
    # cf_dict[RECORD_NAME] = cf_dict[?]
    for key in cf_dict:
        if key != RECORD_NAME and cf_dict[key] == cf_dict[RECORD_NAME]:
            remote_name_noproxy = key

# 可带附件的邮件发送函数
def send(receiver,alert_context, tfile=''):
    # 请自行修改下面的邮件发送者和接收者
    sender = email_api[0]  # 发送者的邮箱地址
    receivers = [receiver]  # 接收者的邮箱地址
    if tfile:
        message = MIMEMultipart()
    else:
        message = MIMEText('Alert:'+str(alert_context), _subtype='plain', _charset='utf-8')
    message['From'] = sender #Header(sender, 'utf-8')  # 邮件的发送者
    message['To'] = Header('Hello', 'utf-8')  # 邮件的接收者
    message['Subject'] = Header(alert_context, 'utf-8')  # 邮件的标题

    if tfile:
        txtfile = MIMEApplication(open(tfile, 'rb').read())
        txtfile.add_header('Content-Disposition','attachment',filename=tfile.split("/")[-1])
        message.attach(txtfile)

    # smtper = SMTP('smtp.qq.com',465)
    smtper = SMTP_SSL("smtp.qq.com", 465)
    # 请自行修改下面的登录口令
    smtper.login(sender, email_api[1])  # QQ邮箱smtp的授权码
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')
#######################################################################

def deal_main():
    get_cf_dns() #更新remote_name_noproxy
    local_ip = get_local_ipv6()
    if remote_name_noproxy == "":
        is_connected = False
    else:
        res = os.popen('ping {} -c 3'.format(remote_name_noproxy)).read()
        is_connected = bool(float(res.split("% packet loss")[0].split(", ")[-1].strip()) < 50)
        is_self = bool(remote_name_noproxy == local_ip)

        port = port_passwd_config.get(remote_name_noproxy, port_passwd_config["default"])[0]
        passwd = port_passwd_config.get(remote_name_noproxy, port_passwd_config["default"])[1]
        # print("remote ip: {}:{}".format(remote_name_noproxy, port))

    # 判断是否需要更新dns
    if not is_connected:
        status = update_cf_dns(local_ip, RECORD_NAME)
        print("update dns:", status)
        # email
        send(email_api[0], "update-dns-{}".format(local_id))

    # 判断是否更新db
    elif not is_self:
        temp_time = os.popen('sshpass -p "{}"  ssh -o StrictHostKeyChecking=no root@{} -p {} stat {} | grep "Modify"'.format(
            passwd, remote_name_noproxy, port, file_path
        )).read()
        file_date = stat_info_to_datestamp(temp_time)
        temp_time = os.popen('stat {} | grep "Modify"'.format(
            local_file_path
        )).read()
        local_file_date = stat_info_to_datestamp(temp_time)
        if file_date > local_file_date + datetime.timedelta(seconds=1):
            # 拉取更新
            os.system('sshpass -p "{}" scp -P {} -r root@{}:{} {}'.format(
                passwd, int(port), remote_name_noproxy, file_path, local_file_path
            ))
            print("update file")

if __name__ == "__main__":
    try:
        deal_main()
    except Exception as e:
        print("error: {}".format(e))
    # import time
    # while 1:
    #     deal_main()
    #     print("once")
    #     time.sleep(1 * 60)
