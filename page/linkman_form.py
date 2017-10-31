# coding=UTF-8
from page.base_page import BasePage
from selenium.webdriver.support.ui import Select
import time


class CustomerLinkman(BasePage):
    url = '/linkman/form?customer.id={}'

    # def click_customer_job(self):
    #     time.sleep(0.5)
    #     self.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[2]/div[1]/div/section/section[1]/div/a[2]').click()
    #     return self

    # 联系人姓名
    def linkman_name(self, name):
        self.find_element_by_name('name').send_keys(name)
        time.sleep(0.5)
        return self

    # 联系人电话
    def linkman_tel(self, tel):
        self.find_element_by_name('tel').send_keys(tel)
        time.sleep(0.5)
        return self

    # 工作单位
    def linkman_work_unit(self, work_unit):
        self.find_element_by_name('workUnit').send_keys(work_unit)
        time.sleep(0.5)
        return self

    # 家庭或工作地址详情
    def linkman_address(self, address):
        self.find_element_by_name('addr').send_keys(address)
        time.sleep(0.5)
        return self

    # 职位
    def linkman_position(self, position):
        self.find_element_by_name('position').send_keys(position)
        time.sleep(0.5)
        return self

    def linkman_detail(self):
        # 联系人类型
        linkman_type = Select(self.find_element_by_name('type'))  # 实例化Select
        linkman_type.select_by_value('1')
        # 与本人关系
        linkman_relation_ship = Select(self.find_element_by_name('relationship'))  # 实例化Select
        linkman_relation_ship.select_by_value('1')

    # 点击保存按钮
    def click_linkman_save(self):
        self.find_element_by_css(
            '.btn.btn-info.waves-effect.waves-classic.s-btn-info').click()
        return self

    # 点击关闭按钮
    def click_job_close(self):
        self.find_element_by_css(
            '.btn.btn-default.btn-pure.waves-effect.waves-classic').click()
        return self

    # 点击添加联系人按钮
    def click_linkman_add(self):
        self.find_element_by_xpath('//*[@id="addbtn"]/div/font').click()
        return self

    # 点击删除按钮
    def click_linkman_delete(self):
        self.find_element_by_css('.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic')

    # linkman流程
    def customer_linkman(self, name, tel, work_unit, address, position):
        self.linkman_name(name).linkman_tel(tel).linkman_work_unit(work_unit).linkman_address(address)
        self.linkman_position(position)
        self.linkman_detail()
        self.click_linkman_save()

    # 联系人姓名错误
    def customer_linkman_name_error(self):
        message = self.find_element_by_xpath('//*[@id="global"]/div/div[1]/div[2]/small[1]').text
        return message

    # 联系电话
    def customer_linkman_tel_error(self):
        message = self.find_element_by_xpath('//*[@id="global"]/div/div[1]/div[4]/small[1]').text
        return message

