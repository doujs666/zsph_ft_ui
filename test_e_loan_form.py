# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.loan_form import CustomerLoan
from utilities.my_sql import select_customer, customer_loan, loan_amount, clear_customer_loan, clear_customer
from page.loan_list import LoanList
from page.customer_from import CustomerFrom
import time
import random


class TestCustomerLoan(BaseSeleniumTestCase):
    '''申请信息'''

    login_name = 'gaohf'
    password = 'admin'
    apply_quota = 1000
    user_name = u'测试新建用户提交'
    repayment_quota = 100

    def setUp(self):
        super(TestCustomerLoan, self).setUp()
        TestPage(self.selenium).console_login(self.login_name, self.password)
        CustomerFrom(self.selenium).new_customer(self.user_name, '220281198210024400', '13651020001', '2', '234567@qq.com',
                                                 20000)

    def test_customer_loan_apply_quota(self):
        '''申请金额'''
        get_customer_id = select_customer(self.user_name)['id']
        message = CustomerLoan(self.selenium, [get_customer_id]).loan_apply_quota(
            'addd').customer_loan_apply_quota_error()
        self.assertEqual(message, u'请输入数字可带小数')

    def test_customer_loan_repayment_quota(self):
        '''最高月还款'''
        get_customer_id = select_customer(self.user_name)['id']
        message = CustomerLoan(self.selenium, [get_customer_id]).loan_repayment_quota(
            'addd').customer_loan_repayment_quota_error()
        self.assertEqual(message, u'请输入数字可带小数')

    def test_customer_loan_v_success(self):
        '''提交成功'''
        db_loan_amount = loan_amount()
        get_customer_id = select_customer(self.user_name)['id']
        type_number = str(random.randint(1, 4))
        cycle_number = str((random.randint(1, 3)) * 12)
        CustomerLoan(self.selenium, [get_customer_id]).customer_loan_save(type_number, self.apply_quota, cycle_number,
                                                                     self.repayment_quota)
        detail = customer_loan(get_customer_id)
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
        self.assertEqual(db_loan_amount, new_loan_amount -1)
        # 提交通过
        CustomerLoan(self.selenium, [get_customer_id]).customer_loan_submit()
        time.sleep(2)
        status = LoanList(self.selenium).get_loan_status(self.user_name)
        self.assertEqual(status, u'审批中')

    def tearDown(self):
        super(TestCustomerLoan, self).tearDown()
        get_customer_id = select_customer(self.user_name)['id']
        clear_customer_loan(get_customer_id)
        clear_customer(get_customer_id)
