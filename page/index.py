# coding=UTF-8
from page.base_page import BasePage
import time


class Index(BasePage):

    url = '?login'

    # 点击客户管理
    def click_customer_manage(self):
        self.find_element_by_xpath('//*[@id="header"]/div/div/div/div/ul/li[3]/a/span').click()
        time.sleep(0.5)
        return self

    # 点击用户头像
    def click_user_list(self):
        self.find_element_by_css('.nav-link.navbar-avatar.waves-effect.waves-light.waves-round').click()
        time.sleep(1)
        return self

    # 点击用户退出登录
    def click_user_quit(self):
        self.find_element_by_css('.icon.md-power').click()
        time.sleep(0.5)
        return self



