# import sys
# sys.path.append('/var/www/django1_nginx/app1')

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import os
import json
import time
import requests

from utils import onenet
########针对js前端的onenet接口

def onenet_check(request):
    data = onenet.onenet_check(request)
    # print(data)
    return JsonResponse(data) #返回数据
    
#写入
def onenet_write(request):
    if onenet.onenet_write(request):
        return HttpResponse("ok")
    else:
        return HttpResponse("fail")