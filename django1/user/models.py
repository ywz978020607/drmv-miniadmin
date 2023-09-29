from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    datasex = models.CharField("性别", max_length=3, default="")
    datainfo = models.CharField("补充信息", max_length=3, default="")
    # dataname = models.CharField("姓名", max_length=3, default="")

    # And other fields you want...
    class Meta:
        verbose_name_plural = "用户信息"