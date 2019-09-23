#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 21:07
# @Author  : liuyang
# @Site    :
# @File    : Users
# @Software: PyCharm
from sqlalchemy import Column, Integer, SmallInteger, String, Text

from common.db_models import BaseDB, db_name_prefix
from application import db


class Users(BaseDB, db.Model):
    __tablename__ = db_name_prefix('user_info')
    username = Column(String(20), default='', comment='用户名')
    password = Column(String(64), default='', comment='用户密码，sha256加密')
    content = Column(Text, default='', comment='用户说明')
    role_id = Column(Integer, default=0, comment='角色id')
    is_del = Column(SmallInteger, default=0, comment='是否删除：0，否；1，是')
    create_user_id = Column(Integer, default=0, comment='创建人id')
    create_time = Column(Integer, default=0, comment='创建时间')
