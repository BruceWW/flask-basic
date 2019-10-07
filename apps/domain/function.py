#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 21:11
# @Author  : Lin Luo
# @Site    :
# @File    : function
# @Software: PyCharm

class Function(object):
    @staticmethod
    def create_redis_key(*args):
        """
        生成redis的键名
        :param args:
        :return:
        """
        return '.'.join(args)

    def init_redis(self):
        """
        初始化redis数据
        :return:
        """
