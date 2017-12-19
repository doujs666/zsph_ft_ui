# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.loan_sign_page import LoanSignPage
from utilities.my_sql import select_customer, clear_sign_page, get_loan_id


class TestSignPage(BaseSeleniumTestCase):
    login_name = 'zhangy'
    password = 'admin'
    name = u'测试合同审核'

    # 验证生成的合同名称
    def test_click_generate_after(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        db_get_loan_id = get_loan_id(get_customer_id)['id']
        print type(get_customer_id), type(db_get_loan_id)
        rel = LoanSignPage(self.selenium, [db_get_loan_id][get_customer_id]).get_contract_status()
        list = [u'电子签章使用授权书', u'借款协议', u'借款服务协议', u'咨询及管理服务协议', u'授权委托书', u'委托扣款授权书', u'还款管理服务说明书']
        self.assertEqual(rel, list)

    # 验证提交后合同状态
    def test_submit_contract_status(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        db_get_loan_id = get_loan_id(get_customer_id)['id']
        LoanSignPage(self.selenium, [db_get_loan_id][get_customer_id]).click_apply_button().choose_pass()


    # def tearDown(self):
    #     super(TestSignPage, self).tearDown()
    #     customer_id = select_customer(self.name)['id']
    #     clear_sign_page(customer_id)
