# coding=UTF-8
from page.base_page import BasePage
from selenium.webdriver.support.ui import Select
import time


class ManagerAllocation(BasePage):
    # 信审经理分配
    url = '/creditAudit/creditLoan/list'

    # 分配角色弹框关闭按钮
    def click_allocation_close(self):
        self.find_element_by_css(
            '.btn.btn-default.btn-pure.waves-effect.waves-classic.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 点击分配按钮
    def click_allocation_button(self):
        self.find_element_by_css(
            '.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic.waves-effect.waves-classic').click()
        time.sleep(1)
        return self

    # 选择角色
    def choose_role(self):
        self.find_element_by_xpath('//*[@id="list-group"]/li[1]').click()
        time.sleep(0.5)
        return self

    # 选择点击分配角色
    def click_allocation_role(self, user_name):
        time.sleep(0.5)
        rows = self.find_elements_by_css('.table tbody tr')
        ret = []
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[1].text, 'detail': tds[-2].text}
                # if u'待审核' == val['detail']:
                ret.append(val['name'])
                # handel = self.find_elements_by_name('id')
                index = ret.index(user_name)
        handel = self.find_elements_by_name('id')
        handel[index].click()
        return self

    # 获取借款状态
    def get_loan_status(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[1].text, 'detail': tds[-2].text}
                if user_name == val['name']:
                    return val['detail']

    # 获取信审专员姓名
    def get_credit_person(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[1].text, 'credit_person_name': tds[3].text}
                if user_name == val['name']:
                    return val['credit_person_name']

    # 按钮是否存在
    def allocation_button(self):
        button = self.find_element_by_css(
            '.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic.waves-effect.waves-classic').text
        return button

    # 分配角色流程
    def allocation_role(self, user_name):
        self.click_allocation_role(user_name).click_allocation_button().choose_role()
        return self

