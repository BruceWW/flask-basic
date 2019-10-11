#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 19:56
# @Author  : Lin Luo
# @Site    :
# @File    : platform
# @Software: PyCharm
from application import cache, app
from apps.domain.platform import Plat
from common.utils.base_resource import BaseResource
from common.utils.format_request import Request


class Platform(BaseResource):
    @cache.cached(app.config.get('PERMANENT_SESSION_LIFETIME'))
    def get(self):
        """
        根据名称查询平台，提供缓存
        :return:
        """
        plat_list = Plat.get_list(Request().get_param('name', ''))
        return self.succeed('平台列表查询成功', plat_list)
