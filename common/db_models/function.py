#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 21:19
# @Author  : Lin Luo
# @Site    :
# @File    : platform
# @Software: PyCharm
from sqlalchemy import Column, SmallInteger, String, Integer, Text, Float

from common.db_models import BaseDB, db_name_prefix
from application import db


class Function(BaseDB, db.Model):
    __tablename__ = db_name_prefix('function')
    name = Column(String(20), default='', comment='方法名称')
    content = Column(Text, default='', comment='方法说明')
    is_del = Column(SmallInteger, default=0, comment='是否删除：0，否；1，是')
    env_id = Column(Integer, default=0, comment='环境id')
    app_id = Column(Integer, default=0, comment='应用id')
    platform_num = Column(Integer, default=0, comment='涉及的平台')
    is_grey = Column(SmallInteger, default=0, comment='是否灰度：0，否；1，是')
    function_name = Column(String(255), default='', comment='api名')
    url = Column(String(255), default='', comment='url地址')
    create_user_id = Column(Integer, default=0, comment='创建人id')
    create_time = Column(Integer, default=0, comment='创建时间')
    del_time = Column(Integer, default=0, comment='失效时间')
    version = Column(Float, default=1.0, comment='版本号')
