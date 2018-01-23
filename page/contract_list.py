# coding=UTF-8
from page.base_page import BasePage
import time


class ContractList(BasePage):
    # 合同列表

    url = '/contract/list'

    # 点击查看按钮
    def click_examine_button(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        ret = []
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[0].text, 'detail': tds[-1].text}
                if u'查看' in val['detail']:
                    ret.append(val['name'])
        index = ret.index(user_name)
        handel = self.find_elements_by_css('.handle')
        handel[index].click()
        return self

    # 获取借款状态
    def get_loan_status(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[2].text, 'detail': tds[-4].text}
                if user_name == val['name']:
                    return val['detail']

    # 获取处理状态
    def get_manage_status(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[2].text, 'approved_product': tds[-2].text}
                if user_name == val['name']:
                    return val['approved_product']

