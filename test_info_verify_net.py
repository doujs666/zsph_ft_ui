# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.info_verify_net import InfoVerifyNet
from utilities.my_sql import select_customer, clear_info_verify
import random


class TestInfoVerifyNet(BaseSeleniumTestCase):
    login_name = 'wanqh'
    password = 'admin'
    name = u'溜溜梅'
    num = random.randint(0, 10)
    text = u'测试网核信息'

    def test_info_verify_tel_success(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        InfoVerifyNet(self.selenium, [get_customer_id]).info_verify(self.text)

    # def tearDown(self):
    #     super(TestInfoVerifyNet, self).tearDown()
    #     customer_id = select_customer(self.name)['id']
    #     clear_info_verify(customer_id)
