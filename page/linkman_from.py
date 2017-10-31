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

    def linkman_detail(self):
        # 联系人类型
        linkman_type = Select(self.find_element_by_name('type'))  # 实例化Select
        linkman_type.select_by_value('1')
        # 与本人关系
        relation_ship = Select(self.find_element_by_name('relationship'))  # 实例化Select
        relation_ship.select_by_value('1')
        # 工作单位
        self.find_element_by_name('workUnit').send_keys(u'融贝')
        # 家庭或工作详细地址
        self.find_element_by_name('addr').send_keys(u'朝阳门')
        # 职位
        self.find_element_by_name('position').send_keys(u'测试')

    # 点击保存按钮
    def click_linkman_save(self):
        self.find_element_by_css(
            '.btn.btn-info.waves-effect.waves-classic.s-btn-info').click()
        return self

    # 点击添加联系人按钮
    def click_add_linkman(self):
        # self.find_element_by_xpath('//*[@id="addbtn"]/div').click()
        self.find_element_by_css('.icondemo.vertical-align-middle').click()
        return self

    # 点击删除按钮
    def click_delete_linkman(self):
        self.find_element_by_css('.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic')

    # 点击关闭按钮
    def click_linkman_close(self):
        self.find_element_by_css(
            '.btn.btn-default.btn-pure.waves-effect.waves-classic').click()
        return self

    # job合集
    def customer_job(self, name, department, position, tel_zone, tel, addr):
        self.job_name(name).job_department(department).job_position(position)
        self.job_detail()
        self.job_tel_zone(tel_zone).job_tel(tel).job_addr(addr)
        self.click_job_save()
        time.sleep(1)
        self.click_job_close()

    # 联系人姓名
    def linkman_name_error(self):
        message = self.find_element_by_xpath('//*[@id="global"]/div/div[1]/div[2]/small[1]').text
        return message

    # 联系电话
    def customer__tel_zone_error(self):
        message = self.find_element_by_xpath('//*[@id="global"]/div/div[1]/div[4]/small[1]').text
        return message

    # 电话
    def customer_linkman_tel_error(self):
        message = self.find_element_by_xpath('//*[@id="jobForm"]/div[2]/div[4]/small[3]').text
        return message
