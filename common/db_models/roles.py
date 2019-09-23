#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 21:13
# @Author  : Lin Luo
# @Site    :
# @File    : roles
# @Software: PyCharm
from sqlalchemy import Column, SmallInteger, String, Text

from common.db_models import BaseDB, db_name_prefix
from application import db


class Roles(BaseDB, db.Model):
    __tablename__ = db_name_prefix('role')
    name = Column(String(20), default='', comment='角色名称')
    content = Column(Text, default='', comment='角色说明')
    is_del = Column(SmallInteger, default=0, comment='是否删除：0，否；1，是')
