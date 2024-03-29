# coding=UTF-8
from page.base_page import BasePage
from selenium.webdriver.support.ui import Select
import time


class ManagerContractForm(BasePage):
    # 信审主管结论
    url = '/contract/form?customer.id={}'

    # 借款状态
    def contract_label(self):
        time.sleep(2)
        text = self.find_element_by_xpath(
            '//*[@id="content"]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div[2]/input').get_attribute(
            "value")
        time.sleep(0.5)
        return text

    # 信审主管
    def governor_name(self):
        text = self.find_element_by_name('contract.governor.id').get_attribute("value")
        time.sleep(0.5)
        return text

    #   决策时间
    def decision_date(self):
        text = self.find_element_by_id('inputBasicProdate').get_attribute("value")
        time.sleep(0.5)
        return text

    # 借款类型
    def loan_type(self, number):
        get_loan_type = Select(self.find_element_by_name('type'))  # 实例化Select
        time.sleep(0.5)
        get_loan_type.select_by_value(number)
        return self

    # 利率
    def loan_rate(self, number):
        get_loan_rate = Select(self.find_element_by_name('rate'))  # 实例化Select
        time.sleep(0.5)
        get_loan_rate.select_by_value(number)
        return self

    # 期限
    def loan_cycle(self, number):
        get_loan_rate = Select(self.find_element_by_name('cycle'))  # 实例化Select
        time.sleep(0.5)
        get_loan_rate.select_by_value(number)
        return self

    # 到手金额
    def loan_actual_quota(self, actual_quota):
        self.find_element_by_name('actualQuota').clear()
        self.find_element_by_name('actualQuota').send_keys(actual_quota)
        time.sleep(0.5)
        return self

    # 备注
    def loan_remarks(self, remarks):
        self.find_element_by_name('remarks').send_keys(remarks)
        time.sleep(0.5)
        return self

    # 点击保存按钮
    def click_contract_save(self):
        self.find_element_by_id('updateForm').click()
        time.sleep(0.5)
        return self

    #  点击审批按钮
    def click_contract_submit(self):
        self.find_element_by_id('apply').click()
        time.sleep(0.5)
        return self

    # 点击关闭按钮
    def click_contract_quit(self):
        self.find_element_by_css(
            '.btn.btn-default.btn-pure.waves-effect.waves-classic.waves-effect.waves-classic').click()
        time.sleep(0.5)

    # 审批通过
    def contract_submit_pass(self):
        self.find_element_by_xpath('/html/body/div[2]/div/form/div/div[2]/div[1]/div[1]/input').click()
        time.sleep(0.5)
        return self

    # 审批驳回
    def contract_submit_reject(self):
        self.find_element_by_xpath('/html/body/div[2]/div/form/div/div[2]/div[1]/div[2]/input').click()
        time.sleep(0.5)
        return self

    # 审批驳回到信审专员
    def contract_submit_reject_commissioner_name(self):
        self.find_element_by_xpath('/html/body/div[2]/div/form/div/div[2]/div[1]/div[3]/input').click()
        time.sleep(0.5)
        return self

    # 实地征信
    def contract_submit_field_reference(self):
        self.find_element_by_xpath('/html/body/div[2]/div/form/div/div[2]/div[1]/div[4]/input').click()
        time.sleep(0.5)
        return self

    # 审批拒绝
    def contract_submit_repulse(self):
        self.find_element_by_xpath('/html/body/div[2]/div/form/div/div[2]/div[1]/div[5]/input').click()
        time.sleep(0.5)
        return self

    # 点击审批确定按钮
    def contract_submit_confirm(self):
        self.find_element_by_css('.btn.btn-primary.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 信审结论保存
    def contract_form(self, number, number1, number2, actual_quota, remarks):
        self.loan_type(number)
        # self.loan_rate(number1)
        self.loan_cycle(number2)
        self.loan_actual_quota(actual_quota)
        self.loan_remarks(remarks)
        self.click_contract_save()
        return self

    # 信审主管审核通过
    def contract_form_submit_pass(self):
        self.click_contract_submit()
        self.contract_submit_pass()
        self.contract_submit_confirm()
        time.sleep(3)
        return self

    # 信审主管审核驳回
    def contract_form_submit_reject(self):
        self.click_contract_submit()
        self.contract_submit_reject()
        self.contract_submit_confirm()
        time.sleep(3)
        return self

    # 信审主管驳回到信审专员
    def contract_form_submit_reject_commissioner(self):
        self.click_contract_submit()
        self.contract_submit_reject_commissioner_name()
        self.contract_submit_confirm()
        time.sleep(3)
        return self

    # 信审主管实地征信
    def contract_form_submit_field_reference(self):
        self.click_contract_submit()
        self.contract_submit_field_reference()
        self.contract_submit_confirm()
        time.sleep(3)
        return self

    # 信审主管拒绝
    def contract_form_submit_repulse(self):
        self.click_contract_submit()
        self.contract_submit_repulse()
        self.contract_submit_confirm()
        time.sleep(3)
        return self
