# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.linkman_form import CustomerLinkman
from utilities.my_sql import select_customer, customer_linkman


class TestCustomerLink(BaseSeleniumTestCase):
    user_name = 'gaohf'
    password = 'admin'
    type_name = u'测试用户'
    name = u'测试用户类型'
    position = u'测试职位'
    tel = '17600719709'
    address = u'测试地址'
    work_unit = u'工作单位'

    def test_customer_linkman_name(self):
        TestPage(self.selenium).console_login(self.type_name, self.password)
        get_customer_id = select_customer(self.type_name)['id']
        message = CustomerLinkman(self.selenium, [get_customer_id]).click_linkman_save().customer_linkman_name_error()
        self.assertEqual(message, u'此值不能为空')

    def test_customer_linkman_tel(self):
        TestPage(self.selenium).console_login(self.user_name, self.password)
        get_customer_id = select_customer(self.type_name)['id']
        message = CustomerLinkman(self.selenium, [get_customer_id]).click_linkman_save().customer_linkman_tel_error()
        self.assertEqual(message, u'此值不能为空')

    def test_customer_linkman_v_success(self):
        TestPage(self.selenium).console_login(self.user_name, self.password)
        get_customer_id = select_customer(self.type_name)['id']
        CustomerLinkman(self.selenium, [get_customer_id]).customer_linkman(self.name, self.tel, self.work_unit, self.address, self.position)
        customer_id = select_customer(self.type_name)['id']
        detail = customer_linkman(customer_id)
        # 工作名称
        db_linkman_name = detail['name']
        self.assertEqual(db_linkman_name, self.name)
        # 工作电话
        # db_linkman_tel = detail['tel']
        # self.assertEqual(db_linkman_tel, self.tel)
        # 职位
        db_linkman_position = detail['position']
        self.assertEqual(db_linkman_position, self.position)
        # 地址
        db_linkman_address = detail['addr']
        self.assertEqual(db_linkman_address, self.address)
        # 工作单位
        db_linkman_work_unit = detail['work_unit']
        self.assertEqual(db_linkman_work_unit, self.work_unit)
