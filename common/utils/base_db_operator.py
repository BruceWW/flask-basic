#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 21:12
# @Author  : Lin Luo
# @Site    :
# @File    : base_db_operator
# @Software: PyCharm
from time import time

from flask import session
from sqlalchemy import and_, text

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
            # 为避免update重写对删除造成影响
            return BaseDBOperator(self._abstraction).update(instance_id, is_del=1)
        else:
            instance = self._abstraction.query.filter(self._abstraction.id == instance_id).first()
            db.session.delete(instance)
            db.session.commit()
            return True

    def update(self, instance_id, **kwargs):
        """
        根据id更新数据
        :param instance_id: 实例id
        :param kwargs: 更新的数据
        :return:
        """
        if kwargs.get('check_del', True) is True:
            check_del = self._abstraction.is_del == 0
        else:
            check_del = text('')
        instance = self._abstraction.query.filter(and_(self._abstraction.id == instance_id, check_del)).first()
        if instance is None:
            return None
        for key, value in kwargs.items():
            if hasattr(instance, key) and value is not None:
                setattr(instance, key, value)
        if hasattr(instance, 'update_time'):
            instance.update_time = time()
        if hasattr(instance, 'update_user_id'):
            instance.update_user_id = session.get('admin_user_id')
        db.session.commit()
        return instance.id

    def query(self, instance_id, check_del=True):
        """
        根据id查询数据，并转换成字典类型
        :param instance_id:
        :param check_del: 是否需要检查被删除数据
        :return:
        """
        if check_del is True:
            check_del = self._abstraction.is_del == 0
        else:
            check_del = text('')
        instance = db.session.query(self._abstraction).filter(
            and_(self._abstraction.id == instance_id, check_del)).first()
        if instance is None:
            return None
        else:
            return instance.to_dict()
