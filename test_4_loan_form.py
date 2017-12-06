# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.loan_form import CustomerLoan
from utilities.my_sql import select_customer, customer_loan, loan_amount
from page.loan_list import LoanList
import random


class TestCustomerLink(BaseSeleniumTestCase):
    # 申请信息
    login_name = 'gaohf'
    password = 'admin'
    apply_quota = 1000
    name = '测试流程'
    repayment_quota = 100

    def test_customer_loan_apply_quota(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        message = CustomerLoan(self.selenium, [get_customer_id]).loan_apply_quota(
            'addd').customer_loan_apply_quota_error()
        self.assertEqual(message, u'请输入数字可带小数')

    def test_customer_loan_repayment_quota(self):
        TestPage(self.selenium).console_login(self.user_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        message = CustomerLoan(self.selenium, [get_customer_id]).loan_repayment_quota(
            'addd').customer_loan_repayment_quota_error()
        self.assertEqual(message, u'请输入数字可带小数')

    def test_customer_loan_v_success(self):
        db_loan_amount = loan_amount()
        TestPage(self.selenium).console_login(self.user_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        type_number = str(random.randint(1, 6))
        cycle_number = str((random.randint(1, 3)) * 12)
        CustomerLoan(self.selenium, [get_customer_id]).customer_loan(type_number, self.apply_quota, cycle_number,
                                                                     self.repayment_quota)
        customer_id = select_customer(self.name)['id']
        detail = customer_loan(customer_id)
        # 借款类型
        db_loan_type = detail['type']
        self.assertEqual(db_loan_type, type_number)
        # 申请金额
        db_loan_apply_quota = detail['apply_quota']
        self.assertEqual(db_loan_apply_quota, self.apply_quota)
        # 申请期限
        db_loan_cycle = detail['cycle']
        self.assertEqual(db_loan_cycle, int(cycle_number))
        # 可接受最高月还款
        db_loan_repayment_quota = detail['repayment_quota']
        self.assertEqual(db_loan_repayment_quota, self.repayment_quota)
        # 验证loan数量
        new_loan_amount = loan_amount()
        self.assertEqual(db_loan_amount, new_loan_amount - 1)
        # loan页面验证
        title_loan_amount = int(LoanList(self.selenium).loan_amount()[22:24])
        self.assertEqual(new_loan_amount, title_loan_amount)