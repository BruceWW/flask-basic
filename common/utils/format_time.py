#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 14:00
# @Author  : liuyang
# @Site    : 
# @File    : format_time
# @Software: PyCharm
from time import time, strftime, strptime, localtime, mktime


def stamp_to_date(stamp=time(), ymd=True):
    """
    将时间戳转换为日期格式
    :param stamp:
    :param ymd:
    :return:
    """
    if ymd:
        return strftime('%Y-%m-%d', localtime(stamp))
    else:
        return strftime('%Y-%m-%d %H:%M:%S', localtime(stamp))


def date_to_stamp(date=time()):
    """
    将日期格式转换为时间戳
    :param date:
    :return:
    """
    try:
        time_array = strptime(str(date), '%Y-%m-%d %H:%M:%S')
        return mktime(time_array)
    except ValueError:
        time_array = strptime(str(date), '%Y-%m-%d')
        return mktime(time_array)
