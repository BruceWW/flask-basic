#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 19:32
# @Author  : Lin Luo
# @Site    :
# @File    : environment
# @Software: PyCharm
from sqlalchemy import and_

from application import db
from common.db_models.environment import Environment
from common.utils.base_db_operator import BaseDBOperator
from application import cache

class Env(BaseDBOperator):
    def __init__(self):
        super().__init__(Environment)

    @staticmethod
    def get_id_by_env(env):
        """
        根据环境名获取环境id
        :param env:
        :return:
        """
        info = db.session.query(Environment.id).filter(
            and_(Environment.name == env, Environment.is_del == 0, Environment.name)).first()
        if info is None:
            return False
        return info[0]

    @staticmethod
    @cache.cached()
    def get_list():
        """
        获取环境列表，没有分页功能，后续可以增加
        :return:
        """
        info = db.session.query(Environment).filter(Environment.is_del == 0).all()
        result = [item.to_dict() for item in info]
        return result
