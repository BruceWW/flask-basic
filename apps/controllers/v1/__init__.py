#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 20:45
# @Author  : Lin Luo
# @Site    :
# @File    : __init__.py
# @Software: PyCharm

from application import restful
from .application import App, AppList, AppToken
from .environment import Environment
from .function import Function, FunctionList
from .platform import Platform
from .users import UserList, UserOperator

# for resource addition
restful.add_resource(AppToken, '/v1/app/token/<app_name>')
restful.add_resource(App, '/v1/app/<app_name>')
restful.add_resource(AppList, '/v1/app')
restful.add_resource(UserOperator, '/v1/user/<user_id>')
restful.add_resource(UserList, '/v1/user')
restful.add_resource(Environment, '/v1/env')
restful.add_resource(Platform, '/v1/platform')

# TODO 待调试
restful.add_resource(Function, '/v1/function/<function_id>')
restful.add_resource(FunctionList, '/v1/function')
