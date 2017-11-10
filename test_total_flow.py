# coding=UTF-8
from base import BaseSeleniumTestCase
from page.total_flow import TotalFlow
from page.loan_list import LoanList
from page.index import Index
from utilities.my_sql import select_customer,clear_customer


class TestTotalFlow(BaseSeleniumTestCase):

    name = u'测试流程'

    def test_loan_status(self):
        TotalFlow(self.selenium).risk_management_new_customer()
        status = LoanList(self.selenium).get_loan_status(self.name)
        self.assertEqual(status, u'待审核')
        Index(self.selenium).click_user_list().click_user_quit()
        TotalFlow(self.selenium).judge_manager_allocation_role()
        status1 = LoanList(self.selenium).get_loan_status(self.name)
        self.assertEqual(status1, u'审批中')

    def tearDown(self):
        super(TestTotalFlow, self).tearDown()
        customer_id = select_customer(self.name)['id']
        clear_customer(customer_id)