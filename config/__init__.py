#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 20:09
# @Author  : Lin Luo
# @Site    :
# @File    : __init__.py
# @Software: PyCharm
from os import urandom

__all__ = ['dev', 'sit', 'uat', 'prod']


def config_format(env):
    return 'config.%s' % env


class BaseConfig(object):
    """配置文件基类"""
    # 日志目录
    LOG_PATH = 'logs/flask.log'

    DEBUG = False

    # 数据库前缀
    DB_PREFIX = 'am'

    FILE_PATH = 'static'
    # 颜色模板位置
    COLOR_TEMPLATE_PATH = 'template'

    # 基础应用
    BASE_FILE = ['common.utils.common_request']
    RESTFUL = ['apps.controllers']

    # 图片后缀
    IMAGE_EXTENSIONS = ('png', 'jpg', 'jpeg', 'gif')

    # 不需要鉴权的路由
    EXCEPT_URL = ['/login']

    # 允许上船的文件后缀
    FILE_EXTENSIONS = ('xls', 'doc', 'ppt', 'xlsx', 'docx', 'pptx', 'txt', 'rar', 'zip', 'png', 'jpg', 'jpeg', 'gif')

    # 会话相关参数
    SESSION_COOKIE_NAME = 'X-Auth-Token'
    SECRET_KEY = urandom(24)
    PERMANENT_SESSION_LIFETIME = 600
    SESSION_USE_SIGNER = True
    SESSION_TYPE = 'redis'

    # redis基础操作键值
    DDOS_IP = 'ddos.ip'
    BLACK_IP_LIST = 'ip.list.black'
    API_CACHE = 'api.cache'
    API_LIST = 'api.list'

    # 开启数据库会话
    SQLQLCHEMY_COMMIT_TEARDOWN = True
