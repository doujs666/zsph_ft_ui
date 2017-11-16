# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.contract_form import ContractForm
from utilities.my_sql import select_customer, update_contract_form,get_contract_form
import time


class TestContractForm(BaseSeleniumTestCase):
    login_name = 'wanqh'
    password = 'admin'
    name = u'测试用户'
    loan_type = '1'
    rate = '2.39'
    cycle = '24'
    actual_quota = '20000.0'
    remarks = u'备注'

    def test_contract_form_save_success(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        # 验证借款状态
        contract_label = ContractForm(self.selenium, [get_customer_id]).contract_label()
        self.assertEqual(contract_label, u'审批中')
        # 验证信审专员
        commissioner_name = ContractForm(self.selenium, [get_customer_id]).commissioner_name()
        self.assertEqual(commissioner_name, u'万秋红')
        ContractForm(self.selenium, [get_customer_id]).contract_form(self.loan_type, self.rate, self.cycle,
                                                                     self.actual_quota, self.remarks)
        # 验证决策时间
        decision_date = ContractForm(self.selenium, [get_customer_id]).decision_date()
        get_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.assertEqual(decision_date, get_time)
        # 验证数据库存储
        db_type = get_contract_form(get_customer_id)['type']
        self.assertEqual(db_type, self.loan_type)
        db_rate = str(get_contract_form(get_customer_id)['rate'])
        self.assertEqual(db_rate, self.rate)
        db_cycle = str(get_contract_form(get_customer_id)['cycle'])
        self.assertEqual(db_cycle, self.cycle)
        db_actual_quota = str(get_contract_form(get_customer_id)['actual_quota'])
        self.assertEqual(db_actual_quota, self.actual_quota)

    # 验证审核通过状态
    def test_contract_form_pass(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        # 验证借款状态
        ContractForm(self.selenium, [get_customer_id]).contract_form(self.loan_type, self.rate, self.cycle,
                                                                     self.actual_quota, self.remarks)
        contract_label = ContractForm(self.selenium, [get_customer_id]).contract_form_submit_pass().contract_label()
        self.assertEqual(contract_label, u'复核中')

    # 验证审核拒绝
    def test_contract_form_repulse(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        # 验证借款状态
        ContractForm(self.selenium, [get_customer_id]).contract_form(self.loan_type, self.rate, self.cycle,
                                                                     self.actual_quota, self.remarks)
        contract_label = ContractForm(self.selenium, [get_customer_id]).contract_form_submit_repulse().contract_label()
        self.assertEqual(contract_label, u'拒绝')

    # 验证审核驳回
    def test_contract_form_reject(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        # 验证借款状态
        ContractForm(self.selenium, [get_customer_id]).contract_form(self.loan_type, self.rate, self.cycle,
                                                                     self.actual_quota, self.remarks)
        contract_label = ContractForm(self.selenium, [get_customer_id]).contract_form_submit_reject().contract_label()
        self.assertEqual(contract_label, u'补充资料')

    def tearDown(self):
        super(TestContractForm, self).tearDown()
        customer_id = select_customer(self.name)['id']
        update_contract_form(customer_id)

