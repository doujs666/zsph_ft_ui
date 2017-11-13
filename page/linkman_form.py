# coding=UTF-8
from page.base_page import BasePage
from selenium.webdriver.support.ui import Select
import time


class CustomerLinkman(BasePage):
    url = '/linkman/form?customer.id={}'

    # 姓名
    def linkman_name(self, name, number):
        value = 'linkmanList' + number + '_name'
        self.find_element_by_id(value).send_keys(name)
        time.sleep(0.5)
        return self

    # 与本人关系
    def linkman_list_relationship(self, number):
        value = 'linkmanList' + number + '_relationship'
        linkman_relationship = Select(self.find_element_by_id(value))  # 实例化Select
        linkman_relationship.select_by_value('2')

    # 工作单位
    def linkman_work_unit(self, work_unit, number):
        value = 'linkmanList' + number + '_workUnit'
        self.find_element_by_id(value).send_keys(work_unit)
        time.sleep(0.5)
        return self

    # 详细地址
    def linkman_address(self, address, number):
        value = 'linkmanList' + number + '_addr'
        self.find_element_by_id(value).send_keys(address)
        time.sleep(0.5)
        return self

    # 职务
    def linkman_position(self, position, number):
        value = 'linkmanList' + number + '_position'
        self.find_element_by_id(value).send_keys(position)
        time.sleep(0.5)
        return self

    # 联系电话
    def linkman_tel(self, tel, number):
        value = 'linkmanList' + number + '_tel'
        self.find_element_by_id(value).send_keys(tel)
        time.sleep(0.5)
        return self

    # 保存按钮
    def click_linkman_save(self):
        self.find_element_by_css(
            '.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 关闭成功按钮
    def click_linkman_quit(self):
        self.find_element_by_css(
            '.btn.btn-default.btn-pure.waves-effect.waves-classic.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 点击添加联系人
    # 点击删除按钮

    # 流程
    def linkman(self, name, work_unit, address, position, tel):
        for i in range(6):
            time.sleep(1)
            self.linkman_name(name, str(i)).linkman_list_relationship(str(i))
            self.linkman_work_unit(work_unit, str(i)).linkman_address(address, str(i)).linkman_position(position, str(
                i)).linkman_tel(tel, str(i))
        self.click_linkman_save()
        self.click_linkman_quit()
