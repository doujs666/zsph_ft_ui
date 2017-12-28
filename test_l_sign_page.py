# coding=UTF-8
from base import BaseSeleniumTestCase
from page.loan_list import LoanList
from page.test_page import TestPage
from page.sign_page import SignPage
import time
from utilities.my_sql import select_customer, clear_sign_page, get_sign_flag


class TestSignPage(BaseSeleniumTestCase):
    login_name = 'gaohf'
    password = 'admin'
    name = u'江丹彤'
    url = 'https://fht.fuiou.com/api_contractAPP.do'
    bank_number = '6215590200000919787'
    verification_code = '999999'

    # 验证点击富有认证是否跳转url
    def test_button_if_exist(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        get_url = SignPage(self.selenium, [get_customer_id]).click_fuyou_button().get_current_page_url()
        self.assertEqual(get_url, self.url)

    # 点击保存之后验证生成按钮
    def test_click_save_button_after(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        SignPage(self.selenium, [get_customer_id]).account_number(self.bank_number).click_save_button()
        self.assertEqual(True, SignPage(self.selenium, [get_customer_id]).fuyou_button_if_exist())

    # 验证生成的合同名称
    def test_click_generate_after(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        SignPage(self.selenium, [get_customer_id]).create_contract_flow(self.bank_number)
        rel = SignPage(self.selenium, [get_customer_id]).get_contract_status()
        list = [u'电子签章使用授权书', u'借款协议', u'借款服务协议', u'咨询及管理服务协议', u'授权委托书', u'委托扣款授权书', u'还款管理服务说明书']
        self.assertEqual(rel, list)

    # 签约验证
    def test_sign_after(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        SignPage(self.selenium, [get_customer_id]).create_contract_flow(self.bank_number)
        SignPage(self.selenium, [get_customer_id]).sign_flow(self.verification_code)
        time.sleep(1)
        sign_flag = int(get_sign_flag(get_customer_id)['sign_flag'])
        self.assertEqual(sign_flag, 1)

    # 提交验证
    def test_after_click_apply_button(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        SignPage(self.selenium, [get_customer_id]).create_contract_flow(self.bank_number)
        SignPage(self.selenium, [get_customer_id]).sign_flow(self.verification_code)
        SignPage(self.selenium, [get_customer_id]).click_apply_button().new_click_apply_button()
        db_apply_state = int(select_customer(self.name)['apply_state'])
        self.assertEqual(db_apply_state, 30)
        get_loan_status = LoanList(self.selenium).get_loan_status(self.name)
        self.assertEqual(get_loan_status, u'合同审核中')

    def tearDown(self):
        super(TestSignPage, self).tearDown()
        customer_id = select_customer(self.name)['id']
        clear_sign_page(customer_id)
