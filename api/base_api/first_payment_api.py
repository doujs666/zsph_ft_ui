# -*- coding:utf-8 -*-
from api.base_api.base_api import BaseApi


class FirstPayment(BaseApi):
    """
    签到
    """
    url = '/api/notify/firstPayment'

    def build_custom_param(self,data):
        return {
            "creditId": data['creditId'],
            "token": data['token'],
            }
