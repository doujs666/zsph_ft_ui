# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.new_staff import NewStaff
from page.index import Index
from utilities.my_sql import clear_user_account


class TestNewStaff(BaseSeleniumTestCase):
    login_name = 'admin_hr'
    password = 'admin'
    new_login_name = u'zhangs'
    url = 'http://116.62.207.57/'

    # 验证选择否，是否可以登录
    def test_if_login(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        NewStaff(self.selenium).staff_flow(self.new_login_name, self.password).if_login('0').click_save_button()
        Index(self.selenium).click_user_list().click_user_quit()
        message = TestPage(self.selenium).console_login(self.new_login_name, self.password).get_login_error()
        self.assertEqual(message, u'该已帐号禁止登录.')

    # 正常登录
    def test_true_login(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        NewStaff(self.selenium).staff_flow(self.new_login_name, self.password).if_login(
            '1').click_save_button()
        Index(self.selenium).click_user_list().click_user_quit()
        url = TestPage(self.selenium).console_login(self.new_login_name, self.password).get_current_page_url()
        self.assertEqual(url, self.url)

    def tearDown(self):
        super(TestNewStaff, self).tearDown()
        clear_user_account(self.login_name)
