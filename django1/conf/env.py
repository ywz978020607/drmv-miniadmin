import os, glob

# 章节设置
SECTION = [
{'name': '主页1', 'link': '/app1/test/', },
{'name': '一级标题(链接自动失效)',
    'sub': [
        {'link': '/app1/test/sub1/', 'name': '二级1',},
    ]
},
]

# markdown系列
md_dict_notes = [
    {'name': '笔记本1(md渲染)',
     'sub': [
        {'link': '/md/notes1/readme.md/', 'name': '笔记1-readme', 'need_login': False},
        {'link': '/md/notes1/notes2.md/', 'name': 'notes2-笔记', 'need_login': False},
     ]
    },
]
SECTION += md_dict_notes

# 后台设置
SECTION.append({'name': '后台管理', 'link': '/admin/', 'need_login': False})


# 整合过滤
PATH_NAME_CACHE = {} # extract link_name_dict
SECTION_NOLOGIN = [] # SECTION_NOLOGIN
for head_1_item in SECTION:
    if 'link' in head_1_item.keys():
        PATH_NAME_CACHE[head_1_item['link']] = head_1_item['name']
        if head_1_item.get('need_login', True) == False:
            SECTION_NOLOGIN.append(head_1_item)
    elif len(head_1_item.get('sub', [])) > 0:
        temp_sub = []
        for head_2_item in head_1_item['sub']:
            PATH_NAME_CACHE[head_2_item['link']] = head_2_item['name']
            if head_2_item.get('need_login', True) == False:
                temp_sub.append(head_2_item)
        if len(temp_sub) > 0:
            SECTION_NOLOGIN.append({'name': head_1_item['name'], 'sub': temp_sub})
# print(PATH_NAME_CACHE)
