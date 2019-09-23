#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 20:12
# @Author  : Lin Luo
# @Site    :
# @File    : index
# @Software: PyCharm
from application import init_app

if __name__ == '__main__':
    init_app('dev').run(port=4060)
