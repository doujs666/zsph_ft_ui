# -*- coding: utf-8 -*-
from base import BaseSeleniumTestCase
from page.total_flow import TotalFlow
from page.loan_list import LoanList
from page.contract_list import ContractList
from page.credit_audit_loan_list import CreditAuditLoanList
from page.historical_list import HistoricalList
from page.index import Index
from utilities.my_sql import select_customer, clear_customer, clear_credit_report, clear_info_verify, clear_contract, \
    clear_sign_page, get_credit_person_login_name
import time


class TestTotalFlow(BaseSeleniumTestCase):
    # 风控专员审核通过
    risk_management = 'zhangbb'
    judge_manager = 'zhangb'
    credit_person = 'wanqh'
    manager_login_name = 'gesy'
    loan_manager = 'zhangy'
    super_script_manager = 'dulr'
    customer_name = u'张宝1'
    card_no = '340101198108119853'
    mobile = '18689262777'
    approved_product = '3'
    status = 'pass'
    bank_number = '6212262201024460356'
    project_number = '998556'

    def test_loan_status(self):
        """总流程"""

        for i in range(20):
            customer_name = u'流程' + str(i+6)
            card_no = str(340101198108210301 + i)
            mobile = str(18689242831 + i)
            # 新建客户
            TotalFlow(self.selenium).risk_management_new_customer(self.risk_management, customer_name, card_no,
                                                                  mobile)
            Index(self.selenium).click_user_list().click_user_quit()

            # 风控专员审核
            TotalFlow(self.selenium).risk_management_submit(self.risk_management, customer_name)
            time.sleep(2)
            # status = LoanList(self.selenium).get_loan_status(self.customer_name)
            # self.assertEqual(status, u'审批中')
            Index(self.selenium).click_user_list().click_user_quit()
            print(i)
        #
        # # 信审经理审核
        # TotalFlow(self.selenium).judge_manager_allocation_role(self.judge_manager, self.customer_name)
        # status1 = CreditAuditLoanList(self.selenium).get_loan_status(self.customer_name, self.judge_manager)
        # self.assertEqual(status1, u'审批中')
        # Index(self.selenium).click_user_list().click_user_quit()
        #
        # #信审专员审核
        # get_customer_id = select_customer(self.customer_name)['id']
        # credit_person_login_name = get_credit_person_login_name(get_customer_id)['login_name']
        # TotalFlow(self.selenium).risk_management_other(credit_person_login_name, self.customer_name)
        # Index(self.selenium).click_user_list().click_user_quit()
        # TotalFlow(self.selenium).risk_management_submit_audit(credit_person_login_name, self.customer_name, self.status)
        # Index(self.selenium).click_user_list().click_user_quit()
        #
        # # 信审主管审核
        # TotalFlow(self.selenium).manager_contract_form(self.manager_login_name, self.customer_name,
        #                                                self.approved_product, self.status)
        # status2 = HistoricalList(self.selenium).get_loan_status(self.customer_name, self.manager_login_name)
        # self.assertEqual(status2, u'待签约')
        # approved_product = HistoricalList(self.selenium).get_approved_product(self.customer_name,
        #                                                                       self.manager_login_name)
        # self.assertEqual(approved_product, u'公积金类')
        # Index(self.selenium).click_user_list().click_user_quit()
        #
    #     # 风控专员提交合同
    #     TotalFlow(self.selenium).submit_sign_page(self.risk_management, self.customer_name, self.bank_number)
    #     status3 = LoanList(self.selenium).get_loan_status(self.customer_name)
    #     self.assertEqual(status3, u'合同审核中')
    #     approved_product1 = LoanList(self.selenium).get_approved_product(self.customer_name)
    #     self.assertEqual(approved_product1, u'公积金类')
    #     Index(self.selenium).click_user_list().click_user_quit()
    #
    #     # 合同专员审核
    #     TotalFlow(self.selenium).loan_sign_page(self.loan_manager, self.customer_name)
    #     status4 = ContractList(self.selenium).get_loan_status(self.customer_name)
    #     self.assertEqual(status4, u'放款中')
    #     Index(self.selenium).click_user_list().click_user_quit()
    #     # 上标专员审核
    #     TotalFlow(self.selenium).super_script_flow(self.super_script_manager, self.customer_name, self.project_number)
    #     Index(self.selenium).click_user_list().click_user_quit()
    #
    #     # 合同专员放款
    #     TotalFlow(self.selenium).make_loan_sign_page(self.loan_manager, self.customer_name)
    #     status6 = ContractList(self.selenium).get_loan_status(self.customer_name)
    #     self.assertEqual(status6, u'已放款')
    #     Index(self.selenium).click_user_list().click_user_quit()
    #
    # def tearDown(self):
    #     super(TestTotalFlow, self).tearDown()
    #     customer_id = select_customer(self.customer_name)['id']
    #     clear_credit_report(customer_id)
    #     clear_info_verify(customer_id)
    #     clear_contract(customer_id)
    #     clear_sign_page(customer_id)
    #     clear_customer(customer_id)
