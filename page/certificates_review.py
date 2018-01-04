# coding=UTF-8
from page.base_page import BasePage
from selenium.webdriver.support.ui import Select
import time


class CertificatesReview(BasePage):
    # 复议信息
    url = '/certificates/list/F?customer.id={}'

    # 点击复议按钮
    def click_review_button(self):
        self.find_element_by_id('reconsider').click()
        time.sleep(0.5)
        return self

    # 点击确定按钮
    def click_confirm_button(self):
        self.find_element_by_id('applySub').click()
        time.sleep(0.5)
        return self

    # 流程
    def review_flow(self):
        self.click_review_button()
        self.click_confirm_button()