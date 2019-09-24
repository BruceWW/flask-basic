#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 12:10
# @Author  : Lin Luo
# @Site    :
# @File    : value_checker
# @Software: PyCharm
from html import escape

"""输入合法性检查"""


def num_checker(num, min_num=None, max_num=None, min_line=True, max_line=True, default=None):
    """
    对数字进行检查
    :param num: 需要检查的值
    :param min_num: 允许的最小值
    :param max_num: 允许的最大值
    :param min_line: 最小值是否闭区间
    :param max_line: 最大值是否闭区间
    :param default: 默认值，用于异常情况返回
    :return:
    """
    # 判断是否有最小值限制
    if min_num is not None:
        # 如果有最小值限制
        # 判断是否是闭区间
        if min_line is True:
            # 如果是闭区间，则判断是否小于最小值限制
            if min_num > num:
                return default
        else:
            # 如果是开区间，则判断是否小于或等于最小值限制
            if min_num >= num:
                return default
    # 判断是否有最大值限制
    if max_num is not None:
        # 如果有最大值限制
        # 判断是否是闭区间
        if max_line is True:
            # 如果是闭区间，则判断是否大于最大值
            if max_num < num:
                return default
        else:
            # 如果是开区间，则判断是否大于或等于最大值
            if max_num <= num:
                return default
    return num


def int_checker(num, min_num=None, max_num=None, min_line=True, max_line=True, default=0):
    """
    对整型数字进行检查
    :param num: 需要检查的值
    :param min_num: 允许的最小值
    :param max_num: 允许的最大值
    :param min_line: 最小值是否闭区间
    :param max_line: 最大值是否闭区间
    :param default: 默认值，用于异常情况返回
    :return:
    """
    try:
        return num_checker(int(num), min_num, max_num, min_line, max_line, default)
    except ValueError:
        # 如果不是整型
        return default
    except TypeError:
        return default


def float_checker(num, min_num=None, max_num=None, min_line=True, max_line=True, default=0):
    """
    对浮点型数字进行检查
    :param num: 需要检查的值
    :param min_num: 允许的最小值
    :param max_num: 允许的最大值
    :param min_line: 最小值是否闭区间
    :param max_line: 最大值是否闭区间
    :param default: 默认值，用于异常情况返回
    :return:
    """
    try:
        return num_checker(float(num), min_num, max_num, min_line, max_line, default)
    except ValueError:
        # 如果不是浮点型
        return default


def str_checker(value, min_length=None, max_length=None, min_line=True, max_line=True, default='',
                is_html_encode=False):
    """
    对字符串进行检查
    :param value: 需要检查的字符串
    :param min_length: 允许的最小长度
    :param max_length: 允许的最大长度
    :param min_line: 最小值是否闭区间
    :param max_line: 最大值是否闭区间
    :param default: 默认值，用于异常情况返回
    :param is_html_encode: 是否行进html转义
    :return:
    """
    try:
        # 对字符串长度进行判断
        if value is None:
            return default
        checker = num_checker(len(value), min_length, max_length, min_line, max_line, None)
        if checker is not None:
            checker = value
        else:
            checker = default
        # 如果返回None，则说明异常，返回默认值
        if checker is None:
            if default is None:
                return None
            return escape(default) if is_html_encode else default
        else:
            return escape(checker) if is_html_encode else checker
    except TypeError:
        return escape(default) if is_html_encode else default
