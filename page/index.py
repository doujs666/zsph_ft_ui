# coding=UTF-8
from page.base_page import BasePage
import time

class Index(BasePage):

    url = '?login'

    def click_customer_manage(self):
        self.find_element_by_xpath('//*[@id="header"]/div/div/div/div/ul/li[3]/a/span').click()
        time.sleep(0.5)
        return self




