#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 19:43
# @Author  : Lin Luo
# @Site    :
# @File    : platform
# @Software: PyCharm
from sqlalchemy import and_, func

from application import db
from common.db_models.platform import Platform
from common.utils.base_db_operator import BaseDBOperator


class Plat(BaseDBOperator):
    def __init__(self):
        super().__init__(Platform)

    @staticmethod
    def get_list(name=''):
        """
        获取平台列表，没有分页功能
        :param name:
        :return:
        """
        info = db.session.query(Platform).filter(and_(Platform.name.like('%%%s%%' % name), Platform.is_del == 0)).all()
        result = [item.to_dict() for item in info]
        return result

    @staticmethod
    def get_platform_count():
        """
        获取当前平台的数量
        :return:
        """
        return db.session.query(func.count(Platform.id)).all()[0]

    def platform_num_to_list(self, platform_num, is_id=0):
        """
        将平台求和后的数量，转换为平台名称的列表
        :param platform_num: 平台求和后的数量
        :param is_id: 是够转换为id的列表
        :return:
        """
        if platform_num == 0:
            return []
        bin_str = str(bin(platform_num))
        num_list = []
        for i, item in enumerate(bin_str):
            if item == '1':
                num_list.append(i + 1) if is_id == 1 else num_list.append(self.query(i + 1))
        return num_list

    def get_platform_num(self, num_list):
        """
        根据平台数字的列表，获取可能相关的平台序列号列表
        :param num_list:
        :return:
        """
        # 获取当前平台总数，包括被删除的
        total_num = self.get_platform_count()
        platform_count_list = set(range(total_num)).difference(set(num_list))
        platform_num = [None] * len(platform_count_list)
        base_str = '0' * total_num
        for i in num_list:
            base_str[i - 1] = '1'
        for i in platform_count_list:
            pass
        # TODO


