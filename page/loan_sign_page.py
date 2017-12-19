# coding=UTF-8
from page.base_page import BasePage
import time


class LoanSignPage(BasePage):
    # 合同审核

    url = '/contract/toSignPage?loanId={0}&customer.id={1}'

    # 获取合同名称
    def get_contract_status(self):
        rows = self.find_elements_by_css('.table tbody tr')
        del rows[0]
        rel = []
        for rows in rows:
            tds = rows.find_elements_by_tag_name('td')
            if tds:
                val = {'contract_name': tds[1].text}
                rel.append(val['contract_name'])
        return rel

    # 点击提交按钮
    def click_apply_button(self):
        self.find_element_by_id('apply').click()
        time.sleep(0.5)
        return self

    # 审批通过
    def choose_pass(self):
        self.find_element_by_xpath('//*[@id="applyForm"]/div/div[2]/div[1]/div[1]/input')
        time.sleep(0.5)
        return self

    # 审批拒绝
    def choose_reject(self):
        self.find_element_by_xpath('//*[@id="applyForm"]/div/div[2]/div[1]/div[2]/input')
        time.sleep(0.5)
        return self

    # 点击确定按钮
    def click_submit_button(self):
        self.find_element_by_css('.btn.btn-primary.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 放款按钮
    def click_loan_button(self):
        self.find_element_by_css('.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self





