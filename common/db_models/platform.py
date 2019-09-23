#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 21:19
# @Author  : liuyang
# @Site    :
# @File    : platform
# @Software: PyCharm
from sqlalchemy import Column, SmallInteger, String, Integer, Text

from common.db_models import BaseDB, db_name_prefix
from application import db


class Platform(BaseDB, db.Model):
    __tablename__ = db_name_prefix('platform')
    name = Column(String(20), default='', comment='环境名称')
    num = Column(Integer, default=0, comment='序列号')
    content = Column(Text, default='', comment='角色说明')
    is_del = Column(SmallInteger, default=0, comment='是否删除：0，否；1，是')
