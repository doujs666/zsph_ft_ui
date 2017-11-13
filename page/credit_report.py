# coding=UTF-8
from page.base_page import BasePage
import time


class CreditReport(BasePage):
    url = '/creditReport/form?customer.id={}'

    # 信用卡账户数量
    def card_account_num(self, num):
        self.find_element_by_name('cardAccountNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 住房借贷账户数量
    def house_account_num(self, num):
        self.find_element_by_name('houseAccountNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 其他借款账户数量
    def other_account_num(self, num):
        self.find_element_by_name('ohterAccountNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 信用卡未结清账户数
    def card_outstanding_num(self, num):
        self.find_element_by_name('cardOutstandingNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 住房借款未结清账户数
    def house_outstanding_num(self, num):
        self.find_element_by_name('houseOutstandingNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 其他借款未结清账户数
    def other_outstanding_num(self, num):
        self.find_element_by_name('ohterOutstandingNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 信用卡发生过逾期的账户数
    def card_overdue_num(self, num):
        self.find_element_by_name('cardOverdueNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 住房借款发生过逾期的账户数
    def house_overdue_num(self, num):
        self.find_element_by_name('houseOverdueNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 其他借款发生过逾期的账户数
    def other_overdue_num(self, num):
        self.find_element_by_name('ohterOverdueNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 信用卡发生过90天以上逾期的账户数
    def card_overdue_more_num(self, num):
        self.find_element_by_name('cardOverdueMoreNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 住房借款发生过90天以上逾期的账户数
    def house_overdue_more_num(self, num):
        self.find_element_by_name('houseOverdueMoreNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 其他借款发生过90天以上逾期的账户数
    def other_overdue_more_num(self, num):
        self.find_element_by_name('ohterOverdueMoreNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 信用卡为他人担保笔数
    def card_guarantee_num(self, num):
        self.find_element_by_name('cardGuaranteeNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 住房借款为他人担保笔数
    def house_guarantee_num(self, num):
        self.find_element_by_name('houseGuaranteeNum').send_keys(num)
        time.sleep(0.5)
        return self

    # 其他借款为他人担保笔数
    def other_guarantee_num(self, num):
        self.find_element_by_name('ohterGuaranteeNum').send_keys(num)
        time.sleep(0.5)
        return self

    def credit_report_detail(self, amount, use_amount, min_amount, real_amount, overdue):
        lists = ['card', 'loan']
        for i in lists:
            credit_report_amount = i + 'Amount'
            credit_report_use_amount = i + 'UseAmount'
            credit_report_min_amount = i + 'MinAmount'
            credit_report_real_amount = i + 'RealAmount'
            credit_report_overdue = i + 'Overdue'
            self.find_element_by_name(credit_report_amount).send_keys(amount)
            self.find_element_by_name(credit_report_use_amount).send_keys(use_amount)
            self.find_element_by_name(credit_report_min_amount).send_keys(min_amount)
            self.find_element_by_name(credit_report_real_amount).send_keys(real_amount)
            self.find_element_by_name(credit_report_overdue).send_keys(overdue)
        return self

    # 点击保存按钮
    def click_credit_report_save(self):
        self.find_element_by_css('.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 点击关闭按钮
    def click_credit_report_quit(self):
        self.find_element_by_css('.btn.btn-default.btn-pure.waves-effect.waves-classic.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 流程
    def credit_report(self, num, amount, use_amount, min_amount, real_amount, overdue):
        self.card_account_num(num).house_account_num(num).other_account_num(num)
        self.card_outstanding_num(num).house_outstanding_num(num).other_outstanding_num(num)
        self.card_overdue_num(num).house_overdue_num(num).other_overdue_num(num)
        self.card_overdue_more_num(num).house_overdue_more_num(num).other_overdue_more_num(num)
        self.card_guarantee_num(num).house_guarantee_num(num).other_guarantee_num(num)
        self.credit_report_detail(amount, use_amount, min_amount, real_amount, overdue)
        self.click_credit_report_save()
        self.click_credit_report_quit()

