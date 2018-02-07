# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.job_form import CustomerJob
from page.customer_from import CustomerFrom
from utilities.my_sql import select_customer, customer_job, clear_customer_job, clear_customer


class TestCustomerJob(BaseSeleniumTestCase):
    login_name = 'gaohf'
    password = 'admin'
    user_name = u'测试工作信息'
    corporation = u'测试公司名称'
    department = u'测试部门'
    position = u'测试职位'
    tel_zone = '010'
    tel = '9438428'
    address = u'测试地址'

    def setUp(self):
        super(TestCustomerJob, self).setUp()
        TestPage(self.selenium).console_login(self.login_name, self.password)
        CustomerFrom(self.selenium).new_customer(self.user_name, '220281198210024400', '13651020001', '2', '234567@qq.com',
                                                 20000)

    def test_customer_job_name(self):
        '''工作单位名称'''
        get_customer_id = select_customer(self.user_name)['id']
        message = CustomerJob(self.selenium, [get_customer_id]).click_job_save().customer_job_name_error()
        self.assertEqual(message, u'此值不能为空')

    def test_customer_job_tel_zone(self):
        '''工作电话区号'''
        get_customer_id = select_customer(self.user_name)['id']
        message = CustomerJob(self.selenium, [get_customer_id]).click_job_save().customer_job_tel_zone_error()
        self.assertEqual(message, u'此值不能为空')

    def test_customer_job_tel(self):
        '''工作电话号'''
        get_customer_id = select_customer(self.user_name)['id']
        message = CustomerJob(self.selenium, [get_customer_id]).click_job_save().customer_job_tel_error()
        self.assertEqual(message, u'此值不能为空')

    def test_customer_job_address(self):
        '''工作地址'''
        get_customer_id = select_customer(self.user_name)['id']
        message = CustomerJob(self.selenium, [get_customer_id]).click_job_save().customer_job_address()
        self.assertEqual(message, u'此值不能为空')

    def test_customer_job_v_success(self):
        '''测试工作信息'''
        get_customer_id = select_customer(self.user_name)['id']
        CustomerJob(self.selenium, [get_customer_id]).customer_job(self.corporation, self.department, self.position,
                                                                   self.tel_zone, self.tel, self.address)
        customer_id = select_customer(self.user_name)['id']
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

    def tearDown(self):
        super(TestCustomerJob, self).tearDown()
        get_customer_id = select_customer(self.user_name)['id']
        clear_customer_job(get_customer_id)
        clear_customer(get_customer_id)



