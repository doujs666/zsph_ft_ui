# coding=UTF-8
from base import BaseSeleniumTestCase
from page.total_flow import TotalFlow
from page.loan_list import LoanList
from page.contract_list import ContractList
from page.credit_audit_loan_list import CreditAuditLoanList
from page.historical_list import HistoricalList
from page.index import Index
from utilities.my_sql import select_customer, clear_customer, clear_credit_report, clear_info_verify, clear_contract, \
    clear_sign_page


class TestTotalFlow(BaseSeleniumTestCase):
    # 驳回

    customer_name = u'张博5'
    card_no = '131023197908293345'
    mobile = '13522241005'
    reject_status = 'repulse'
    pass_status = 'pass'
    risk_management = 'gaohf'
    judge_manager = 'zhangb'
    credit_person = 'wanqh'
    manager_login_name = 'gesy'
    loan_manager = 'zhangy'
    super_script_manager = 'dulr'
    review_manager = 'zhangbb'
    approved_product = '3'
    bank_number = '6215590200000919787'
    project_number = '998556'

    def test_loan_status(self):
        '''信审专员拒绝'''

        # 新建客户
        TotalFlow(self.selenium).risk_management_new_customer(self.risk_management, self.customer_name, self.card_no,
                                                              self.mobile)
        Index(self.selenium).click_user_list().click_user_quit()

        # 风控专员审核
        TotalFlow(self.selenium).risk_management_submit(self.risk_management, self.customer_name)
        Index(self.selenium).click_user_list().click_user_quit()

        # 信审经理审核
        TotalFlow(self.selenium).judge_manager_allocation_role(self.judge_manager, self.customer_name)
        status1 = CreditAuditLoanList(self.selenium).get_loan_status(self.customer_name, self.judge_manager)
        self.assertEqual(status1, u'审批中')
        Index(self.selenium).click_user_list().click_user_quit()
        # 信审专员审核驳回
        TotalFlow(self.selenium).risk_management_other(self.credit_person, self.customer_name)
        Index(self.selenium).click_user_list().click_user_quit()
        TotalFlow(self.selenium).risk_management_submit_audit(self.credit_person, self.customer_name, self.reject_status)
        status2 = HistoricalList(self.selenium).get_loan_status(self.customer_name, self.credit_person)
        self.assertEqual(status2, u'补充资料')
        Index(self.selenium).click_user_list().click_user_quit()

        # 风控专员审核
        TotalFlow(self.selenium).risk_management_submit(self.risk_management, self.customer_name)
        Index(self.selenium).click_user_list().click_user_quit()

        # 信审专员审核通过
        TotalFlow(self.selenium).risk_management_submit_audit(self.credit_person, self.customer_name,
                                                              self.pass_status)
        status2 = HistoricalList(self.selenium).get_loan_status(self.customer_name, self.credit_person)
        self.assertEqual(status2, u'复核中')
        Index(self.selenium).click_user_list().click_user_quit()

        # 信审主管审核驳回到信审专员
        TotalFlow(self.selenium).manager_contract_form(self.manager_login_name, self.customer_name,
                                                       self.approved_product, self.pass_status)
        status2 = HistoricalList(self.selenium).get_loan_status(self.customer_name, self.manager_login_name)
        self.assertEqual(status2, u'待签约')
        approved_product = HistoricalList(self.selenium).get_approved_product(self.customer_name, self.manager_login_name)
        self.assertEqual(approved_product, u'公积金类')
        Index(self.selenium).click_user_list().click_user_quit()





        # 风控专员提交合同
        TotalFlow(self.selenium).submit_sign_page(self.risk_management, self.customer_name, self.bank_number)
        status3 = LoanList(self.selenium).get_loan_status(self.customer_name)
        self.assertEqual(status3, u'合同审核中')
        approved_product1 = LoanList(self.selenium).get_approved_product(self.customer_name)
        self.assertEqual(approved_product1, u'公积金类')
        Index(self.selenium).click_user_list().click_user_quit()
        # 合同专员审核
        TotalFlow(self.selenium).loan_sign_page(self.loan_manager, self.customer_name)
        status4 = ContractList(self.selenium).get_loan_status(self.customer_name)
        self.assertEqual(status4, u'放款中')
        Index(self.selenium).click_user_list().click_user_quit()
        # 上标专员审核
        TotalFlow(self.selenium).super_script_flow(self.super_script_manager, self.customer_name, self.project_number)
        Index(self.selenium).click_user_list().click_user_quit()
        # 合同专员放款
        TotalFlow(self.selenium).make_loan_sign_page(self.loan_manager, self.customer_name)
        status6 = ContractList(self.selenium).get_loan_status(self.customer_name)
        self.assertEqual(status6, u'已放款')
        Index(self.selenium).click_user_list().click_user_quit()

    def tearDown(self):
        super(TestTotalFlow, self).tearDown()
        customer_id = select_customer(self.customer_name)['id']
        clear_credit_report(customer_id)
        clear_info_verify(customer_id)
        clear_contract(customer_id)
        clear_sign_page(customer_id)
        clear_customer(customer_id)
