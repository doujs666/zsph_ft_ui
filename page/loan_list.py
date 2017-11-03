# coding=UTF-8
from page.base_page import BasePage
import time


class LoanList(BasePage):
    # 销售列表

    url = '/loan/list'

    def loan_amount(self):
        message = self.find_element_by_css('.s_tabnum.flt').text
        time.sleep(0.5)
        return message

