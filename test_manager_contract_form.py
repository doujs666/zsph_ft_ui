# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.manager_contract_form import ManagerContractForm
from utilities.my_sql import select_customer, update_manager_contract_form, get_manager_contract_form
import time


class TestContractForm(BaseSeleniumTestCase):
    login_name = 'gesy'
    password = 'admin'
    name = u'张十一博'
    loan_type = '4'
    rate = '2.39'
    cycle = '36'
    actual_quota = '50000.0'
    remarks = u'备注'

    def test_contract_form_save_success(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        # 验证借款状态
        contract_label = ManagerContractForm(self.selenium, [get_customer_id]).contract_label()
        self.assertEqual(contract_label, u'复核中')
        ManagerContractForm(self.selenium, [get_customer_id]).contract_form(self.loan_type, self.rate, self.cycle,
                                                                            self.actual_quota, self.remarks)
        # 验证决策时间
        decision_date = ManagerContractForm(self.selenium, [get_customer_id]).decision_date()
        get_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.assertEqual(decision_date, get_time)
        # 验证数据库存储
        db_type = get_manager_contract_form(get_customer_id)['type']
        self.assertEqual(db_type, self.loan_type)
        db_rate = str(get_manager_contract_form(get_customer_id)['rate'])
        self.assertEqual(db_rate, self.rate)
        db_cycle = str(get_manager_contract_form(get_customer_id)['cycle'])
        self.assertEqual(db_cycle, self.cycle)
        db_actual_quota = str(get_manager_contract_form(get_customer_id)['actual_quota'])
        self.assertEqual(db_actual_quota, self.actual_quota)
        # 验证信审主管
        commissioner_name = ManagerContractForm(self.selenium, [get_customer_id]).governor_name()
        self.assertEqual(commissioner_name, u'戈思雨')

    # 验证审核通过状态
    def test_manager_contract_form_pass(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        # 验证借款状态
        ManagerContractForm(self.selenium, [get_customer_id]).contract_form(self.loan_type, self.rate, self.cycle,
                                                                            self.actual_quota, self.remarks)
        contract_label = ManagerContractForm(self.selenium,
                                             [get_customer_id]).contract_form_submit_pass().contract_label()
        self.assertEqual(contract_label, u'待签约')

    # 验证审核驳回
    def test_manager_contract_form_reject(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        # 验证借款状态
        ManagerContractForm(self.selenium, [get_customer_id]).contract_form(self.loan_type, self.rate, self.cycle,
                                                                            self.actual_quota, self.remarks)
        contract_label = ManagerContractForm(self.selenium,
                                             [get_customer_id]).contract_form_submit_reject().contract_label()
        self.assertEqual(contract_label, u'补充资料')

    # 验证审核驳回
    def test_manager_contract_form_reject_commissioner(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        # 验证借款状态
        ManagerContractForm(self.selenium, [get_customer_id]).contract_form(self.loan_type, self.rate, self.cycle,
                                                                            self.actual_quota, self.remarks)
        contract_label = ManagerContractForm(self.selenium,
                                             [
                                                 get_customer_id]).contract_form_submit_reject_commissioner().contract_label()
        self.assertEqual(contract_label, u'审批中')

    # 验证实地征信
    def test_manager_contract_form_field_reference(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        # 验证借款状态
        ManagerContractForm(self.selenium, [get_customer_id]).contract_form(self.loan_type, self.rate, self.cycle,
                                                                            self.actual_quota, self.remarks)
        contract_label = ManagerContractForm(self.selenium,
                                             [
                                                 get_customer_id]).contract_form_submit_field_reference().contract_label()
        self.assertEqual(contract_label, u'实地征信')

    # 验证审核拒绝
    def test_manager_contract_form_repulse(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        # 验证借款状态
        ManagerContractForm(self.selenium, [get_customer_id]).contract_form(self.loan_type, self.rate, self.cycle,
                                                                            self.actual_quota, self.remarks)
        contract_label = ManagerContractForm(self.selenium,
                                             [get_customer_id]).contract_form_submit_repulse().contract_label()
        self.assertEqual(contract_label, u'拒绝')

    def tearDown(self):
        super(TestContractForm, self).tearDown()
        customer_id = select_customer(self.name)['id']
        update_manager_contract_form(customer_id)
