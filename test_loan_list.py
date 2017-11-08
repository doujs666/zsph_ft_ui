# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.loan_list import LoanList


class TestCustomerLink(BaseSeleniumTestCase):
    user_name = 'zhangb'
    password = 'admin'
    apply_quota = 1000
    name = u'测试用户'
    repayment_quota = 100

    def test_customer_loan_apply_quota(self):
        TestPage(self.selenium).console_login(self.user_name, self.password)
        LoanList(self.selenium).allocation_role(self.name)

