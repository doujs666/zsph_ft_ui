# coding=UTF-8
from page.base_page import BasePage
import time


class HistoricalList(BasePage):
    # 信审历史工单

    url = '/historical/list'

    # 获取借款状态
    def get_loan_status(self, user_name, login_name):
        time.sleep(2)
        rows = self.find_elements_by_css('.table tbody tr')
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val1 = {'name': tds[0].text, 'detail': tds[-2].text}
                if user_name == val1['name']:
                    return val1['detail']

    # 获取批核产品
    def get_approved_product(self, user_name, login_name):
        time.sleep(2)
        rows = self.find_elements_by_css('.table tbody tr')
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                if login_name != 'zhangb':
                    val = {'name': tds[0].text, 'approved_product': tds[-6].text}
                    if user_name == val['name']:
                        return val['approved_product']
                else:
                    val1 = {'name': tds[1].text, 'approved_product': tds[-6].text}
                    if user_name == val1['name']:
                        return val1['approved_product']


