#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 21:11
# @Author  : Lin Luo
# @Site    :
# @File    : function
# @Software: PyCharm
from sqlalchemy import and_, func, text

from application import db, app, storage_redis
from common.db_models.function import Function
from common.utils.base_db_operator import BaseDBOperator
from common.utils.value_checker import str_checker, int_checker, float_checker
from .application import Application
from .environment import Env


class ParamFormat(object):
    def __init__(self, info):
        self._info = info
        self._params_dict = {'env_id': None, 'app_id': None, 'platform_num': None, 'is_grey': None, 'name': None,
                             'content': None, 'function_name': '', 'url': '', 'version': 0.0, 'page_size': 10,
                             'page_index': 1}
        self._result = dict()

    def get_operate_params(self):
        """
        获取操作接口相关的参数
        :return:
        """
        self._trans_dict()
        self._check_operate_params()
        return self._result

    def get_search_params(self):
        """
        获取查询接口相关的参数
        :return:
        """
        self._trans_dict()
        self._check_search_params()
        return self._result

    def _trans_dict(self):
        for key, value in self._params_dict.items():
            self._result[key] = self._info.get_param(key, value)

    def _check_operate_params(self):
        """
        检查创建、编辑的操作合法性
        :return:
        """
        self._result.pop('page_size')
        self._result.pop('page_index')
        self._result['env_id'] = int_checker(self._result.get('env_id'), 0, default=0)
        if self._result.get('env_id') == 0:
            raise ValueError('环境参数异常')
        self._result['app_id'] = int_checker(self._result.get('app_id'), 0, default=0)
        if self._result.get('app_id') == 0:
            raise ValueError('应用参数错误')
        self._result['is_grey'] = int_checker(self._result.get('is_grey'), 0, default=0)
        self._result['platform_num'] = int_checker(self._result.get('platform_num'), 0, default=0)
        if self._result.get('platform_num') == 0:
            raise ValueError('平台参数异常')
        self._result['name'] = str_checker(self._result.get('name'), 5, 100, is_html_encode=True, default=None)
        if self._result['name'] is None:
            raise ValueError('路由名参数错误')
        self._result['content'] = str_checker(self._result.get('content'), is_html_encode=True)
        self._result['url'] = str_checker(self._result.get('url'), is_html_encode=True, default='')
        if self._result.get('url') == '':
            raise ValueError('API路由不能为空')
        self._result['version'] = float_checker(self._result.get('version'), 0.0, default=0.0)
        if self._result.get('version') == 0.0:
            raise ValueError('版本号异常')
        self._result['function_name'] = str_checker(self._result.get('function_name'), 5, 255, is_html_encode=True,
                                                    default=None)
        if self._result.get('function_name') is None:
            raise ValueError('函数名称参数异常')

    def _check_search_params(self):
        """
        检查查询的参数合法性
        :return:
        """
        if self._result.get('env_id') is None:
            self._result['env_id'] = 0
        if self._result.get('app_id') is None:
            self._result['app_id'] = 0
        int_checker(self._result.get('page_size'), 5, 50, default=10)
        int_checker(self._result.get('page_index'), 1, default=1)
        self._result.pop('function_name')
        self._result.pop('url')
        self._result.pop('version')


class Func(BaseDBOperator):
    def __init__(self):
        super().__init__(Function)

    @staticmethod
    def create_redis_key(args):
        """
        生成redis的键名
        :param args:
        :return:
        """
        args = (str(arg) for arg in args)
        return '.'.join(args)

    def create_redis_key_by_id(self, function_id):
        """
        根据接口id创建redis的键名
        :param function_id:
        :return:
        """
        return self.create_redis_key(
            db.session.query(Function.app_id, Function.env_id, Function.platform_num, Function.name,
                             Function.version).filter(Function.id == function_id).first())

    @staticmethod
    def format_result(result=None):
        """
        对查询到的应用id，环境id等参数进行替换
        :param result:
        :return:
        """
        if result is None:
            return dict()
        else:
            result['environment'] = Env().query(result.get('env_id')).get('name')
            result['application_name'] = Application().query(result.get('app_id')).get('name')
        return result

    def init_redis(self):
        """
        初始化redis数据
        :return:
        """
        # 清空原有hash的数据
        storage_redis.delete(app.config.get('API_CACHE'))
        tmp_list = db.session.query(Function.app_id, Function.env_id, Function.platform_num, Function.name,
                                    Function.version, Function.url).filter(Function.is_del == 0).all()
        info = dict()
        for item in tmp_list:
            info[self.create_redis_key((item[0], item[1], item[2], item[3], item[4]))] = item[5]
        storage_redis.hmset(app.config.get('API_CACHE'), info)
        return True

    @staticmethod
    def update_redis(key, value):
        """
        更新数据
        :param key:
        :param value:
        :return:
        """
        storage_redis.hset(app.config.get('API_CACHE'), key, value)

    @staticmethod
    def del_redis(key):
        """
        删除redis数据
        :param key:
        :return:
        """
        storage_redis.hdel(app.config.get('API_CACHE'), key)
        return True

    def delete(self, instance_id, is_real=False):
        """
        重写删除方法，删除同时更新redis数据
        :param instance_id:
        :param is_real:
        :return:
        """
        res = super().delete(instance_id, is_real)
        if res is not None:
            self.del_redis(self.create_redis_key_by_id(instance_id))
        return res

    def update(self, instance_id, **kwargs):
        """
        重新更新方法，更新同时更新redis数据
        :param instance_id:
        :param kwargs:
        :return:
        """
        res = super().update(instance_id, **kwargs)
        if res is not None:
            key = self.create_redis_key((kwargs.get('app_id'), kwargs.get('env_id'), kwargs.get('platform_num'),
                                         kwargs.get('name'), kwargs.get('version')))
            self.update_redis(key, kwargs.get('url'))
        return res

    def create(self, **kwargs):
        res = super().create(**kwargs)
        if res is not None:
            key = self.create_redis_key((kwargs.get('app_id'), kwargs.get('env_id'), kwargs.get('platform_num'),
                                         kwargs.get('name'), kwargs.get('version')))
            self.update_redis(key, kwargs.get('url'))
        return res

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
        pass

    @staticmethod
    def check_name(name, app_id, env_id, version, platform_num):
        """
        检查相同的app id，环境以及版本是否有重名的路由名称
        :param name: 路由名称
        :param app_id: 应用id
        :param env_id: 环境id
        :param version: 版本号
        :param platform_num: 平台id
        :return:
        """
        if db.session.query(Function.id).filter(
                and_(Function.name == name, Function.app_id == app_id, Function.env_id == env_id,
                     Function.version == version, Function.is_del == 0,
                     Function.platform_num == platform_num)).first() is None:
            return True
        else:
            return False

    @staticmethod
    def check_function_name(function_name, app_id, env_id, version, platform_num):
        """
        检查相同的app id，环境以及版本是否有重名的函数名称
        :param function_name: 函数名称
        :param app_id: 应用id
        :param env_id: 环境id
        :param version: 版本号
        :param platform_num: 平台id
        :return:
        """
        if db.session.query(Function.id).filter(
                and_(Function.function_name == function_name, Function.app_id == app_id, Function.env_id == env_id,
                     Function.version == version, Function.is_del == 0,
                     Function.platform_num == platform_num)).first() is None:
            return True
        else:
            return False

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
            env_id = text('')
        else:
            env_id = Function.env_id == env_id
        if app_id == 0:
            app_id = text('')
        else:
            app_id = Function.app_id == app_id
        if platform_num == 0 or platform_num is None:
            platform_num = text('')
        else:
            platform_num = Function.platform_num == platform_num
        if is_grey is None:
            is_grey = text('')
        else:
            is_grey = Function.is_grey == is_grey
        if name is None:
            name = text('')
        else:
            name = Function.name.like('%%%s%%' % name)
        if content is None:
            content = text('')
        else:
            content = Function.content.like('%%%s%%' % content)
        current_num = page_size * page_index
        where = and_(env_id, app_id, platform_num, is_grey, name, content, Function.is_del == 0)
        function_list = db.session.query(Function).filter(where).slice(current_num - page_size, current_num).all()
        function_num = len(
            db.session.query(func.count(Function.id)).filter(where).slice(current_num - page_size, current_num).all())
        return {'list': function_list,
                'page_info': {'page_num': int(function_num / page_size) + 1, 'page_index': page_index,
                              'page_size': page_size, 'total_num': function_num}}
