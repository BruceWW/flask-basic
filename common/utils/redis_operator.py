#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 21:12
# @Author  : Lin Luo
# @Site    :
# @File    : redis_operator
# @Software: PyCharm
from application import storage_redis


class RedisOperator(object):
    @staticmethod
    def set(key, value=None, expire=None):
        """
        设置redis的值
        :param key: 键名
        :param value: 键值
        :param expire: 超时时间，毫秒；如果为None则没有超时时间
        :return:
        """
        if expire is None:
            storage_redis.set(key, value)
        else:
            storage_redis.set(key, value, px=expire)
        return True

    @staticmethod
    def get(key, default=None):
        """
        获取redis的值，并进行防穿刺保护
        :param key: 键名
        :param default: 默认值
        :return:
        """
        result = storage_redis.get(key)
        if result is None:
            # TODO 需要根据ip进行穿刺查询的检查保护
            storage_redis.set(key, default)
            return default
        return result

    @staticmethod
    def delete(key):
        """
        删除失效的键
        :param key: 键名
        :return:
        """
        storage_redis.delete(key)
        return True
