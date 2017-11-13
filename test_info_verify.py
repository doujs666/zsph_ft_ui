# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.info_verify import InfoVerify
from utilities.my_sql import select_customer, clear_info_verify
import random


class TestInfoVerify(BaseSeleniumTestCase):
    login_name = 'wanqh'
    password = 'admin'
    name = u'测试用户'
    num = random.randint(0, 10)
    text = u'测试备注'

    def test_customer_linkman_success(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        InfoVerify(self.selenium, [get_customer_id]).info_verify(self.text)

    def tearDown(self):
        super(TestInfoVerify, self).tearDown()
        customer_id = select_customer(self.name)['id']
        clear_info_verify(customer_id)
