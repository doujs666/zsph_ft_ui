# -*- coding:utf-8 -*-
from api.web_api.base_web_api import WebBaseApi


class FirstPayment(WebBaseApi):
    """
    签到
    """
    url = '/'

    def build_custom_param(self,data):
        return {
            "username": data['username'],
            "password": data['password'],
            }
