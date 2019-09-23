#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 20:48
# @Author  : liuyang
# @Site    :
# @File    : __init__.py
# @Software: PyCharm
from time import time

from flask import session
from sqlalchemy import Column, Integer

from application import app


def db_name_prefix(name):
    return '%s_%s' % (app.config.get('DB_PREFIX'), name)


class BaseDB(object):
    """数据库基类，建议所有数据库model全都继承"""
    id = Column(Integer, primary_key=True, autoincrement=True)

    def _get_column_object(self):
        """
        获取类中的Column对象
        :return:
        """
        columns = []
        for i in dir(self):
            if i.startswith('_'):
                continue
            if isinstance(getattr(self, i), int) or isinstance(getattr(self, i), str) or isinstance(getattr(self, i),
                                                                                                    float):
                columns.append(i)
        return columns

    def __init__(self):
        """
        初始化操作
        """
        if hasattr(self, 'create_time'):
            setattr(self, 'create_time', time())
        if hasattr(self, 'create_user_id'):
            setattr(self, 'create_user_id', session.get('admin_user_id'))

    def to_dict(self):
        """
        转换为字典
        :return:
        """
        attributes = self._get_column_object()
        result = {}
        for attribute in attributes:
            result[attribute] = getattr(self, attribute)
        return result
