#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 19:25
# @Author  : liuyang
# @Site    :
# @File    : login
# @Software: PyCharm
from flask import session

from application import restful
from common.utils.base_resource import BaseResource
from common.utils.format_request import Request
from ..domain.authorization import Authorization


class Login(BaseResource):
    def post(self):
        """
        用户登陆
        :return:
        """
        request = Request()
        username = request.get_param('username')
        password = request.get_param('password')
        if Authorization.login_check(username, password):
            return self.succeed('登陆成功')
        else:
            return self.error_401('登陆失败，用户名或密码错误')

    def get(self):
        """
        获取用户登陆状态
        :return:
        """
        if session.get('admin_user_id') is not None:
            return self.succeed('用户已登录', {'username': session.get('admin_user'), 'role': session.get('role')})
        else:
            return self.error_401('登陆失败，用户名或密码错误')


class Logout(BaseResource):
    def post(self):
        """
        注销用户登陆
        :return:
        """
        Authorization.logout()
        return self.succeed('登陆注销成功')


restful.add_resource(Login, '/login')
restful.add_resource(Logout, '/logout')
