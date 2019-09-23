#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 20:45
# @Author  : liuyang
# @Site    :
# @File    : __init__.py
# @Software: PyCharm

from application import restful
from .application import App, AppList, AppToken
from .users import UserList, UserOperator

restful.add_resource(AppToken, '/v1/app/token/<app_name>')
restful.add_resource(App, '/v1/app/<app_name>')
restful.add_resource(AppList, '/v1/app')
restful.add_resource(UserOperator, '/v1/user/<user_id>')
restful.add_resource(UserList, '/v1/user')
