#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 20:12
# @Author  : liuyang
# @Site    :
# @File    : application
# @Software: PyCharm
import importlib
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler

from flask import Flask, Blueprint
from flask_caching import Cache
from flask_redis import FlaskRedis
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from werkzeug.utils import import_string

from config import config_format

app = Flask(__name__)

cache = Cache()
db = SQLAlchemy()
storage_redis = FlaskRedis(config_prefix='STORAGE_REDIS')
session = Session()
restful = Api(app)


def init_app(env):
    # 获取配置参数类
    config = importlib.import_module(config_format(env)).Config
    # 加载配置参数
    app.config.from_object(config)
    # 初始化数据库参数
    db.init_app(app)
    # 初始化redis参数
    storage_redis.init_app(app)
    # cache.init_app(app)
    session.init_app(app)

    # 设置日志输出以及回滚周期
    formatter = Formatter('[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s')
    handler = TimedRotatingFileHandler(config.LOG_PATH, when='D', interval=1, backupCount=15, encoding='utf-8',
                                       delay=False, utc=True)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    for rest_file in config.RESTFUL:
        importlib.import_module(rest_file)

    for base_file in config.BASE_FILE:
        importlib.import_module(base_file)
    # from apps.controllers.login import Login
    # restful.add_resource(Login, '/login')

    # from apps.controllers import init_restful
    # init_restful()

    # for blueprint in config.BLUEPRINT:
    #     app.register_blueprint(import_string(blueprint))

    return app
