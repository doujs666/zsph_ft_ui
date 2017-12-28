# coding=UTF-8
from page.base_page import BasePage
import time


class LoanList(BasePage):
    # 销售管理

    url = '/loan/list'

    def loan_amount(self):
        message = self.find_element_by_css('.s_tabnum.flt').text
        time.sleep(0.5)
        return message

    # 点击查看按钮
    def click_examine_button(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        ret = []
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[0].text, 'detail': tds[12].text}
                if u'查看' in val['detail']:
                    ret.append(val['name'])
        index = ret.index(user_name)
        handel = self.find_elements_by_css('.handle')
        handel[index].click()
        return self

    # 获取借款状态
    def get_loan_status(self, user_name):
        time.sleep(1)
        rows = self.find_elements_by_css('.table tbody tr')
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[0].text, 'detail': tds[-2].text}
                if user_name == val['name']:
                    return val['detail']

    # 获取借款状态
    def get_approved_product(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[0].text, 'approved_product': tds[-6].text}
                if user_name == val['name']:
                    return val['approved_product']

