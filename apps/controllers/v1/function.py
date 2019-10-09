#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 21:12
# @Author  : Lin Luo
# @Site    :
# @File    : function
# @Software: PyCharm
from common.utils.base_resource import BaseResource
from common.utils.format_request import Request
from apps.domain.function import Func, ParamFormat


class Function(BaseResource):
    def get(self, function_id):
        """

        :param function_id:
        :return:
        """
        info = Func().query(function_id)
        if info is None:
            return self.error_404('接口查询失败')
        return self.succeed('接口查询成功', info)

    def put(self, function_id):
        """

        :param function_id:
        :return:
        """
        info = Request()

    def delete(self, function_id):
        """

        :param function_id:
        :return:
        """
        func = Func()
        if func.query(function_id) is None:
            return self.error_404('接口查询失败')
        func.delete(function_id)
        return self.succeed('接口删除成功')


class FunctionList(BaseResource):
    def get(self):
        """

        :return:
        """
        try:
            info = ParamFormat(Request()).get_search_params()
            function_info = Func.get_list(**info)
            return self.succeed('查询成功',
                                {'app_list': function_info.get('list'), 'page_info': function_info.get('page_info')})
        except ValueError as e:
            self.error_400(str(e))

    def post(self):
        """

        :return:
        """
        info = Request()
