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
import os
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from utils import render_data
from django.conf import settings

def mdrender(request):
    file_path = os.path.join("conf/", request.path.strip("/"))
    title = settings.PATH_NAME_CACHE.get(request.path.rstrip("/"), request.path.rstrip("/"))
    if os.path.isfile(file_path):
        load_data = open(file_path, 'r', encoding='utf-8').read()
        return render_data.flush_and_render(request, "md2html.html", locals())
    return render(request, "404.html")
