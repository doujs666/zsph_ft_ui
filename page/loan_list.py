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

    # 分配角色弹框关闭按钮
    def click_allocation_close(self):
        self.find_element_by_css(
            '.btn.btn-default.btn-pure.waves-effect.waves-classic.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 选择角色
    def choose_role(self):
        self.find_element_by_xpath('//*[@id="list-group"]/li[1]').click()
        return self

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

    # 点击分配角色
    def click_allocation_role(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        ret = []
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[0].text, 'detail': tds[10].text}
                if u'分配' in val['detail']:
                    ret.append(val['name'])
        index = ret.index(user_name)
        handel = self.find_elements_by_css('.handle .rit')
        handel[index].click()
        return self

    # 获取借款状态
    def get_loan_status(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        ret = []
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[0].text, 'detail': tds[-2].text}
                if user_name == val['name']:
                    return val['detail']

    # 分配角色流程
    def allocation_role(self, user_name):
        self.click_allocation_role(user_name).choose_role()
        return self

