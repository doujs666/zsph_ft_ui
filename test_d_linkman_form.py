# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.linkman_form import CustomerLinkman
from utilities.my_sql import select_customer, customer_linkman


class TestCustomerLink(BaseSeleniumTestCase):
    login_name = 'gaohf'
    password = 'admin'
    name = u'测试用户'
    linkman_name = u'测试联系人姓名'
    position = u'测试职位'
    tel = '17600719709'
    address = u'测试地址'
    work_unit = u'工作单位'

    def test_customer_linkman_success(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        CustomerLinkman(self.selenium, [get_customer_id]).linkman(self.linkman_name, self.work_unit, self.address,
                                                                  self.position, self.tel)
