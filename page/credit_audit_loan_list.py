# coding=UTF-8
from page.base_page import BasePage
import time


class CreditAuditLoanList(BasePage):
    # 信审专员工单

    url = '/creditAudit/creditLoan/list'

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

    # 点击分配按钮
    def click_allocation_button(self):
        time.sleep(1)
        self.find_element_by_id('distributionMore').click()
        time.sleep(1)
        return self

    # 选择角色
    def choose_role(self):
        self.find_element_by_xpath('//*[@id="list-group"]/li[1]').click()
        time.sleep(0.5)
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

    # 选择点击分配角色
    def click_allocation_role(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[1].text, 'detail': tds[-2].text}
                if user_name == val['name'] and u'待审核' == val['detail']:
                    self.find_element_by_name('id').click()
                    return self
        #           ret.append(val['name'])
        # index = ret.index(user_name)
        # handel = self.find_elements_by_css('.handle .rit')
        # handel[index].click()

    # 获取借款状态
    def get_loan_status(self, user_name, login_name):
        time.sleep(2)
        rows = self.find_elements_by_css('.table tbody tr')
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                if login_name != 'zhangb':
                    val = {'name': tds[0].text, 'detail': tds[-2].text}
                    if user_name == val['name']:
                        return val['detail']
                else:
                    val1 = {'name': tds[1].text, 'detail': tds[-2].text}
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

    # 获取登录名
    def get_login_name(self, user_name):
        time.sleep(1)
        rows = self.find_elements_by_css('.table tbody tr')
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[1].text, 'new_login_name': tds[4].text}
                if user_name == val['name']:
                    return val['new_login_name']

    # 分配角色流程
    def allocation_role(self, user_name):
        self.click_allocation_role(user_name).click_allocation_button().choose_role()
        return self

