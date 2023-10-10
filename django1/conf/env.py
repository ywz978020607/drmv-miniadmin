import os, glob

# 发送邮件的账号密钥
EMAIL_SENDER = {
    "addr": "978020607@qq.com",
    "api": "",
}

# 章节设置 - 共用标题栏
SECTION = [
{'name': '主页1', 'link': '/app1/test/', },
{'name': '一级标题(链接自动失效)',
    'sub': [
        {'link': '/app1/test/sub1/', 'name': '二级1',},
    ]
},
]

# markdown系列
md_dict_notes = {
    "笔记本1(md渲染)": {
        "/md/notes1/readme.md": "笔记1-readme",
    },
    
}
PATH_NAME_CACHE = {}
for nb_name in md_dict_notes.keys():
    sub_data = []
    md_dict_sub = md_dict_notes[nb_name]
    PATH_NAME_CACHE.update(md_dict_sub)
    for file_path in md_dict_sub.keys(): sub_data.append({'link': file_path + "/", 'name': md_dict_sub[file_path],},)
    SECTION.append({'name': nb_name,'sub': sub_data })

# 后台设置
SECTION.append({'name': '后台管理', 'link': '/admin/', })