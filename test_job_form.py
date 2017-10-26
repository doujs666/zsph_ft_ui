# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.index import Index
from page.customer_list import CustomerList
from page.job_form import CustomerJob
from utilities.my_sql import clear_customer, select_customer, customer_amount
from page.customer_from import CustomerFrom
import time
import settings


class TestNewCustomer(BaseSeleniumTestCase):
    user_name = 'gaohf'
    password = 'gaohf'
    name = u'测试用户'
    work = u'测试工作地址'
    department = u'测试部门'
    position = u'测试职位'
    tel_zone = '010'
    tel = 9438428
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
        CustomerJob(self.selenium, [get_customer_id]).customer_job(self.work, self.department, self.position,
                                                                   self.tel_zone, self.tel, self.address)

    def test_customer_job_url(self):
        return '123'
