# DRRV全后端小型demo - 不分离式个人快速开发
基于django模板渲染能力，前端基础为inspinia(bootstrap系)，结合django自带权限管理后台  
提供一个django+vue二次渲染的小网站demo，面向个人全栈量产式开发应用场景，提供一套基础小demo，方便二次开发

## 技术方案
django+django-render+vue.js(非分离编译-模板+动态引入后编译)+sqlite3

## 优点：
1. 适合小型网站快速开发
2. 后端一把梭，render时两次渲染，免去一次ajax向后端要数据的过程，后端所赋即前端所得，自动变量渲染
3. 前端非编译写法，且套用模板，方便多个子页面书写时仅关注内容即可，方便快速增接口
4. 后端render提供html给前端，非前后端分离，在鉴权/缓存等方面有优势，直接复用django自带的认证权限/缓存功能，并使用缓存过滤所有变量
5. 免配置数据库，利用文件类型数据库
6. 不需要npm，不需要nodejs，不需要单独安装前端环境，方便交付后部署环境下修改前端


## 缺点
1. 非主流开发方式，前后端不分离
2. 前端非编译式写法，页面可理解为二次渲染，相比于编译压缩的前端工程，体积更大
3. 无法通过nginx等单独部署前端，项目部署时采用uwsgi/docker部署

## 测试方法
```
python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000 # 即可打开浏览器直接输入ip:8000访问
```

## 页面展示(主站+后台)
其中后台为django默认自带页面，如需美化可一键安装django-simpleui等主题包

<center class="half">
<img src=".introduction/mainpage1.png" width="500" />
<img src=".introduction/mainpage2.png" width="500" />
<img src=".introduction/mainpage3.png" width="500" />
<img src=".introduction/backpage1.png" width="500" />
<img src=".introduction/backpage2.png" width="500" />
</center>

