#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 21:13
# @Author  : Lin Luo
# @Site    :
# @File    : application
# @Software: PyCharm
from apps.domain.application import Application
from common.utils.base_resource import BaseResource
from common.utils.format_request import Request
from common.utils.value_checker import str_checker, int_checker


class App(BaseResource):
    def get(self, app_name):
        """
        根据应用名称获取应用信息
        :param app_name:
        :return:
        """
        app_name = str_checker(app_name, is_html_encode=True)
        app_info = Application().get_info_by_app_name(app_name)
        if app_info is False:
            return self.error_404('应用：%s查询失败' % app_name)
        else:
            return self.succeed('应用查找成功', app_info)

    def put(self, app_name):
        """

        :param app_name:
        :return:
        """
        app = Application()
        if not app.check_role():
            return self.error_403('没有权限操作应用')
        info = Request()
        content = str_checker(info.get_param('content'), default=True, is_html_encode=True)
        app_id = app.get_app_id_by_name(app_name)
        if app_id is False:
            return self.error_404('应用：%s更新失败' % app_name)
        app.update(app_id, content=content)
        return self.succeed('应用：%s更新成功' % app_name)

    def delete(self, app_name):
        """
        根据应用名称删除应用
        :param app_name:
        :return:
        """
        app = Application()
        if not app.check_role():
            return self.error_403('没有权限操作应用')
        app_id = app.get_app_id_by_name(app_name)
        if app_id is False:
            return self.error_404('应用：%s删除失败' % app_name)
        app.delete(app_id)
        return self.succeed('应用：%s删除成功' % app_name)


class AppList(BaseResource):
    def get(self):
        """
        获取应用列表
        :return:
        """
        info = Request()
        app_name = str_checker(info.get_param('app_name'))
        page_size = int_checker(info.get_param('page_size', 10), 5, 50, default=10)
        page_index = int_checker(info.get_param('page_index', 1), 1, default=1)
        app_info = Application.get_list(app_name, page_size, page_index)
        return self.succeed('查询成功', {'app_list': app_info.get('list'), 'page_info': app_info.get('page_info')})

    def post(self):
        """
        创建应用
        :return:
        """
        app = Application()
        if not app.check_role():
            return self.error_403('没有权限操作应用')
        info = Request()
        app_name = str_checker(info.get_param('app_name'), 5, 50, default='', is_html_encode=True)
        if app_name is None or app_name == '':
            return self.error_400('应用名长度需要需要在5-50个字符之间')
        content = str_checker(info.get_param('content'), default='', is_html_encode=True)
        if not app.get_app_id_by_name(app_name):
            app_id = app.create(name=app_name, content=content)
            return self.succeed('应用创建成功', {'app_id': app_id})
        else:
            return self.error_400('应用名已被占用')


class AppToken(BaseResource):
    def get(self, app_name):
        """
        根据应用名获取token
        :param app_name:
        :return:
        """
        app = Application()
        if not app.check_role():
            return self.error_403('没有权限操作应用')
        app_id = app.get_app_id_by_name(app_name)
        if not app_id:
            return self.error_404('应用名错误')
        info = app.query(app_id)
        return self.succeed('应用token查询成功', {'token': info.get('token')})

    def put(self, app_name):
        """
        更新应用token
        :param app_name: 应用名
        :return:
        """
        app_name = str_checker(app_name, is_html_encode=True)
        app = Application()
        if not app.check_role():
            return self.error_403('没有权限操作应用')
        if not app.get_app_id_by_name(app_name):
            return self.error_404('应用名错误')
        new_token = app.update_token(app_name)
        return self.succeed('应用token更新成功', {'token': new_token})
