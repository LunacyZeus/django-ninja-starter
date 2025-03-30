**django-ninja-starter**
**项目简介**
一个基于 Django、django-ninja-extra的快速开发项目脚手架
项目正在开发中......

**基本功能**
1.使用现代的、响应式的、扁平化的管理界面django-admin-interface  
2.使用gunicorn+uvicorn作为生产部署,提供一些详细的部署教程和参数配置  
3.使用supervisord守护进程部署    
4.提供了celery的基本配置  
5.提供了日志系统配置，详见application/settings/logging.py  
6.提供环境变量区分开发或生产环境  
7.接入django-ninja-extra，提供了简单的实例  
  

**常用命令**

```
tree -I '*.pyc|__init__.py'#输出当前项目文件目录架构
```

**TODO**
1.增加docker部署例子  
2.增加uwsgi部署例子  
3.增加websocket链接例子  
4.写一个基本的后台框架，提供简单的权限控制，vue3开发前端并使用AI根据现有代码进行前端crud自动生成（目前是内部自用项目，后面稳定了会剥离业务代码开源出来）  
5.接入prometheus对业务进行监控  
6.日志改成远程上传采集  
7.完善celery例子（后续开源）  
8.多租户支持例子  


#### 代码结构
```python
"""
├── README.md
├── application
│   ├── __pycache__
│   ├── admin.py
│   ├── asgi.py
│   ├── celery.py
│   ├── custom_exceptions.py
│   ├── db.sqlite3
│   ├── settings
│   │   ├── __pycache__
│   │   ├── common.py
│   │   ├── cors.py
│   │   ├── custom.py
│   │   ├── db.py
│   │   ├── logging.py
│   │   ├── middleware.py
│   │   └── redis.py
│   ├── urls.py
│   └── wsgi.py
├── apps
│   ├── __pycache__
│   ├── api.py
│   ├── base_app
│   │   ├── admin.py
│   │   ├── const.py
│   │   ├── controllers
│   │   │   └── base_app.py
│   │   ├── models.py
│   │   ├── schemes
│   │   │   └── base_app.py
│   │   ├── services
│   │   │   └── base_app.py
│   │   ├── tasks
│   │   ├── utils.py
│   │   └── views.py
│   ├── constants.py
│   └── demo
│       ├── __pycache__
│       ├── actions
│       │   ├── __pycache__
│       │   └── group.py
│       ├── admin.py
│       ├── apps.py
│       ├── const.py
│       ├── controllers
│       │   ├── __pycache__
│       │   └── demo.py
│       ├── migrations
│       │   └── __pycache__
│       ├── models.py
│       ├── schemes
│       │   ├── __pycache__
│       │   └── demo.py
│       ├── services
│       │   ├── __pycache__
│       │   └── demo.py
│       ├── tasks
│       ├── urls.py
│       ├── utils.py
│       └── views.py
├── data
│   ├── conf
│   │   ├── nginx
│   │   │   ├── demo.conf
│   │   │   └── nginx.conf
│   │   └── supervisord
│   │       ├── celery.ini
│   │       └── ecwit.ini
│   ├── docs
│   │   └── supervisord安装.md
│   └── scripts
│       └── empty_log.sh
├── gunicorn_config.py
├── logs
│   ├── demo.log
│   ├── error.log
│   ├── git.keep
│   └── server.log
├── manage.py
├── pkg
│   ├── __pycache__
│   ├── response
│   │   ├── __pycache__
│   │   └── response.py
│   ├── schemas
│   │   ├── __pycache__
│   │   ├── common.py
│   │   └── typehint.py
│   └── utils
│       ├── common.py
│       ├── ip.py
│       ├── mixins.py
│       └── redis
│           └── data_queue.py
├── pyproject.toml
├── static
│   └── git.keep
├── templates
│   └── git.keep
└── uv.lock
"""
```