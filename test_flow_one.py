# coding=UTF-8
from base import BaseSeleniumTestCase
from page.total_flow import TotalFlow
from page.loan_list import LoanList
from page.credit_audit_loan_list import CreditAuditLoanList
from page.index import Index
import time
from utilities.my_sql import select_customer, clear_customer, clear_credit_report, clear_info_verify, clear_contract, \
    clear_sign_page


class TestTotalFlow(BaseSeleniumTestCase):
    # 风控专员审核通过
    risk_management = 'tianl'
    judge_manager = 'zhangb'
    credit_person = 'sunf'
    manager_login_name = 'gesy'
    customer_name = u'张二十博'
    card_no = '340827198311170462'
    mobile = '13522241003'
    approved_product = '3'
    status = 'pass'
    bank_number = '6215590200000919787'

    def test_loan_status(self):
        # 新建客户
        TotalFlow(self.selenium).risk_management_new_customer(self.risk_management, self.customer_name, self.card_no,
                                                              self.mobile)
        time.sleep(2)
        status = LoanList(self.selenium).get_loan_status(self.customer_name)
        self.assertEqual(status, u'待审核')
        Index(self.selenium).click_user_list().click_user_quit()
        # 信审经理审核
        TotalFlow(self.selenium).judge_manager_allocation_role(self.judge_manager, self.customer_name)
        status1 = CreditAuditLoanList(self.selenium).get_loan_status(self.customer_name, self.judge_manager)
        self.assertEqual(status1, u'审批中')
        Index(self.selenium).click_user_list().click_user_quit()
        # 信审专员审核
        TotalFlow(self.selenium).risk_management_submit_audit(self.credit_person, self.customer_name, self.status)
        Index(self.selenium).click_user_list().click_user_quit()
        # 信审主管审核
        TotalFlow(self.selenium).manager_contract_form(self.manager_login_name, self.customer_name,
                                                       self.approved_product, self.status)
        status2 = CreditAuditLoanList(self.selenium).get_loan_status(self.customer_name, self.manager_login_name)
        self.assertEqual(status2, u'待签约')
        approved_product = CreditAuditLoanList(self.selenium).get_approved_product(self.customer_name, self.manager_login_name)
        self.assertEqual(approved_product, u'公积金类')
        Index(self.selenium).click_user_list().click_user_quit()
        # 风控专员提交合同
        TotalFlow(self.selenium).submit_sign_page(self.risk_management, self.customer_name, self.bank_number)
        status3 = LoanList(self.selenium).get_loan_status(self.customer_name)
        self.assertEqual(status3, u'合同审核中')
        approved_product1 = LoanList(self.selenium).get_approved_product(self.customer_name)
        self.assertEqual(approved_product1, u'公积金类')
        Index(self.selenium).click_user_list().click_user_quit()

    def tearDown(self):
        super(TestTotalFlow, self).tearDown()
        customer_id = select_customer(self.customer_name)['id']
        clear_credit_report(customer_id)
        clear_info_verify(customer_id)
        clear_contract(customer_id)
        clear_sign_page(customer_id)
        clear_customer(customer_id)
