# python manage.py createsuperuser

from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from user.models import *

ADDITIONAL_FIELDS = (("其他信息", {'fields': ('datasex', 'datainfo')}),)

class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_FIELDS
    add_fieldsets = UserAdmin.fieldsets + ADDITIONAL_FIELDS

admin.site.register(MyUser, MyUserAdmin)

## 隐藏认证授权-只剩组了
from django.contrib.auth.models import Group #, User
admin.site.unregister(Group)

## 修改标题
admin.site.site_header = '后台管理系统'  # 设置header
admin.site.site_title = 'Admin'          # 设置title