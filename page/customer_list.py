# coding=UTF-8
from page.base_page import BasePage
import time


class CustomerList(BasePage):
    # 客户列表

    url = '/customer/list'

    def click_new_customer(self):
        self.find_element_by_css('.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

