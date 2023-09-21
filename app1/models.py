from django.db import models

# Create your models here.


#产品分类表
class Type(models.Model):
    id = models.AutoField("序号",primary_key= True)
    type_name = models.CharField("产品类型",max_length=20)
    #为了后台显示中文
    def __str__(self):
        return self.type_name

#产品信息表
class Product(models.Model):
    id = models.AutoField("序号",primary_key=True)
    name = models.CharField("名称",max_length=50)
    weight = models.CharField("重量",max_length=20)
    size =models.CharField("大小",max_length=20)
    type = models.ForeignKey(Type,on_delete=models.CASCADE, db_constraint=False,default=0,verbose_name='产品类型')

    #为了后台显示中文
    def __str__(self):
        return self.name
    class Meta:
        #防止多个产品时出现后缀s
        verbose_name = "产品信息"
        verbose_name_plural = "产品信息" #复数时


# class Info(models.Model):
#     # name = models.CharField(max_length=30, default="") #productname
#     # # userid = models.CharField(max_length=30, default="") #只有单片机端用到此信息
#     # secret = models.CharField(max_length=30, default="")

#     temptime = models.DateTimeField(auto_now=True)
#     # username = models.CharField(max_length=30, default="") #绑定到的账号名

#     # alertmail = models.CharField(max_length=30, default="")  # 邮箱
#     ##

# # no use
class History(models.Model):
    dataid = models.CharField(max_length=30, default="") #信息-工号
    temptime = models.DateTimeField(auto_now=True)
    
    productid = models.CharField(max_length=30, default="") #productname

