#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 21:11
# @Author  : Lin Luo
# @Site    :
# @File    : function
# @Software: PyCharm
from common.utils.base_db_operator import BaseDBOperator
from common.db_models.function import Function
from .platform import Plat
from application import db

from sqlalchemy import and_, func


class Function(BaseDBOperator):
    def __init__(self):
        super().__init__(Function)

    @staticmethod
    def create_redis_key(*args):
        """
        生成redis的键名
        :param args:
        :return:
        """
        return '.'.join(args)

    @staticmethod
    def calculate_platform_num(num):
        """
        计算
        :param num:
        :return:
        """
        plat = Plat()
        platform_count = plat.get_platform_count()
        num_list = plat.platform_num_to_list(num, 1)

    def init_redis(self):
        """
        初始化redis数据
        :return:
        """

    def get_fun(self, env_id, app_id, platform_num, is_grey, name, version):
        """
        根据各种条件，查询api的地址
        :param env_id:
        :param app_id:
        :param platform_num:
        :param is_grey:
        :param name:
        :param version:
        :return:
        """

    @staticmethod
    def get_list(env_id=0, app_id=0, platform_num=0, is_grey=None, name=None, content=None, page_size=10,
                 page_index=1):
        """

        :param env_id:
        :param app_id:
        :param platform_num:
        :param is_grey:
        :param name:
        :param content:
        :param page_size:
        :param page_index:
        :return:
        """
        # 操作查询条件
        if env_id == 0:
            env_id = ''
        else:
            env_id = Function.env_id == env_id
        if app_id == 0:
            app_id = ''
        else:
            app_id = Function.app_id == app_id
        if platform_num == 0:
            platform_num = ''
        else:
            platform_num = Function.platform_num == platform_num
        if is_grey is None:
            is_grey = ''
        else:
            is_grey = Function.is_grey == is_grey
        if name is None:
            name = ''
        else:
            name = Function.name.like('%%%s%%' % name)
        if content is None:
            content = ''
        else:
            content = Function.name.like('%%%s%%' % content)
        current_num = page_size * page_index
        where = and_(env_id, app_id, platform_num, is_grey, name, content, Function.is_del == 0)
        function_list = db.session.query(Function).filter(where).slice(current_num - page_size, current_num).all()
        function_num = len(
            db.session.query(func.count(Function.id)).filter(where).slice(current_num - page_size, current_num).all())
        return {'list': function_list,
                'page_info': {'page_num': int(function_num / page_size) + 1, 'page_index': page_index,
                              'page_size': page_size, 'total_num': function_num}}
