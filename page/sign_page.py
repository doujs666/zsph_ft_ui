# coding=UTF-8
from page.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


class SignPage(BasePage):
    # 销售管理

    url = '/contract/toSignPage?customer.id={}'

    # 开户行
    def bank_num(self, value):
        get_bank_num = Select(self.find_element_by_id('bankNm'))  # 实例化Select
        time.sleep(0.5)
        get_bank_num.select_by_value(value)
        return self

    # 银行账号
    def account_number(self, number):
        self.find_element_by_name('acntNo').send_keys(number)
        return self

    # 点击保存按钮
    def click_save_button(self):
        self.find_element_by_id('saveBtn').click()
        return self

    # 点击富有认证
    def click_fuyou_button(self):
        self.find_element_by_id('fuiouBtn').click()
        return self

    # 富有认证按钮存不存在
    def fuyou_button_if_exist(self):
        try:
            if self.find_element_by_id('fuiouBtn'):
                return True
        except:
            return False

    # 点击签约按钮
    def click_sign_button(self):
        self.find_element_by_id('signBtn').click()
        time.sleep(2)
        return self

    # 点击生成按钮
    def click_generate_button(self):
        self.find_element_by_id('generateBtn').click()
        time.sleep(10)
        return self

    # 点击提示信息关闭按钮
    def click_hint_close(self):
        self.find_element_by_css('.btn.btn-default.btn-pure.waves-effect.waves-classic.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 获取合同名称
    def get_contract_status(self):
        rows = self.find_elements_by_css('.table tbody tr')
        del rows[0]
        rel = []
        for rows in rows:
            tds = rows.find_elements_by_tag_name('td')
            if tds:
                val = {'contract_name': tds[1].text, 'detail': tds[3].text}
                rel.append(val['contract_name'])
        return rel

    # 拖拽签章
    def move_signature(self):
        element = self.find_element_by_xpath('//*[@id="signpanel"]/div/img')
        ActionChains(self.selenium).drag_and_drop_by_offset(element, 400, 800).perform()
        time.sleep(0.5)
        return self

    # 点击确认签署
    def click_affirm_sign(self):
        self.find_element_by_id('confirmSubmit').click()
        time.sleep(0.5)
        return self

    # 定位确认签署验证码输入框
    def input_verification_code(self, verification_code):
        self.find_element_by_id('smsval').send_keys(verification_code)
        time.sleep(0.5)
        return self

    # 点击确认签署按钮
    def click_new_affirm_sign(self):
        self.find_element_by_css('.commit').click()
        time.sleep(0.5)
        return self

    # 点击提交按钮
    def click_apply_button(self):
        self.find_element_by_id('apply').click()
        time.sleep(0.5)
        return self

    # 提交弹框确认按钮
    def new_click_apply_button(self):
        self.find_element_by_id('applySub').click()
        time.sleep(0.5)
        return self

    # 签署流程
    def sign_flow(self, verification_code):
        self.click_sign_button()
        self.move_signature().click_affirm_sign().input_verification_code(verification_code)
        self.click_new_affirm_sign()
        time.sleep(1)
        return self

    # 生成合同流程
    def create_contract_flow(self, bank_number):
        self.account_number(bank_number).click_save_button().click_generate_button()
        return self

    # 整体流程
    def sign_page_flow(self, bank_number):
        self.create_contract_flow(bank_number)
        self.click_apply_button().new_click_apply_button()


