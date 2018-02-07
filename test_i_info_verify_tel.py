# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.info_verify_tel import InfoVerifyTel
from utilities.my_sql import select_customer, clear_info_verify
import random


class TestInfoVerifyTel(BaseSeleniumTestCase):
    '''电核信息'''
    login_name = 'xut'
    password = 'admin'
    name = u'测试信审'
    num = random.randint(0, 10)
    text = u'测试电核信息'

    def test_info_verify_tel_success(self):
        '''测试电核信息'''
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        InfoVerifyTel(self.selenium, [get_customer_id]).info_verify(self.text)
