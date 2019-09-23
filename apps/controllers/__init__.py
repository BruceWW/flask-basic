#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 21:27
# @Author  : liuyang
# @Site    :
# @File    : __init__.py
# @Software: PyCharm

import os
import pkgutil

pkg_path = os.path.dirname(__file__)
pkg_name = os.path.basename(pkg_path)

# for _, file, _ in pkgutil.iter_modules([pkg_path]):
#     # __import__(pkg_name + '.' + file)
#     __import__(file)

from . import login



__all__ = ['login']

# from .application import App, AppList, AppToken
# from .login import Login, Logout
# from .users import UserOperator, UserList
# from application import restful


# def init_restful():
#     restful.add_resource(AppToken, '/v1/app/token/<app_name>')
#     restful.add_resource(App, '/v1/app/<app_name>')
#     restful.add_resource(AppList, '/v1/app')
#     restful.add_resource(Login, '/login')
#     restful.add_resource(Logout, '/logout')
#     restful.add_resource(UserOperator, '/v1/user/<user_id>')
#     restful.add_resource(UserList, '/v1/user')
