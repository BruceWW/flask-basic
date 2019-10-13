#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/13 13:42
# @Author  : Lin Luo
# @Site    :
# @File    : ddos_exception
# @Software: PyCharm


class DDosException(BaseException):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message
