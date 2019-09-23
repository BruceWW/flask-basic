#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 21:14
# @Author  : liuyang
# @Site    :
# @File    : application
# @Software: PyCharm
from hashlib import sha256
from time import time

from flask import session
from sqlalchemy import and_, func

from application import db
from common.db_models.app_info import AppInfo
from common.utils.base_db_operator import BaseDBOperator


class Application(BaseDBOperator):
    def __init__(self):
        super().__init__(AppInfo)

    @staticmethod
    def get_app_id_by_name(app_name):
        """
        根据应用名获取应用id
        :param app_name:
        :return:
        """
        info = db.session.query(AppInfo.id).filter(AppInfo.name == app_name).first()
        if info is None:
            return False
        else:
            return info[0]

    @staticmethod
    def create_token(app_name):
        """
        生成token
        :param app_name: 应用名
        :return:
        """
        return sha256('%s_%d' % (app_name, int(time())))

    def update_token(self, app_name):
        """
        根据app名称更新token
        :param app_name:
        :return:
        """
        new_token = self.create_token()
        db.session.query(AppInfo).filter(AppInfo.name == app_name).update(
            {AppInfo.token: new_token, AppInfo.create_time: time(),
             AppInfo.create_user_id: session.get('admin_user_id')})
        db.session.commit()
        return True

    @staticmethod
    def check_role():
        """
        检查操作用户是否可以操作对应应用
        :return:
        """
        if session.get('role') in (1, 2):
            return True
        else:
            return False

    @staticmethod
    def get_list(app_name, page_size=10, page_index=1):
        """
        获取应用列表
        :param app_name: 应用名，模糊查询
        :param page_size: 每页大小
        :param page_index: 页码
        :return:
        """
        current_num = page_size * page_index
        app_list = db.session.query(AppInfo).filter(
            and_(AppInfo.name.like('%%%s%%' % app_name), AppInfo.is_del == 0)).slice(
            current_num - page_size, current_num).all()
        app_num = db.session.query(func.count(AppInfo.id)).filter(
            and_(AppInfo.name.like('%%%s%%' % app_name), AppInfo.is_del == 0)).slice(
            current_num - page_size, current_num).all()
        return {'list': app_list,
                'page_info': {'page_num': app_num / page_size, 'page_index': page_index, 'page_size': page_size,
                              'total_num': app_num}}

    def create(self, **kwargs):
        """
        创建应用
        :param kwargs:
        :return:
        """
        token = self.create_token(kwargs.get('app_name'))
        return super().create(token=token, **kwargs)

    @staticmethod
    def get_info_by_app_name(app_name):
        """
        根据应用名获取应用信息
        :param app_name: 应用名
        :return:
        """
        app_info = db.session.query(AppInfo).filter(AppInfo.name == app_name).filter()
        if app_info is None:
            return False
        else:
            app_info = app_info.to_dict()
            del app_info['is_del']
            del app_info['token']
            return app_info
