#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 19:25
# @Author  : Lin Luo
# @Site    :
# @File    : users
# @Software: PyCharm
from hashlib import sha256

from flask import session

from apps.domain.users import User
from common.utils.base_resource import BaseResource
from common.utils.format_request import Request
from common.utils.value_checker import int_checker, str_checker


class UserOperator(BaseResource):
    def get(self, user_id):
        """

        :param user_id:
        :return:
        """
        user_id = int(user_id)
        user_info = User().query(user_id)
        if user_info is None:
            return self.error_404('用户id：%d查询失败' % user_id)
        else:
            return self.succeed('用户查找成功', user_info)

    def put(self, user_id):
        """

        :param user_id:
        :return:
        """
        info = Request()
        user_id = int(user_id)
        user_object = User()
        username = str_checker(info.get_param('username'), 5, 20, default=None)
        password = str_checker((info.get_param('password')), 8, default=None)
        role_id = int_checker(info.get_param('role_id'), 1, 3, default=3)
        content = str_checker(info.get_param('content'), is_html_encode=True)
        if session.get('role') == 1:
            if user_object.update(user_id, role_id=role_id) is None:
                return self.error_404('用户不存在')
            else:
                self.succeed('用户更新成功')
        if session.get('admin_user_id') == user_id:
            if username is None:
                return self.error_400('用户名长度需要需要在5-20个字符之间')
            if password is None:
                return self.error_400('密码不符合要求')
            if user_object.update(user_id, username=username, password=sha256(password), content=content) is None:
                return self.error_404('用户不存在')
            else:
                self.succeed('用户更新成功')
        return self.error_403('用户更新失败')

    def delete(self, user_id):
        """
        根据用户id删除用户
        :param user_id:
        :return:
        """
        user_id = int(user_id)
        user_object = User()
        if session.get('role') != 1:
            return self.error_403('删除失败')
        if user_object is None:
            return self.error_404('用户id：%d删除失败' % user_id)
        user_object.delete(user_id)
        return self.succeed('用户id：%d删除成功' % user_id)


class UserList(BaseResource):
    def get(self):
        """
        获取用户列表
        :return:
        """
        info = Request()
        username = str_checker(info.get_param('username'), is_html_encode=True)
        page_size = int_checker(info.get_param('page_size', 10), 5, 50, default=10)
        page_index = int_checker(info.get_param('page_index', 1), 1, default=1)
        user_list, page_info = User.get_list(username, page_size, page_index)
        return self.succeed('查询成功', {'user_list': user_list, 'page_info': page_info})

    def post(self):
        """
        创建用户
        :return:
        """
        user_object = User()
        if session.get('role') != 1:
            return self.error_403('创建用户失败')
        info = Request()
        username = str_checker(info.get_param('username'), 5, 20, default=None, is_html_encode=True)
        password = str_checker((info.get_param('password')), 8, default=None, is_html_encode=True)
        if username is None:
            return self.error_400('用户名长度需要需要在5-20个字符之间')
        if password is None:
            return self.error_400('密码不符合要求')
        if user_object.check_username(username):
            user_object.create(username=username, password=sha256(password),
                               content=str_checker(info.get_param('content'), is_html_encode=True),
                               role_id=int_checker(info.get_param('role_id'), 1, 3, default=3))
            return self.succeed('用户创建成功')
        else:
            return self.error_400('用户名已被占用')
