#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 19:29
# @Author  : Lin Luo
# @Site    :
# @File    : login
# @Software: PyCharm
from flask import session
from sqlalchemy import and_
from hashlib import sha256

from application import db
from common.db_models.users import Users


class Authorization(object):
    @staticmethod
    def login_check(username, password):
        """
        用户登陆
        :param username: 用户名
        :param password: 用户密码
        :return:
        """
        info = db.session.query(Users).filter(
            and_(Users.username == username, Users.password == sha256(password.encode('utf-8')).hexdigest())).first()
        if info is None:
            return False
        else:
            session['admin_user_id'] = info.id
            session['admin_user'] = info.username
            session['role'] = info.role_id
            return True

    @staticmethod
    def logout():
        """
        用户登出
        :return:
        """
        del session['admin_user_id']
        del session['admin_user']
        del session['role']
        return True
