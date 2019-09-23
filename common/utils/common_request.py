#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 20:01
# @Author  : Lin Luo
# @Site    :
# @File    : common_request
# @Software: PyCharm
from flask import jsonify

from application import app


@app.before_first_request
def before_first_request():
    pass


@app.before_request
def before_request():
    """
    验证用户登录
    :return:
    """
    print(123)


@app.errorhandler(400)
def error_400(e=None):
    """

    :param e:
    :return:
    """
    return jsonify({'status_code': 400, 'message': e})


@app.errorhandler(401)
def error_401(e=None):
    """
    401处理
    :param e:
    :return:
    """
    if e is None:
        e = 'login in please'
    else:
        e = str(e)
    app.logger.warning(e)
    return jsonify({'status_code': 401, 'message': e})


@app.errorhandler(403)
def error_403(e=None):
    """
    403处理
    :param e:
    :return:
    """
    if e is None:
        e = 'unauthorized'
    else:
        e = str(e)
    app.logger.warning(e)
    return jsonify({'status_code': 403, 'message': e})


@app.errorhandler(404)
def error_404(e=None):
    """
    404处理
    :param e:
    :return:
    """
    if e is None:
        e = 'file or page not found'
    else:
        e = str(e)
    app.logger.warning(e)
    return jsonify({'status_code': 404, 'message': e})


@app.errorhandler(500)
def error_500(e=None):
    """
    500处理
    :param e:
    :return:
    """
    if e is None:
        e = 'error occured'
    else:
        e = str(e)
    app.logger.error(e)
    return jsonify({'status_code': 500, 'message': e})


@app.teardown_request
def teardown_request(e=None):
    """
    请求结束操作
    :param e:
    :return:
    """
    print(234)
