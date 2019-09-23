#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 13:58
# @Author  : Lin Luo
# @Site    :
# @File    : file
# @Software: PyCharm
from os import path

from application import app
from common.utils.format_time import stamp_to_date


class File(object):
    @staticmethod
    def get_upload_file_path():
        """
        获取文件存储路径
        :return:
        """
        return path.join(app.root_path, app.config.get('FILE_PATH'), 'file', stamp_to_date())

