#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 13:25
# @Author  : liuyang
# @Site    :
# @File    : base_resource
# @Software: PyCharm
from flask import jsonify, current_app, make_response
from flask_restful import Resource

from .format_request import Request
from application import app


class BaseResource(Resource):
    """
    Rest框架基类
    """

    def __init__(self):
        self._request = Request()
        self._app = current_app

    @property
    def request(self):
        return self._request

    @property
    def app(self):
        return self._app

    def succeed(self, message=None, info=None, **kwargs):
        return self.format_result(200, 'success' if message is None else message, info, **kwargs)

    @staticmethod
    def format_result(code=200, message=None, info=None, **kwargs):
        """
        
        :param code:
        :param message:
        :param info:
        :param kwargs:
        :return:
        """
        result = {key: value for key, value in kwargs}
        if result.get('message') is None:
            result['message'] = message
        if result.get('data') is None and info is not None and info != '':
            result['data'] = info
        result['status_code'] = code
        return make_response(result, code)

    def error_400(self, message=None, info='', **kwargs):
        """
        400异常处理
        :param message: 提示信息
        :param info: 返回的内容
        :param kwargs: 其他参数
        :return:
        """
        app.logger.warning(message, info)
        return self.format_result(400, message, info, **kwargs)

    def error_401(self, message=None, info='', **kwargs):
        """
        401异常处理
        :param message: 提示信息
        :param info: 返回的内容
        :param kwargs: 其他参数
        :return:
        """
        app.logger.warning(message, info)
        return self.format_result(401, message, info, **kwargs)

    def error_403(self, message=None, info='', **kwargs):
        """
        403异常处理
        :param message: 提示信息
        :param info: 返回的内容
        :param kwargs: 其他参数
        :return:
        """
        app.logger.warning(message, info)
        return self.format_result(403, message, info, **kwargs)

    def error_404(self, message=None, info='', **kwargs):
        """
        404异常处理
        :param message: 提示信息
        :param info: 返回的内容
        :param kwargs: 其他参数
        :return:
        """
        app.logger.warning(message, info)
        return self.format_result(404, message, info, **kwargs)

    def error_500(self, message=None, info='', **kwargs):
        """
        500异常处理
        :param message:
        :param info:
        :param kwargs:
        :return:
        """
        app.logger.warning(message, info)
        return self.format_result(500, message, info, **kwargs)
