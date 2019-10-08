#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 19:56
# @Author  : Lin Luo
# @Site    :
# @File    : platform
# @Software: PyCharm
from common.utils.base_resource import BaseResource
from apps.domain.platform import Plat
from application import cache, app


class Platform(BaseResource):
    @cache.cached(app.config.get('PERMANENT_SESSION_LIFETIME'))
    def get(self, name):
        """

        :return:
        """
        plat_list = Plat.get_list(name)
        return self.succeed('平台列表查询成功', plat_list)
