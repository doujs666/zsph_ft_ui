# coding=UTF-8
from page.base_page import BasePage
from selenium.webdriver.support.ui import Select
import time


class CustomerLoan(BasePage):
    url = '/loan/form?customer.id={}'

    # 申请金额
    def loan_apply_quota(self, apply_quota):
        self.find_element_by_id('applyQuota').send_keys(apply_quota)
        time.sleep(0.5)
        return self

    # 每月最高还款
    def loan_repayment_quota(self, repayment_quota):
        self.find_element_by_id('repaymentQuota').send_keys(repayment_quota)
        time.sleep(0.5)
        return self

    # 借款类型
    def loan_type(self, type_number):
        loan_type = Select(self.find_element_by_name('type'))  # 实例化Select
        loan_type.select_by_value(type_number)
        return self

    # 申请期限
    def loan_cycle(self, cycle_number):
        loan_cycle = Select(self.find_element_by_name('cycle'))  # 实例化Select
        loan_cycle.select_by_value(cycle_number)
        return self

    def loan_detail(self):
        # 借款用途
        loan_purpose = Select(self.find_element_by_name('purpose'))  # 实例化Select
        loan_purpose.select_by_value('1')
        # 是否加急
        loan_urgent = Select(self.find_element_by_name('urgent'))  # 实例化Select
        loan_urgent.select_by_value('1')
        # 从何处得知本借款
        loan_where_know = Select(self.find_element_by_name('whereKnow'))  # 实例化Select
        loan_where_know.select_by_value('2')

    # 申请日期
    def loan_apply_date(self):
        apply_date = self.find_element_by_name('applyDate').text
        return apply_date

    # 点击保存按钮
    def click_loan_save(self):
        self.find_element_by_css(
            '.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic.waves-effect.waves-classic').click()
        return self

    # 点击关闭按钮
    def click_loan_close(self):
        self.find_element_by_css(
            '.btn.btn-default.btn-pure.waves-effect.waves-classic.waves-effect.waves-classic').click()
        return self

    # loan流程
    def customer_loan(self, type_number, apply_quota, cycle_number, repayment_quota):
        self.loan_type(type_number).loan_apply_quota(apply_quota).loan_cycle(cycle_number).loan_repayment_quota(
            repayment_quota)
        self.loan_detail()
        self.click_loan_save()
        self.click_loan_close()
        self.click_loan_submit()
    # 申请金额error

    def customer_loan_apply_quota_error(self):
        message = self.find_element_by_xpath('//*[@id="Loan_form"]/div[2]/div[3]/small[1]').text
        return message

    # 可接受最高月还款error
    def customer_loan_repayment_quota_error(self):
        message = self.find_element_by_xpath('//*[@id="Loan_form"]/div[3]/div[1]/small[1]').text
        return message

    # 点击提交按钮
    def click_loan_submit(self):
        time.sleep(1)
        self.find_element_by_xpath('//*[@id="apply"]').click()
        time.sleep(1)
        self.find_element_by_css('.btn.btn-primary.waves-effect.waves-classic').click()
        return self
