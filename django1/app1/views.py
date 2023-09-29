from django.shortcuts import render
# import pymongo

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required,permission_required

import datetime
import time
import json
import requests

#下载
from django.http import StreamingHttpResponse
import re
from .models import * #引用
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from utils import send_email, render_data

#默认入口设计：
@login_required(login_url = '/user/login.html')
def index(request):
    username = request.user.username
    print(username)
    return HttpResponseRedirect('/app1/test/')


@login_required(login_url = '/user/login.html')
def test(request):
    # 只要赋值给任意变量，即可直接以v-html语法写前端组件
    # xxx 自己的逻辑 
    load_data = {'a': 123, 'b': 12} # 将直接在前端渲染

    return render_data.flush_and_render(request, "test.html", locals())


@login_required(login_url = '/user/login.html')
def test_sub1(request):
    # 只要赋值给任意变量，即可直接以v-html语法写前端组件
    # xxx 自己的逻辑 
    load_data = {'data': 'in sub 1!'} # 将直接在前端渲染

    return render_data.flush_and_render(request, "test.html", locals())



    # ####################
    # # username = request.user.username
    # recv = request.GET.dict()
    # print(recv)
    # kind = recv["kind"]
    # ret = {}
    # ret['data'] = []
    # if kind =='check':
    #     # 查询签到记录
    #     username = recv['username']
    #     if username == 'admin':
    #         all_list = History.objects.filter().order_by('-temptime')
    #     else:
    #         all_list = History.objects.filter(dataid = username).order_by('-temptime')
    #     ret = {'data':[]}
    #     # if len(all_list)>0:
    #     # 所有账号下都要变
    #     ret['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     ret['status'] = 'ok'
    #     return JsonResponse(ret)


    # #修改信息，创建信息
    # elif kind=='change_device_info':
    #     username = recv['username']
    #     data = recv["data"]
    #     data = json.loads(data)
    #     print(data)
        # all_list2 = Info.objects.filter(name=productname,username=username) #本账号绑定的本设备
        # if len(all_list2)>0:
        #     temp_iter2 = all_list2[0]
        #     if data[1]:
        #         temp_iter2.alertmail = str(data[1]) #邮箱
        #     if data[2]:
        #         temp_iter2.data1set = float(data[2]) #阈值
        #     if data[3]:
        #         temp_iter2.secret = str(data[3]) #secret
        #     if data[4]:
        #         temp_iter2.comments = str(data[4])  # comments
        #     temp_iter2.save()

        # ret['status'] = 'ok'
        # return JsonResponse(ret)

    # elif kind == 'delete_product':  # 删除
    #     # try:
    #     username = recv['username']
    #     productname = recv['id']
    #     print(username)
    #     print(productname)
    #     Info.objects.filter(username=username,name = productname).all().delete()
    #     ret['status'] = "ok"
    #     # except:
    #     #     ret['status'] = 'fail'
    #     return JsonResponse(ret)

    # #获取曲线图历史数据
    # elif kind=='get_curve':
    #     #根据username获取绑定的设备号 --Info表
    #     username = recv['username']
    #     temp_id = ''
    #     all_list = Info.objects.filter(username=username)
    #     if len(all_list) > 0:
    #         temp_id = all_list[0].productname
    #     else:
    #         Info.objects.create(username=username)
    #     print("设备号")
    #     print(temp_id)
    #     if temp_id!='':
    #         temp_index = (int)(recv['temp_index'])
    #         print(temp_index)
    #         charts_len = (int)(recv['charts_len'])
    #         ret = {}
    #         all_find = History.objects.filter(name=temp_id).order_by('-temptime') #倒叙
    #         all_count = len(all_find) #所有项目数量
    #
    #         if all_count<charts_len:
    #             #创建并初始放置一组数据
    #             for ii in range(charts_len+1):
    #                 History.objects.create(name=temp_id)
    #             print("create")
    #
    #         count_f0 = 0 #从0开始
    #         for count in range(temp_index*charts_len,(temp_index+1)*charts_len):
    #             find_data = all_find[count]
    #
    #             ret[count_f0] = {}
    #             ret[count_f0]['data'] = [(float)("%.2f" % find_data.data1),(float)("%.2f" % find_data.data2),(float)("%.2f" % find_data.data3),(float)("%.2f" % find_data.data4),(float)("%.2f" % find_data.data5)] #几种数据
    #             ret[count_f0]['time'] = find_data.temptime.strftime("%Y-%m-%d %H:%M:%S")[2:]
    #             count_f0 +=1
    #         ret['all_count'] =  all_count
    #
    #     ret['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     return JsonResponse(ret)


#     # 下载数据
#     elif kind == 'download':
#         parkid = json.loads(recv['parkid'])
#         parkid = (int)(parkid)
#         print(parkid)
#         ret = {}
#         ret['data'] = []
#
#         all_list = Sharelog.objects.filter()
#
#         the_file_name = "temp.txt"
#         # .strftime("%Y-%m-%d %H:%M:%S")
#         file_handle = open(the_file_name, mode='w')
#         for ii in range(len(all_list)):
#             if all_list[ii].outtime!=None:
#                 temp_row = ([all_list[ii].addtime.strftime("%Y-%m-%d %H:%M:%S"),all_list[ii].outtime.strftime("%Y-%m-%d %H:%M:%S"),all_list[ii].client,all_list[ii].numid])
#             else:
#                 temp_row = (
#                 [all_list[ii].addtime.strftime("%Y-%m-%d %H:%M:%S"), "-to now-",
#                  all_list[ii].client, all_list[ii].numid])
#             file_handle.write(str(temp_row) + '\n')
#         file_handle.close()
#
#         response = StreamingHttpResponse(file_iterator(the_file_name))
#         response['Content-Type'] = 'application/octet-stream'
#         response['Access-Control-Expose-Headers'] = 'Content-Disposition'  # 允许跨域
#         response['Content-Disposition'] = 'attachment;filename="temp.txt"'
#         return response
#
#     return JsonResponse(ret)
#
# ##下载文件
# def file_iterator(file_name, chunk_size=512):
#     with open(file_name) as f:
#         while True:
#             c = f.read(chunk_size)
#             if c:
#                 yield c
#             else:
#                 break


# ===================
# esp32
# ===================


#####esp32
def esp32_up(request):
    recv = json.loads(request.body.decode())
    print(recv)
    ret = {}
    # name = recv['name']
    # data = recv['data']

    # all_list = Info.objects.filter() #所有账号的所有设备副本逐个遍历
    # # if len(all_list)>0:
    # for ii in range(len(all_list)):
    #     temp_iter = all_list[ii]

    return JsonResponse(ret)

#获取状态 -- no use
def esp32_down(request):
    recv = json.loads(request.body.decode())
    print(recv)
    ret = {}
    # name = recv['name']

    # all_list = Status.objects.filter(name=name)
    # if len(all_list)>0:
    #     ret['data'] = [all_list[0].data1alertstatus,all_list[0].data2alertstatus,all_list[0].data3alertstatus,all_list[0].data4alertstatus,all_list[0].data5alertstatus,all_list[0].ledstatus]

    return JsonResponse(ret)
