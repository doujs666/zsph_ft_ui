# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.job_form import CustomerJob
from utilities.my_sql import select_customer, customer_job


class TestCustomerJob(BaseSeleniumTestCase):
    user_name = 'gaohf'
    password = 'admin'
    name = u'测试用户'
    corporation = u'测试公司名称'
    department = u'测试部门'
    position = u'测试职位'
    tel_zone = '010'
    tel = '9438428'
    address = u'测试地址'

    def test_customer_job_name(self):
        TestPage(self.selenium).console_login(self.user_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        message = CustomerJob(self.selenium, [get_customer_id]).click_job_save().customer_job_name_error()
        self.assertEqual(message, u'此值不能为空')

    def test_customer_job_tel_zone(self):
        TestPage(self.selenium).console_login(self.user_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        message = CustomerJob(self.selenium, [get_customer_id]).click_job_save().customer_job_tel_zone_error()
        self.assertEqual(message, u'此值不能为空')

    def test_customer_job_tel(self):
        TestPage(self.selenium).console_login(self.user_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        message = CustomerJob(self.selenium, [get_customer_id]).click_job_save().customer_job_tel_error()
        self.assertEqual(message, u'此值不能为空')

    def test_customer_job_address(self):
        TestPage(self.selenium).console_login(self.user_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        message = CustomerJob(self.selenium, [get_customer_id]).click_job_save().customer_job_address()
        self.assertEqual(message, u'此值不能为空')

    def test_customer_job_v_success(self):
        TestPage(self.selenium).console_login(self.user_name, self.password)
        get_customer_id = select_customer(self.name)['id']
        CustomerJob(self.selenium, [get_customer_id]).customer_job(self.corporation, self.department, self.position,
                                                                   self.tel_zone, self.tel, self.address)
        customer_id = select_customer(self.name)['id']
        detail = customer_job(customer_id)
        # 工作名称
        db_job_name = detail['name']
        self.assertEqual(db_job_name, self.corporation)
        # 工作电话
        db_job_tel_zone = detail['tel_zone']
        self.assertEqual(db_job_tel_zone, self.tel_zone)
        db_job_tel = detail['tel']
        self.assertEqual(db_job_tel, self.tel)
        # 部门
        db_job_department = detail['department']
        self.assertEqual(db_job_department, self.department)
        # 职位
        db_job_position = detail['position']
        self.assertEqual(db_job_position, self.position)
        # 地址
        db_job_address = detail['addr']
        self.assertEqual(db_job_address, self.address)
