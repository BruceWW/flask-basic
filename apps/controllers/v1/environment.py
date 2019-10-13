#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 19:53
# @Author  : Lin Luo
# @Site    :
# @File    : environment
# @Software: PyCharm
from apps.domain.environment import Env
from common.utils.base_resource import BaseResource


class Environment(BaseResource):
    def get(self):
        """
        获取环境列表， 采用缓存提升查询效率，且不设置失效时间
        :return:
        """
        env_list = Env.get_list()
        return self.succeed('环境列表查询成功', env_list)
