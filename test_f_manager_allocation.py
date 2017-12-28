# coding=UTF-8
from base import BaseSeleniumTestCase
from page.manager_allocation import ManagerAllocation
from page.test_page import TestPage
import time
from page.total_flow import TotalFlow
from page.credit_audit_loan_list import CreditAuditLoanList
from page.index import Index
from utilities.my_sql import select_customer,clear_customer


class TestManagerAllocation(BaseSeleniumTestCase):
    # 验证信审经理分配角色
    name = u'测试用户'
    login_name = 'zhangb'
    password = 'admin'

    # 验证分配按钮是否存在
    def test_allocation_button_true(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        text = ManagerAllocation(self.selenium).allocation_button()
        self.assertEqual(text, u'分配专员')

    # 验证状态
    def test_loan_status(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        # status = ManagerAllocation(self.selenium).get_loan_status(self.name)
        # self.assertEqual(status, u'待审核')
        # get_credit_person = ManagerAllocation(self.selenium).get_credit_person(self.name)
        # self.assertEqual(get_credit_person, u'')
        ManagerAllocation(self.selenium).allocation_role(self.name)
        time.sleep(2)
        status1 = ManagerAllocation(self.selenium).get_loan_status(self.name)
        self.assertEqual(status1, u'审批中')
        get_credit_person1 = ManagerAllocation(self.selenium).get_credit_person(self.name)
        time.sleep(0.5)
        self.assertEqual(get_credit_person1, u'许彤')
