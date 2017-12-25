# coding=UTF-8
from page.base_page import BasePage
import time


class AuditSuperScript(BasePage):
    # 销售管理

    url = '/superscript/list'

    # 点击查看按钮
    def click_allocation_role(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        ret = []
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[3].text, 'detail': tds[-1].text}
                # if u'待审核' == val['detail']:
                ret.append(val['name'])
                # handel = self.find_elements_by_name('id')
        index = ret.index(user_name)
        handel = self.find_elements_by_css('.handle')
        handel[index].click()
        return self

    # 获取审核上标状态
    def get_super_script_status(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[3].text, 'super_script': tds[-2].text}
                if user_name == val['name']:
                    return val['super_script']

    def click_button(self):
        self.find_element_by_xpath(
            '//*[@id="searchForm"]/div/div[3]/div/div/div/div/div[1]/table/tbody/tr/td[14]/span').click()
        return self
