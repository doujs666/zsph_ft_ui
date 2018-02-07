# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.index import Index
import settings


class TestConsoleLogin(BaseSeleniumTestCase):
    '''登录'''

    user_name = 'gaohf'
    password = 'admin'

    def test_console_login_successful(self):
        # 校验登录成功后url跳转
        after_login_url = TestPage(self.selenium).console_login(self.user_name, self.password).get_current_page_url()
        self.assertEqual(after_login_url, settings.WEB_TEST_BASE_URL + '/')

    # def test_login_failed(self):
    #     # 校验登录时用户名输入错误提示信息
    #     failed_message = TestPage(self.selenium).console_login(self.user_name+'i', self.password).get_login_error()
    #     self.assertEqual(failed_message, u'用户或密码错误, 请重试.')
    #
    #     # 校验登录时密码输入错误提示信息
    #     failed_message = TestPage(self.selenium).console_login(self.user_name , self.password + 'i').get_login_error()
    #     self.assertEqual(failed_message, u'用户或密码错误, 请重试.')
    #
    #     # 校验登录时手机号密码都输入错误提示信息
    #     failed_message = TestPage(self.selenium).console_login(self.user_name + 'i', self.password + 'i').get_login_error()
    #     self.assertEqual(failed_message, u'验证码错误, 请重试.')

    def test_login_quit(self):
        TestPage(self.selenium).console_login(self.user_name, self.password)
        Index(self.selenium).click_user_list().click_user_quit()






