import os

from django1.settings import BASE_DIR


# 发送邮件的账号密钥
email_sender = {
    "addr": "978020607@qq.com",
    "api": "",
}


# 章节设置 - 共用标题栏
section = [
{'name': '主页1', 'link': '/app1/test/', },
{'name': '一级标题(链接自动失效)',
    'sub': [
        {'link': '/app1/test/sub1/', 'name': '二级1',},
    ]
},
{'name': '后台管理', 'link': '/admin/', },

]