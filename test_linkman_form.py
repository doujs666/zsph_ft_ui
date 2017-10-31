# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.linkman_from import CustomerLinkman
from utilities.my_sql import select_customer


class TestNewCustomer(BaseSeleniumTestCase):
    user_name = 'gaohf'
    password = 'gaohf'
    name = u'测试用户'
    corporation = u'测试公司名称'
    department = u'测试部门'
    position = u'测试职位'
    tel_zone = '010'
    tel = '9438428'
    address = u'测试地址'

    def test_customer_linkman_name(self):
        TestPage(self.selenium).console_login(self.user_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        message = CustomerLinkman(self.selenium, [get_customer_id]).click_linkman_save().linkman_name_error()
        self.assertEqual(message, u'此值不能为空')

    def test_customer_linkman_tel(self):
        TestPage(self.selenium).console_login(self.user_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        message = CustomerLinkman(self.selenium, [get_customer_id]).click_linkman_save().customer_linkman_tel_error()
        self.assertEqual(message, u'此值不能为空')



