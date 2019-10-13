#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 21:12
# @Author  : Lin Luo
# @Site    :
# @File    : function
# @Software: PyCharm
from apps.domain.function import Func, ParamFormat
from common.utils.base_resource import BaseResource
from common.utils.format_request import Request


class Function(BaseResource):
    def get(self, function_id):
        """

        :param function_id:
        :return:
        """
        info = Func().query(function_id)
        if info is None:
            return self.error_404('接口%s不存在' % function_id)
        return self.succeed('接口查询成功', info)

    def put(self, function_id):
        """
        只允许更新urk地址和content
        :param function_id:
        :return:
        """
        try:
            # info = ParamFormat(Request()).get_operate_params()
            info = Request()
        except ValueError as e:
            return self.error_400(str(e))
        if Func().update(function_id, url=info.get_param('url'), coontent=info.get_param('content')) is None:
            return self.error_404('接口%s不存在' % function_id)
        return self.succeed('接口%s更新成功' % function_id)

    def delete(self, function_id):
        """

        :param function_id:
        :return:
        """
        func = Func()
        if func.delete(function_id) is None:
            return self.error_404('接口%s不存在' % function_id)
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
            return self.error_400(str(e))
        except BaseException as e:
            return self.error_500(str(e))

    def post(self):
        """

        :return:
        """
        try:
            info = ParamFormat(Request()).get_operate_params()
        except ValueError as e:
            return self.error_400(str(e))
        func = Func()
        if func.check_name(info.get('name'), info.get('app_id'), info.get('env_id'), info.get('version'),
                           info.get('platform_num')) is False:
            return self.error_400('路由名已被占用')
        if func.check_function_name(info.get('name'), info.get('app_id'), info.get('env_id'),
                                    info.get('version'), info.get('platform_num')) is False:
            return self.error_400('函数名已被占用')
        function_id = func.create(**info)
        return self.succeed('接口创建成功', {'function_id': function_id})


class CacheTest(BaseResource):
    def get(self):
        Func().init_redis()
        return self.succeed()
