#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 21:15
# @Author  : Lin Luo
# @Site    :
# @File    : app_info
# @Software: PyCharm
from sqlalchemy import Column, Integer, SmallInteger, String, Text

from common.db_models import BaseDB, db_name_prefix
from application import db


class AppInfo(BaseDB, db.Model):
    __tablename__ = db_name_prefix('app_info')
    name = Column(String(50), default='', comment='应用名')
    content = Column(Text, default='', comment='应用说明')
    app_code = Column(String(50), default='', comment='应用code')
    is_del = Column(SmallInteger, default=0, comment='是否删除：0，否；1，是')
    create_user_id = Column(Integer, default=0, comment='创建人id')
    create_time = Column(Integer, default=0, comment='创建时间')
    token = Column(String(64), default='', comment='应用token')
