#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 20:20
# @Author  : Lin Luo
# @Site    :
# @File    : dev
# @Software: PyCharm
from . import BaseConfig
from redis import Redis


class Config(BaseConfig):
    """开发环境配置参数"""

    SQLALCHEMY_ECHO = True
    DEBUG = True
    EMV = 'dev'

    # DB
    DB_USERNAME = 'root'
    DB_PASSWORD = 'root'
    DB_HOST = '127.0.0.1'
    DB_PORT = '3306'
    DB_DATABASE = 'api_manager'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
        DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE)

    # redis 库
    STORAGE_REDIS_HOST = '127.0.0.1'
    STORAGE_REDIS_PORT = '6379'
    STORAGE_REDIS_PASSWORD = ''
    STORAGE_REDIS_NUM = '1'
    STORAGE_REDIS_URL = 'redis://%s@%s:%s/%s' % (
        STORAGE_REDIS_PASSWORD, STORAGE_REDIS_HOST, STORAGE_REDIS_PORT, STORAGE_REDIS_NUM)

    # 缓存配置
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = '6379'
    CACHE_REDIS_PASSWORD = ''
    CACHE_REDIS_DB = '2'

    # 会话管理库
    SESSION_REDIS_HOST = '127.0.0.1'
    SESSION_REDIS_PORT = '6379'
    SESSION_REDIS_PASSWORD = ''
    SESSION_REDIS_NUM = '3'
    SESSION_REDIS = Redis(host=SESSION_REDIS_HOST, port=SESSION_REDIS_PORT, db=SESSION_REDIS_NUM,
                          password=SESSION_REDIS_PASSWORD)
