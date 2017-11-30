# coding=UTF-8
from base import BaseSeleniumTestCase
from page.total_flow import TotalFlow
from page.loan_list import LoanList
from page.index import Index
from utilities.my_sql import select_customer, clear_customer, clear_credit_report, clear_info_verify


class TestTotalFlow(BaseSeleniumTestCase):
    # 风控专员审核通过
    risk_management = 'gaohf'
    judge_manager = 'zhangb'
    credit_person = 'wanqh'
    name = u'张十一博'
    card_no = '340827198311170460'
    mobile = '13522241003'
    status = 'pass'

    def test_loan_status(self):
        TotalFlow(self.selenium).risk_management_new_customer(self.name, self.card_no, self.mobile)
        status = LoanList(self.selenium).get_loan_status(self.name, self.risk_management)
        self.assertEqual(status, u'待审核')
        Index(self.selenium).click_user_list().click_user_quit()
        TotalFlow(self.selenium).judge_manager_allocation_role(self.name)
        status1 = LoanList(self.selenium).get_loan_status(self.name, self.judge_manager)
        self.assertEqual(status1, u'审批中')
        Index(self.selenium).click_user_list().click_user_quit()
        TotalFlow(self.selenium).risk_management_submit_audit(self.name, self.status)

    def tearDown(self):
        super(TestTotalFlow, self).tearDown()
        customer_id = select_customer(self.name)['id']
        clear_credit_report(customer_id)
        clear_info_verify(customer_id)
        clear_customer(customer_id)
