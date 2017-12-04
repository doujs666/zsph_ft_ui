# coding=UTF-8
from page.base_page import BasePage
from page.test_page import TestPage
from page.index import Index
from page.customer_list import CustomerList
from page.customer_from import CustomerFrom
from page.job_form import CustomerJob
from page.linkman_form import CustomerLinkman
from page.loan_form import CustomerLoan
from page.loan_list import LoanList
from utilities.my_sql import select_customer
from page.credit_report import CreditReport
from page.info_verify_net import InfoVerifyNet
from page.info_verify_tel import InfoVerifyTel
from page.contract_form import ContractForm
from page.manager_contract_form import ManagerContractForm
import random


class TotalFlow(BasePage):
    risk_management = 'gaohf'
    judge_manager = 'zhangb'
    credit_person = 'wanqh'

    password = 'admin'
    url = '?login'

    # 新建用户
    def risk_management_new_customer(self, name, card_no, mobile):
        TestPage(self.selenium).console_login(self.risk_management, self.password)
        Index(self.selenium).click_customer_manage()
        CustomerList(self.selenium).click_new_customer()
        CustomerFrom(self.selenium).new_customer(name, card_no, mobile, 24, '281545444@qq.com', 200000)
        get_customer_id = select_customer(name)['id']
        CustomerJob(self.selenium, [get_customer_id]).customer_job(u'测试公司名称', u'测试部门', u'测试职位',
                                                                   '010', '5438438', u'测试地址')
        CustomerLinkman(self.selenium, [get_customer_id]).linkman(u'测试联系人姓名', u'工作单位', u'测试地址',
                                                                  u'测试职位', '17600719709')
        type_number = str(random.randint(1, 6))
        cycle_number = str((random.randint(1, 3)) * 12)
        CustomerLoan(self.selenium, [get_customer_id]).customer_loan_save(type_number, 10000, cycle_number, 100)
        CustomerLoan(self.selenium, [get_customer_id]).customer_loan_submit()

    # 经理分配角色
    def judge_manager_allocation_role(self, name):
        TestPage(self.selenium).console_login(self.judge_manager, self.password)
        LoanList(self.selenium).allocation_role(name)

    # 信审专员审核
    def risk_management_submit_audit(self, name, status):
        TestPage(self.selenium).console_login(self.credit_person, self.password)
        get_customer_id = select_customer(name)['id']
        CreditReport(self.selenium, [get_customer_id]).credit_report(6, 3000, 4000, 5000, 6000, 7000)
        InfoVerifyNet(self.selenium, [get_customer_id]).info_verify(u'网核信息')
        InfoVerifyTel(self.selenium, [get_customer_id]).info_verify(u'电核信息')
        ContractForm(self.selenium, [get_customer_id]).contract_form('1', '2.39', '24', '20000', u'备注')
        if status == 'pass':
            ContractForm(self.selenium, [get_customer_id]).contract_form_submit_pass()
        elif status == 'reject':
            ContractForm(self.selenium, [get_customer_id]).contract_form_submit_reject()
        else:
            ContractForm(self.selenium, [get_customer_id]).contract_form_submit_repulse()

    # 信审主管审核
    def manager_contract_form(self, login_name, name, status):
        TestPage(self.selenium).console_login(login_name, self.password)
        get_customer_id = select_customer(name)['id']
        ManagerContractForm(self.selenium, [get_customer_id]).contract_form('4', '2.39', '36', '100000', u'备注')
        if status == 'pass':
            ManagerContractForm(self.selenium,
                                [get_customer_id]).contract_form_submit_pass()
        if status == 'reject':
            ManagerContractForm(self.selenium,
                                [get_customer_id]).contract_form_submit_reject()
        if status == 'reject_commissioner':
            ManagerContractForm(self.selenium,
                                [get_customer_id]).contract_form_submit_reject_commissioner()
        if status == 'field_reference':
            ManagerContractForm(self.selenium,
                                [get_customer_id]).contract_form_submit_field_reference()
        if status == 'repulse':
            ManagerContractForm(self.selenium,
                                [get_customer_id]).contract_form_submit_repulse()