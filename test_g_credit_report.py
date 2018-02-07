# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.credit_report import CreditReport
from utilities.my_sql import select_customer, clear_credit_report
import random


class TestCreditReport(BaseSeleniumTestCase):
    # 信用报告
    login_name = 'wanqh'
    password = 'admin'
    name = u'测试信审'
    num = random.randint(0, 10)

    amount = 10000
    use_amount = 20000
    min_amount = 30000
    real_amount = 40000
    overdue = 50000

    def test_customer_linkman_success(self):
        '''信用报告'''
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        CreditReport(self.selenium, [get_customer_id]).credit_report(self.num, self.amount, self.use_amount,
                                                                     self.min_amount, self.real_amount, self.overdue)

    def tearDown(self):
        super(TestCreditReport, self).tearDown()
        customer_id = select_customer(self.name)['id']
        clear_credit_report(customer_id)
