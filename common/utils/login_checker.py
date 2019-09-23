#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 20:29
# @Author  : Lin Luo
# @Site    :
# @File    : login_check
# @Software: PyCharm
from flask import session, abort


def login_require(func):
    """
    装饰器，判断用户是否登录
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        if session.get('admin_user_id') is None:
            abort(401, '用户未登录')
        else:
            return func(*args, **kwargs)

    return inner
