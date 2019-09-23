#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 13:42
# @Author  : Lin Luo
# @Site    :
# @File    : format_request
# @Software: PyCharm
from flask import request
from application import app


class Request(object):
    """前台传入的参数操作类"""

    def __init__(self):
        """
        初始化
        """
        self._request = request
        if self._request.method == 'PUT':
            self._dicts = self._request.json
        elif self._request.method == 'POST':
            if self._request.json is not None:
                self._dicts = self._request.json
            elif len(self._request.form) != 0:
                self._dicts = self._request.form
            else:
                self._dicts = self._request.args
        else:
            self._dicts = self._request.args
        self._files = self._request.files

    @property
    def request(self):
        return self._request

    @property
    def dicts(self):
        return self._dicts

    @property
    def files(self):
        return self._files

    def get_param(self, key='', default=None):
        """
        根据键获取单个参数
        :param key: 键名
        :param default: 默认值
        :return:
        """
        return self._dicts.get(key, default)

    def get_params(self, keys=None, default=None):
        """
        根据键的列表，获取多个参数
        :param keys: 键的列表
        :param default: 默认值
        :return:
        """
        result = {}
        if keys is not None:
            for key in keys:
                result[key] = self.get_param(key, default)
        return result

    def get_file(self, key=''):
        """
        根据键获取文件
        :param key: 键值
        :return:
        """
        return self._files.get(key)

    def get_files(self, keys=None):
        """
        根据键的列表获取多个文件
        :param keys: 键的列表
        :return:
        """
        result = {}
        if keys is not None:
            for key in keys:
                result[key] = self.get_file(key)
        return result

    def get_all(self, params=None, files=None):
        """
        获取所有类型的参数
        :param params: 参数列表
        :param files: 文件列表
        :return:
        """
        return {'params': self.get_param(params), 'files': self.get_files(files)}

    def get_token(self):
        """
        获取用户传入的token
        :return:
        """
        return self._request.cookies.get(app.config.get('SESSION_COOKIE_NAME'), None)
