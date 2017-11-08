# coding=UTF-8
from page.base_page import BasePage
from selenium.webdriver.support.ui import Select
import time


class CustomerJob(BasePage):
    url = '/job/form?customer.id={}'

    # def click_customer_job(self):
    #     time.sleep(0.5)
    #     self.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div[1]/div/section/section[1]/div/a[2]').click()
    #     return self

    # 公司名称
    def job_name(self, name):
        self.find_element_by_id('name').send_keys(name)
        time.sleep(0.5)
        return self

    # 公司部门
    def job_department(self, department):
        self.find_element_by_id('department').send_keys(department)
        time.sleep(0.5)
        return self

    # 公司职位
    def job_position(self, position):
        self.find_element_by_id('position').send_keys(position)
        time.sleep(0.5)
        return self

    # 电话
    def job_tel_zone(self, tel_zone):
        self.find_element_by_id('telZone').send_keys(tel_zone)
        time.sleep(0.5)
        return self

    # 电话
    def job_tel(self, tel):
        self.find_element_by_id('tel').send_keys(tel)
        time.sleep(0.5)
        return self

    # 工作地址
    def job_addr(self, address):
        self.find_element_by_id('addr').send_keys(address)
        time.sleep(0.5)
        return self

    def job_detail(self):
        # 单位性质
        unit_property_status = Select(self.find_element_by_name('unitProperty'))  # 实例化Select
        unit_property_status.select_by_value('1')
        # 职位级别
        position_level_status = Select(self.find_element_by_name('positionLevel'))  # 实例化Select
        position_level_status.select_by_value('1')
        # 现单位地址
        address_province_status = Select(self.find_element_by_name('addrProvince'))  # 实例化Select
        address_province_status.select_by_value('110000')
        # 城市
        address_city_status = Select(self.find_element_by_name('addrCity'))  # 实例化Select
        time.sleep(0.5)
        address_city_status.select_by_value('110100')
        # 区
        marital_status = Select(self.find_element_by_name('addrCounty'))  # 实例化Select
        time.sleep(0.5)
        marital_status.select_by_value('110101')
        # 工资发放形式
        salary_style_status = Select(self.find_element_by_name('salaryStyle'))  # 实例化Select
        salary_style_status.select_by_value('1')
        # 入职时间
        time.sleep(0.5)
        self.find_element_by_name('inductionDate').send_keys('20170101')

    # 点击保存按钮
    def click_job_save(self):
        time.sleep(0.5)
        self.find_element_by_css(
            '.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic').click()
        return self

    # 点击关闭按钮
    def click_job_close(self):
        self.find_element_by_css(
            '.btn.btn-default.btn-pure.waves-effect.waves-classic.waves-effect.waves-classic').click()
        return self

    # job合集
    def customer_job(self, name, department, position, tel_zone, tel, addr):
        self.job_name(name).job_department(department).job_position(position)
        self.job_detail()
        self.job_tel_zone(tel_zone).job_tel(tel).job_addr(addr)
        self.click_job_save()
        time.sleep(1)
        self.click_job_close()

    # 工作单位错误提示
    def customer_job_name_error(self):
        message = self.find_element_by_xpath('//*[@id="jobForm"]/div[1]/div[1]/small[1]').text
        return message

    # 电话区号
    def customer_job_tel_zone_error(self):
        message = self.find_element_by_xpath('//*[@id="jobForm"]/div[2]/div[4]/small[1]').text
        return message

    # 电话
    def customer_job_tel_error(self):
        message = self.find_element_by_xpath('//*[@id="jobForm"]/div[2]/div[4]/small[3]').text
        return message

    # 地址
    def customer_job_address(self):
        message = self.find_element_by_xpath('//*[@id="jobForm"]/div[3]/div[2]/small[1]').text
        return message
