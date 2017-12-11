# coding=UTF-8
from page.base_page import BasePage
import time


class CustomerList(BasePage):
    # 客户列表

    url = '/customer/list'

    # 点击新增正式客户按钮
    def click_new_customer(self):
        self.find_element_by_css('.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 查看并切换句柄
    def get_customer_window_handle(self):
        handle = self.get_current_window_handle()
        return handle

    def get_customer_window_handles(self):
        handles = self.get_window_handles()
        return handles



