#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 21:12
# @Author  : Lin Luo
# @Site    :
# @File    : base_db_operator
# @Software: PyCharm
from time import time

from flask import session

from application import db


class BaseDBOperator(object):
    def __init__(self, abstraction):
        self._abstraction = abstraction

    def create(self, **kwargs):
        """
        创建数据
        :param kwargs:
        :return:
        """
        instance = self._abstraction()
        if hasattr(instance, 'create_time'):
            instance.update_time = time()
        if hasattr(instance, 'create_user_id'):
            instance.update_user_id = session.get('admin_user_id')
        for key in kwargs.keys():
            if hasattr(instance, key):
                setattr(instance, key, kwargs.get(key))
        db.session.add(instance)
        db.session.commit()
        return instance.id

    def delete(self, instance_id, is_real=False):
        """
        执行删除操作
        :param instance_id:
        :param is_real: 是否真删
        :return:
        """
        if is_real is False:
            return self.update(instance_id, is_del=1)
        else:
            instance = self._abstraction.query.filter(self._abstraction.id == instance_id).first()
            db.session.delete(instance)
            db.session.commit()

    def update(self, instance_id, **kwargs):
        """
        根据id更新数据
        :param instance_id: 实例id
        :param kwargs: 更新的数据
        :return:
        """
        instance = self._abstraction.query.filter(self._abstraction.id == instance_id).first()
        if instance is None:
            return None
        for key in kwargs.keys():
            if hasattr(instance, key):
                setattr(instance, key, kwargs.get(key))
            if hasattr(instance, 'update_time'):
                instance.update_time = time()
            if hasattr(instance, 'update_user_id'):
                instance.update_user_id = session.get('admin_user_id')
            db.session.commit()
            return instance.id

    def query(self, instance_id):
        """
        根据id查询数据，并转换成字典类型
        :param instance_id:
        :return:
        """
        # instance = db.session.query(self._abstraction).filter(self._abstraction.id == instance_id).first()
        instance = self._abstraction.query(self._abstraction.id == instance_id).first()
        if instance is None:
            return False
        else:
            return instance.to_dict()
