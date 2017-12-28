# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.loan_sign_page import LoanSignPage
from page.contract_list import ContractList
from utilities.my_sql import select_customer,clear_contract_loan_status


class TestLoanSignPage(BaseSeleniumTestCase):
    login_name = 'zhangy'
    password = 'admin'
    name = u'测试合同审核'

    # 验证生成的合同名称
    def test_click_generate_after(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        rel = LoanSignPage(self.selenium, [get_customer_id]).get_contract_status()
        list = [u'电子签章使用授权书', u'借款服务协议', u'咨询及管理服务协议', u'授权委托书', u'委托扣款授权书', u'还款管理服务说明书']
        self.assertEqual(rel, list)

    # 验证审核通过合同状态
    def test_submit_pass_contract_status(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        LoanSignPage(self.selenium, [get_customer_id]).click_apply_button().choose_pass().click_submit_button()
        message = LoanSignPage(self.selenium, [get_customer_id]).get_button_text()
        self.assertEqual(message, u'放款')
        loan_status = ContractList(self.selenium).get_loan_status(self.name)
        self.assertEqual(loan_status, u'放款中')

    # 验证审核拒绝合同状态
    def test_submit_contract_status(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        LoanSignPage(self.selenium, [get_customer_id]).click_apply_button().choose_reject().click_submit_button()
        db_contract_status = select_customer(self.name)['apply_state']
        self.assertEqual(db_contract_status, '25')

    # 验证放款后合同状态
    def test_credit_contract_status(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        LoanSignPage(self.selenium, [get_customer_id]).click_apply_button().choose_pass().click_submit_button()
        LoanSignPage(self.selenium, [get_customer_id]).click_apply_button().click_submit_button()
        new_loan_status = ContractList(self.selenium).get_loan_status(self.name)
        self.assertEqual(new_loan_status, u'已放款')


    def tearDown(self):
        super(TestLoanSignPage, self).tearDown()
        customer_id = select_customer(self.name)['id']
        clear_contract_loan_status(customer_id)

