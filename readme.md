# Django Render Markdown/Vue.js(~~nodejs~~) with sqlite3
## DRMV全后端简易后台管理网站方案
<img src=".readme/drmv.png" width="300" />

基于django模板渲染能力，前端基础为inspinia(bootstrap系)，结合django自带权限管理后台  
提供一个django+vue二次渲染的小网站demo，面向个人全栈量产式开发应用场景，提供一套基础小demo，方便二次开发

## 特性
- 易调试：单python命令可完整启动调试
- 易部署：支持docker+nginx+uwsgi部署
- 免编译：前端支持markdown/单页式Vue，无需编译前端
- 低依赖：装好django即可，不需任何nodejs相关环境即可使用vue
- 支持后台管理：复用django-admin后台管理，可嵌套模板
- 支持游客模式：对目录可选验证登录属性，不登录也可看部分章节，方便做wifi分享
- 前后端不分离：后端一把梭，重后端弱前端，部署时可选启用nginx部分-仅增加文件服务器功能，也可仅uwsgi部署django
- 容灾性扩展：可选，支持一主多从、多机热备方案，单脚本维护
- 免配置数据库：采用sqlite3文件式数据库，免安装配置、易迁移
- 代码简单
- 维护方便
- 易迁移


## 技术方案
django+django-render+markdown/vue.js(~~nodejs~~)+sqlite3

## 优点：
1. 适合小型网站快速开发
2. 后端一把梭，render时两次渲染，免去一次ajax向后端要数据的过程，后端所赋即前端所得，自动变量渲染
3. 前端非编译写法，且套用模板，方便多个子页面书写时仅关注内容即可，方便快速增接口
4. 后端render提供html给前端，非前后端分离，在鉴权/缓存等方面有优势，直接复用django自带的认证权限/缓存功能，并使用缓存过滤所有变量
5. 免配置数据库，利用文件类型数据库
6. 不需要npm，不需要nodejs，不需要单独安装前端环境，方便交付后部署环境下修改前端
7. 支持markdown原生写法直接转网页目录，方便做wifi，免编译

## 缺点
非主流开发方式，前后端不分离

## 测试方法
```
cd django1/
python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000 # 即可打开浏览器直接输入ip:8000访问
```

## 部署方法
```
cd docker/
docker-compose build
docker-compose up -d
```

## 页面展示(主站+后台)
其中后台为django默认自带页面，如需美化可一键安装django-simpleui等主题包

<center class="half">
<img src=".readme/mainpage1.png" width="500" />
<img src=".readme/mainpage2.png" width="500" />
<img src=".readme/mainpage3.png" width="500" />
<img src=".readme/backpage1.png" width="500" />
<img src=".readme/backpage2.png" width="500" />
</center>

## 其他说明
项目已经对静态文件规整，兼容debug的开关双模式，在django后端对静态文件路由，uwsgi/(nginx)不需单独配置，(当然如果想另外配置静态文件也可以)。  
通过静态文件路由模式的兼容，极大方便了纯python运行时、uwsgi/docker运行下的调试模式分别开或关的代码兼容。
- 总结一句话，无论用哪种启动方式，都可自由地只改动setting.py中debug=True或False切换运行模式，不需特意处理静态文件路由。
- 另外，如果想额外再次打包静态文件(python manage.py collectstatic)，需要到settings中设置1. debug=True 2. collect_mode=True

# 一主多从扩展
见dnsdbsync.py 我使用的cloudfare进行域名管理和主节点在线判断，使用sshpass等方式进行同步
