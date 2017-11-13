# coding=UTF-8
from page.base_page import BasePage
from selenium.webdriver.support.ui import Select
import time, random


class CustomerFrom(BasePage):
    url = '/customer/form'

    def customer_name(self, name):
        self.find_element_by_xpath('//*[@id="name"]').send_keys(name)
        time.sleep(0.5)
        return self

    def customer_card_no(self, card_no):
        self.find_element_by_name('cardNo').send_keys(card_no)
        time.sleep(0.5)
        return self

    def customer_mobile(self, mobile):
        self.find_element_by_name('mobile1').send_keys(mobile)
        time.sleep(0.5)
        return self

    def customer_tel_time(self, tel_time):
        self.find_element_by_name('telTime').send_keys(tel_time)
        time.sleep(0.5)
        return self

    def customer_status(self):
        number = random.randint(1, 4)
        # 婚姻状况
        marital_status = Select(self.find_element_by_name('maritalStatus'))  # 实例化Select
        marital_status.select_by_value(str(number))
        # 子女数目
        child_count = Select(self.find_element_by_name('childCount'))  # 实例化Select
        child_count.select_by_value(str(number))
        # 供养人数
        apply_count = Select(self.find_element_by_name('applyCount'))  # 实例化Select
        apply_count.select_by_value(str(number))
        # 最高学历
        education = Select(self.find_element_by_name('education'))  # 实例化Select
        education.select_by_value(str(number))
        # 是否本市户籍
        census_register = Select(self.find_element_by_name('censusRegister'))  # 实例化Select
        census_register.select_by_value('1')
        # 居住类型
        houst_status = Select(self.find_element_by_name('houstStatus'))  # 实例化Select
        houst_status.select_by_value(str(number))
        # 现住宅地起始居住日期
        self.find_element_by_name('houseStartDate').send_keys(20170101)
        # 来本市日期
        self.find_element_by_name('comeDate').send_keys(20170101)
        # 户口所在地
        card_addr_province = Select(self.find_element_by_name('cardAddrProvince'))  # 实例化Select
        card_addr_province.select_by_value('110000')
        time.sleep(0.5)
        card_addr_city = Select(self.find_element_by_name('cardAddrCity'))  # 实例化Select
        card_addr_city.select_by_value('110100')
        time.sleep(1)
        card_addr_county = Select(self.find_element_by_name('cardAddrCounty'))  # 实例化Select
        card_addr_county.select_by_value('110105')
        # 详细地址
        self.find_element_by_name('cardAddr').send_keys(u'测试详细地址')
        # 现住宅地址
        addr_province = Select(self.find_element_by_name('addrProvince'))  # 实例化Select
        addr_province.select_by_value('120000')
        time.sleep(0.5)
        addrCity = Select(self.find_element_by_name('addrCity'))  # 实例化Select
        addrCity.select_by_value('120100')
        time.sleep(0.5)
        addr_county = Select(self.find_element_by_name('addrCounty'))  # 实例化Select
        addr_county.select_by_value('120114')
        # 详细地址2
        self.find_element_by_name('addr').send_keys(u'测试详细地址2')
        return self

    # 电子邮箱
    def customer_email(self, email):
        self.find_element_by_name('email').send_keys(email)
        time.sleep(0.5)
        return self

    def customer_annual_income(self, annual_income):
        self.find_element_by_name('annualIncome').send_keys(annual_income)
        time.sleep(0.5)
        return self

    def click_save(self):
        self.find_element_by_css(
            '.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic').click()
        self.get_current_page_url()
        time.sleep(0.5)
        return self

    # 创建客户
    def new_customer(self, name, card_no, mobile, tel_time, email, annual_income):
        self.customer_name(name).customer_card_no(card_no).customer_mobile(mobile).customer_tel_time(tel_time)
        self.customer_status()
        self.customer_email(email).customer_annual_income(annual_income)
        self.click_save()
        self.click_limit()

    def get_card_no_error(self):
        message = self.find_element_by_xpath('//*[@id="customerForm"]/div[2]/div[2]/small[1]').text
        return message

    def get_card_no_none_error(self):
        message = self.find_element_by_xpath('//*[@id="customerForm"]/div[2]/div[2]/small[2]').text
        return message

    def get_name_none_error(self):
        message = self.find_element_by_xpath('//*[@id="customerForm"]/div[2]/div[1]/small[1]').text
        return message

    def get_mobile_none_error_error(self):
        message = self.find_element_by_xpath('//*[@id="customerForm"]/div[2]/div[3]/small[2]').text
        return message

    def get_email_error(self):
        message = self.find_element_by_xpath('//*[@id="customerForm"]/div[7]/div[1]/small[1]').text
        return message

    def get_email_none_error(self):
        message = self.find_element_by_xpath('//*[@id="customerForm"]/div[7]/div[1]/small[2]').text
        return message

    def get_annual_income_error(self):
        message = self.find_element_by_xpath('//*[@id="customerForm"]/div[7]/div[2]/small[1]').text
        return message

    def click_limit(self):
        time.sleep(1)
        self.find_element_by_xpath('//*[@id="showMessage"]/div/div/div[1]/button').click()
