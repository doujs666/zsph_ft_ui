# -*- coding:utf-8 -*-
from .base_api import BaseApi


class UserRegister(BaseApi):
    """
    用户祖册
    """
    url = '/register'

    def build_custom_param(self, data):
        return {
            "mobile": data['mobile'],
            "verifyCode": data['verifyCode'],
            "password": data['password']
        }
