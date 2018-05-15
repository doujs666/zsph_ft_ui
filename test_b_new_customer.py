# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.index import Index
from page.customer_list import CustomerList
from page.customer_from import CustomerFrom
from utilities.my_sql import select_customer, customer_amount, clear_customer
import settings


class TestNewCustomer(BaseSeleniumTestCase):
    """新建客户"""

    user_name = 'gaohf'
    password = 'admin'
    name = u'测试用户'
    email = 'ceshiyouxiang@qq.com'
    card_no = '220281198210024497'
    mobile = '13522241003'
    tel_time = 24
    annual_income = 200000

    def test_new_customer_url(self):
        """测试url跳转"""
        TestPage(self.selenium).console_login(self.user_name, self.password)
        Index(self.selenium).click_customer_manage()
        # 校验跳转成功后url跳转
        CustomerList(self.selenium).click_new_customer()
        handles = CustomerList(self.selenium).get_window_handles()
        url = CustomerList(self.selenium).choose_window_handle(handles[2]).get_current_page_url()

        self.assertEqual(url, settings.WEB_TEST_BASE_URL + '/customer/form')

    def test_customer_name(self):
        """测试姓名"""
        TestPage(self.selenium).console_login(self.user_name, self.password)
        none_message = CustomerFrom(self.selenium).customer_card_no('').click_save().get_name_none_error()
        self.assertEqual(none_message, u'此值不能为空')

    def test_customer_mobile(self):
        """测试手机号"""
        TestPage(self.selenium).console_login(self.user_name, self.password)
        none_message = CustomerFrom(self.selenium).customer_card_no('').click_save().get_mobile_none_error_error()
        self.assertEqual(none_message, u'此值不能为空')

    def test_customer_card_no(self):
        """测试身份证号"""
        TestPage(self.selenium).console_login(self.user_name, self.password)
        message = CustomerFrom(self.selenium).customer_card_no('sdfd').get_card_no_error()
        self.assertEqual(message, u'身份证号码不合法')
        number_mix_message = CustomerFrom(self.selenium).customer_card_no('14020202').get_card_no_error()
        self.assertEqual(number_mix_message, u'身份证号码不合法')
        number_max_message = CustomerFrom(self.selenium).customer_card_no('140202021992121665511').get_card_no_error()
        self.assertEqual(number_max_message, u'身份证号码不合法')
        none_message = CustomerFrom(self.selenium).customer_card_no('').click_save().get_card_no_none_error()
        self.assertEqual(none_message, u'此值不能为空')

    def test_customer_email(self):
        """测试邮箱"""
        TestPage(self.selenium).console_login(self.user_name, self.password)
        message = CustomerFrom(self.selenium).customer_email('123').get_email_error()
        self.assertEqual(message, u'邮件地址不合法')
        format_message = CustomerFrom(self.selenium).customer_email('adfdqq.com').get_email_error()
        self.assertEqual(format_message, u'邮件地址不合法')
        none_message = CustomerFrom(self.selenium).customer_email('').click_save().get_email_none_error()
        self.assertEqual(none_message, u'此值不能为空')

    def test_customer_annual_income(self):
        """测试个人月收入"""
        TestPage(self.selenium).console_login(self.user_name, self.password)
        message = CustomerFrom(self.selenium).customer_annual_income('abc').get_annual_income_error()
        self.assertEqual(message, u'请输入数字可带小数')

    def test_new_customer_success(self):
        """测试新建客户"""
        db_customer_amount = customer_amount()
        TestPage(self.selenium).console_login(self.user_name, self.password)
        CustomerFrom(self.selenium).new_customer(self.name, self.card_no, self.mobile, self.tel_time, self.email,
                                                 self.annual_income)
        # db_mobile = select_customer(self.name)['mobile1']
        # self.assertEqual(db_mobile, self.mobile)
        db_card_no = select_customer(self.name)['card_no']
        self.assertEqual(db_card_no, self.card_no)
        db_annual_income = select_customer(self.name)['annual_income']
        self.assertEqual(db_annual_income, int(self.annual_income))
        db_email = select_customer(self.name)['email']
        self.assertEqual(db_email, self.email)
        # 验证customer数量
        new_customer_amount = customer_amount()
        self.assertEqual(db_customer_amount, new_customer_amount - 1)

        # clear数据
        customer_id = select_customer(self.name)['id']
        clear_customer(customer_id)

    # def tearDown(self):
    #     super(TestNewCustomer, self).tearDown()
    #     customer_id = select_customer(self.name)['id']
    #     clear_customer(customer_id)
