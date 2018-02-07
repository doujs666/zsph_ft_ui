# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.linkman_form import CustomerLinkman
from page.customer_from import CustomerFrom
from utilities.my_sql import select_customer, clear_customer_linkman, clear_customer


class TestCustomerLink(BaseSeleniumTestCase):

    '''联系人'''

    login_name = 'gaohf'
    password = 'admin'
    user_name = u'测试联系人'
    linkman_name = u'测试联系人姓名'
    position = u'测试职位'
    tel = '17600719709'
    address = u'测试地址'
    work_unit = u'工作单位'

    def setUp(self):
        super(TestCustomerLink, self).setUp()
        TestPage(self.selenium).console_login(self.login_name, self.password)
        CustomerFrom(self.selenium).new_customer(self.user_name, '220281198210024400', '13651020001', '2', '234567@qq.com',
                                                 20000)

    def test_customer_linkman_success(self):
        '''联系人'''
        get_customer_id = select_customer(self.user_name)['id']
        CustomerLinkman(self.selenium, [get_customer_id]).linkman(self.linkman_name, self.work_unit, self.address,
                                                                  self.position, self.tel)

    def tearDown(self):
        super(TestCustomerLink, self).tearDown()
        get_customer_id = select_customer(self.user_name)['id']
        clear_customer_linkman(get_customer_id)
        clear_customer(get_customer_id)
