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
import random


class TotalFlow(BasePage):

    risk_management = 'gaohf'
    judge_manager = 'zhangb'
    password = 'admin'
    name = u'测试流程'
    card_no = '640105197303265646'
    mobile = '13651020524'
    corporation = u'测试公司名称'
    department = u'测试部门'
    position = u'测试职位'
    tel_zone = '010'
    tel = '9438428'
    address = u'测试地址'
    tel = '17600719709'
    url = '?login'

    # 新建用户
    def risk_management_new_customer(self):
        TestPage(self.selenium).console_login(self.risk_management, self.password)
        Index(self.selenium).click_customer_manage()
        CustomerList(self.selenium).click_new_customer()
        CustomerFrom(self.selenium).new_customer(self.name, self.card_no, self.mobile, 24, '281545444@qq.com',
                                                 200000)
        get_customer_id = select_customer(self.name)['id']
        CustomerJob(self.selenium, [get_customer_id]).customer_job(u'测试公司名称', u'测试部门', u'测试职位',
                                                                   '010', '5438438', u'测试地址')
        CustomerLinkman(self.selenium, [get_customer_id]).linkman(u'测试联系人姓名', u'工作单位', u'测试地址',
                                                                  u'测试职位', '17600719709')
        type_number = str(random.randint(1, 6))
        cycle_number = str((random.randint(1, 3)) * 12)
        CustomerLoan(self.selenium, [get_customer_id]).customer_loan(type_number, 10000, cycle_number,
                                                                     100)

    # 经理分配角色
    def judge_manager_allocation_role(self):
        TestPage(self.selenium).console_login(self.judge_manager, self.password)
        LoanList(self.selenium).allocation_role(self.name)