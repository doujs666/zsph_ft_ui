# coding=UTF-8
from page.base_page import BasePage
from page.test_page import TestPage
from page.loan_sign_page import LoanSignPage
from page.customer_from import CustomerFrom
from page.job_form import CustomerJob
from page.linkman_form import CustomerLinkman
from page.loan_form import CustomerLoan
from page.credit_audit_loan_list import CreditAuditLoanList
from utilities.my_sql import select_customer
from page.credit_report import CreditReport
from page.info_verify_net import InfoVerifyNet
from page.info_verify_tel import InfoVerifyTel
from page.certificates_review import CertificatesReview
from page.contract_form import ContractForm
from page.sign_page import SignPage
from page.manager_contract_form import ManagerContractForm
from page.super_script import SuperScript
import random


class TotalFlow(BasePage):
    risk_management = 'tianl'
    judge_manager = 'zhangb'
    credit_person = 'sunf'
    password = 'admin'
    url = '?login'

    # 新建用户
    def risk_management_new_customer(self, login_name, customer_name, card_no, mobile):
        TestPage(self.selenium).console_login(login_name, self.password)
        CustomerFrom(self.selenium).new_customer(customer_name, card_no, mobile, 24, '281545444@qq.com', 200000)
        # get_customer_id = select_customer(customer_name)['id']
        # CustomerJob(self.selenium, [get_customer_id]).customer_job(u'测试公司名称', u'测试部门', u'测试职位',
        #                                                            '010', '5438409', u'测试地址')
        # CustomerLinkman(self.selenium, [get_customer_id]).linkman(u'测试联系人姓名', u'工作单位', u'测试地址',
        #                                                           u'测试职位', '17600719709')

     # 风控专员提交
    def risk_management_submit(self, login_name, customer_name):
        type_number = str(random.randint(1, 4))
        cycle_number = str((random.randint(1, 3)) * 12)
        get_customer_id = select_customer(customer_name)['id']
        TestPage(self.selenium).console_login(login_name, self.password)
        CustomerLoan(self.selenium, [get_customer_id]).customer_loan_save(type_number, 10000, cycle_number, 100)
        CustomerLoan(self.selenium, [get_customer_id]).customer_loan_submit()

    # 经理分配角色
    def judge_manager_allocation_role(self, login_name, customer_name):
        TestPage(self.selenium).console_login(login_name, self.password)
        CreditAuditLoanList(self.selenium).allocation_role(customer_name)

    # 得到登录名
    def get_login_name(self, login_name, customer_name):
        TestPage(self.selenium).console_login(login_name, self.password)
        get_login_name = CreditAuditLoanList(self.selenium).get_login_name(customer_name)
        return get_login_name

    # 信审专员审核
    def risk_management_other(self, login_name, customer_name):
        TestPage(self.selenium).console_login(login_name, self.password)
        get_customer_id = select_customer(customer_name)['id']
        # CreditReport(self.selenium, [get_customer_id]).credit_report(6, 3000, 4000, 5000, 6000, 7000)
        # InfoVerifyNet(self.selenium, [get_customer_id]).info_verify(u'网核信息')
        # InfoVerifyTel(self.selenium, [get_customer_id]).info_verify(u'电核信息')

    def risk_management_submit_audit(self, login_name, customer_name, status):
        TestPage(self.selenium).console_login(login_name, self.password)
        get_customer_id = select_customer(customer_name)['id']
        ContractForm(self.selenium, [get_customer_id]).contract_form('1', '2.39', '24', '20000', u'备注')
        if status == 'pass':
            ContractForm(self.selenium, [get_customer_id]).contract_form_submit_pass()
        elif status == 'reject':
            ContractForm(self.selenium, [get_customer_id]).contract_form_submit_reject()
        else:
            ContractForm(self.selenium, [get_customer_id]).contract_form_submit_repulse()

    # 信审主管审核
    def manager_contract_form(self, login_name, customer_name, approved_product, status):
        TestPage(self.selenium).console_login(login_name, self.password)
        get_customer_id = select_customer(customer_name)['id']
        ManagerContractForm(self.selenium, [get_customer_id]).contract_form(approved_product, '2.39', '36', '100000',
                                                                            u'备注')
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

    # 风控专员填写合同
    def submit_sign_page(self, login_name, customer_name, bank_number):
        TestPage(self.selenium).console_login(login_name, self.password)
        get_customer_id = select_customer(customer_name)['id']
        SignPage(self.selenium, [get_customer_id]).sign_page_flow(bank_number)

    # 合同专员审核合同
    def loan_sign_page(self, login_name, customer_name):
        TestPage(self.selenium).console_login(login_name, self.password)
        get_customer_id = select_customer(customer_name)['id']
        LoanSignPage(self.selenium, [get_customer_id]).click_apply_button().choose_pass().click_submit_button()

    # 上标专员审核
    def super_script_flow(self, login_name, customer_name, project_no):
        TestPage(self.selenium).console_login(login_name, self.password)
        get_customer_id = select_customer(customer_name)['id']
        SuperScript(self.selenium, [get_customer_id]).super_script_flow(project_no)

    # 合同专员放款
    def make_loan_sign_page(self, login_name, customer_name):
        TestPage(self.selenium).console_login(login_name, self.password)
        get_customer_id = select_customer(customer_name)['id']
        LoanSignPage(self.selenium, [get_customer_id]).click_apply_button().click_submit_button()

    # 复议
    def certificates_flow(self, login_name, customer_name):
        TestPage(self.selenium).console_login(login_name, self.password)
        get_customer_id = select_customer(customer_name)['id']
        CertificatesReview(self.selenium, [get_customer_id]).review_flow()
