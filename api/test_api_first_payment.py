# -*- coding:utf-8 -*-
from unittest import TestCase
from api.base_api.first_payment_api import FirstPayment
import json,settings


class TestFirstPaymentApi(TestCase):
    username = 'gaohf'
    password = 'admin'

    @classmethod
    def test_get_response_content(self):
        first_user_invest_api = FirstPayment()
        first_user_invest_api.post({"username": self.username, "password": self.password})
        print first_user_invest_api.get_response_message()
        # self.assertEqual(first_user_invest_api.get_code(), u'0000')
        # self.assertEqual(first_user_invest_api.get_response_message(), u'账户余额不足')