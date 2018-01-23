# coding=UTF-8
from page.base_page import BasePage
import time


class TestPage(BasePage):
    url = '/login'

    def input_user_name(self, user_name):
        self.find_element_by_name('username').send_keys(user_name)
        time.sleep(0.5)
        return self

    def input_password(self, password):
        self.find_element_by_name('password').send_keys(password)
        time.sleep(0.5)
        return self

    def login_submit(self):
        self.find_element_by_css('.btn.btn-primary.btn-block.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    def console_login(self, user_name, password):
        self.input_user_name(user_name).input_password(password)
        self.login_submit()
        return self

    def get_login_error(self):
        message = self.find_element_by_xpath('/html/body/div/div/div[2]/p').text
        return message