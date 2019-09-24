#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 19:29
# @Author  : Lin Luo
# @Site    :
# @File    : users
# @Software: PyCharm
from sqlalchemy import and_, func

from application import db
from common.db_models.users import Users
from common.utils.base_db_operator import BaseDBOperator


class User(BaseDBOperator):
    def __init__(self):
        """
        初始化，传入操作的数据库类
        """
        super().__init__(Users)

    def query(self, instance_id):
        info = super().query(instance_id)
        if info is not None:
            info.pop('password')
            info.pop('create_user_id')
            info.pop('create_time')
        return info

    @staticmethod
    def get_list(username, page_size=10, page_index=1):
        """
        查询用户信息列表
        :param username: 用户名，模糊查询
        :param page_size: 每页数量
        :param page_index: 查询的页码
        :return:
        """
        current_num = page_size * page_index
        user_list = db.session.query(Users.id, Users.username, Users.content, Users.role_id).filter(and_(
            Users.username.like('%%%s%%' % username), Users.is_del == 0)).slice(current_num - page_size,
                                                                                current_num).all()
        user_num = db.session.query(func.count(Users.id)).filter(
            and_(Users.username.like('%%%s%%' % username), Users.is_del == 0)).first()[0]
        # TODO 需要把role转换为角色名称
        for i in range(len(user_list)):
            user_list[i] = {'user_id': user_list[i][0], 'user_name': user_list[i][1], 'content': user_list[i][2],
                            'role': user_list[i][3]}
        return {'list': user_list,
                'page_info': {'page_num': user_num / page_size, 'page_index': page_index, 'page_size': page_size,
                              'total_num': user_num}}

    @staticmethod
    def check_username(username):
        """
        检查用户名是否被占用
        :param username: 用户名
        :return:
        """
        user_info = db.session.query(Users.id).filter(Users.username == username).first()
        if user_info is None:
            return True
        else:
            return False
