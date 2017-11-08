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

    # 借款列表的一行
    def get_loan_list(self):
        rows = self.find_elements_by_css('.panel-body.s_panelbox')
        ret = []
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {"name": tds[0].text, "region": tds[1].text, "department": tds[2].text,
                       "risk_control": tds[3].text,"team_manager": tds[4].text, "customer_manager": tds[5].text,
                       "date": tds[6].text,"borrow_type": tds[7].text, "apply_money": tds[8].text,
                       "get_money": tds[9].text, "deadline": tds[11].text, "interest_rate": tds[12].text,
                       "status": tds[13].text, "detail": tds[14].text}
                ret.append(val)
        print ret

    # 点击分配角色
    def click_allocation_role(self, user_name):
        rows = self.find_elements_by_css('.table tbody tr')
        ret = []
        for row in rows:
            tds = row.find_elements_by_tag_name('td')
            if tds:
                val = {'name': tds[0].text, 'detail': tds[11].text}
                if u'分配' in val['detail']:
                    ret.append(val['name'])
        index = ret.index(user_name)
        handel = self.find_elements_by_css('.handle .rit')
        handel[index].click()
        return self

    # 分配角色流程
    def allocation_role(self, user_name):
        self.click_allocation_role(user_name).choose_role()
        return self

