# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.contract_form import ContractForm
from utilities.my_sql import select_customer, update_contract_form,get_contract_form,get_credit_person_login_name
import time


class TestContractForm(BaseSeleniumTestCase):
    # 验证信审专员信审结论
    password = 'admin'
    name = u'测试用户'
    loan_type = '2'
    rate = '2.18'
    cycle = '24'
    actual_quota = '20000.0'
    remarks = u'备注'

    def test_contract_form_save_success(self):
        # 获取信审专员
        get_customer_id = select_customer(self.name)['id']
        login_name = get_credit_person_login_name(get_customer_id)
        TestPage(self.selenium).console_login(login_name, self.password)
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
        db_audit_type = get_contract_form(get_customer_id)['audit_type']
        self.assertEqual(db_audit_type, self.loan_type)
        db_audit_rate = str(get_contract_form(get_customer_id)['audit_rate'])
        self.assertEqual(db_audit_rate, self.rate)
        db_audit_cycle = str(get_contract_form(get_customer_id)['audit_cycle'])
        self.assertEqual(db_audit_cycle, self.cycle)
        db_audit_actual_quota = str(get_contract_form(get_customer_id)['autid_actual_quota'])
        self.assertEqual(db_audit_actual_quota, self.actual_quota)

    # 验证审核通过状态
    def     test_contract_form_pass(self):
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
        status = ContractForm(self.selenium, [get_customer_id]).contract_form_submit_repulse().contract_label()
        self.assertEqual(status, u'拒绝')

    # 验证审核驳回
    def test_contract_form_reject(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        # 验证借款状态
        ContractForm(self.selenium, [get_customer_id]).contract_form(self.loan_type, self.rate, self.cycle,
                                                                     self.actual_quota, self.remarks)
        status = ContractForm(self.selenium, [get_customer_id]).contract_form_submit_reject().contract_label()
        self.assertEqual(status, u'补充资料')

    def tearDown(self):
        super(TestContractForm, self).tearDown()
        customer_id = select_customer(self.name)['id']
        update_contract_form(customer_id)

