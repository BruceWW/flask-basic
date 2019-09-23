#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 21:17
# @Author  : liuyang
# @Site    :
# @File    : environment
# @Software: PyCharm
from sqlalchemy import Column, SmallInteger, String

from common.db_models import BaseDB, db_name_prefix
from application import db


class Environment(BaseDB, db.Model):
    __tablename__ = db_name_prefix('env')
    name = Column(String(50), default='', comment='环境名称')
    is_del = Column(SmallInteger, default=0, comment='是否删除：0，否；1，是')
