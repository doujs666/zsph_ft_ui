# coding=UTF-8
from page.base_page import BasePage
import time
from selenium.webdriver.support.ui import Select

class NewStaff(BasePage):
    # 合同审核

    url = '/user/form'

    # 选择大区
    def select_region(self):
        region = Select(self.find_element_by_id('region'))  # 实例化Select
        time.sleep(0.5)
        region.select_by_value('24')
        return self

    # 选择营业部
    def select_sales_department(self):
        sales_department = Select(self.find_element_by_id('salesDepartment'))
        time.sleep(0.5)
        sales_department.select_by_value('4f2a4788aa084cf495f5b3156032b2a4')
        return self

    # 工号
    def staff_number(self):
        self.find_element_by_id('no').send_keys('9527')
        time.sleep(0.5)
        return self

    # 姓名
    def staff_name(self):
        self.find_element_by_name('name').send_keys(u'张三')
        time.sleep(0.5)
        return self

    # 登录名
    def staff_login_name(self, staff_login_name):
        self.find_element_by_id('loginName').send_keys(staff_login_name)
        time.sleep(0.5)
        return self

    # 密码
    def staff_new_password(self, new_password):
        self.find_element_by_id('newPassword').send_keys(new_password)
        time.sleep(0.5)
        return self

    # 确认密码
    def confirm_new_password(self):
        self.find_element_by_id('confirmNewPassword').send_keys('admin')
        time.sleep(0.5)
        return self

    # 邮箱
    def staff_email(self):
        self.find_element_by_name('email').send_keys('778899@qq.com')
        time.sleep(0.5)
        return self

    # 电话
    def staff_phone(self):
        self.find_element_by_id('phone').send_keys('5138438')
        time.sleep(0.5)
        return self

    # 手机
    def staff_tel(self):
        self.find_element_by_id('mobile').send_keys('13888888888')
        time.sleep(0.5)
        return self

    # 是否允许登录
    def if_login(self, login_flag):
        if_login = Select(self.find_element_by_id('loginFlag'))
        time.sleep(0.5)
        if_login.select_by_value(login_flag)
        return self

    # 用户角色
    def staff_role(self):
        self.find_element_by_id('roleIdList5').click()
        time.sleep(0.5)
        return self

    # 点击保存按钮
    def click_save_button(self):
        self.find_element_by_css('.btn.btn-info.waves-effect.waves-classic.s-btn-info.waves-effect.waves-classic.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 流程
    def staff_flow(self, staff_login_name, new_password):
        self.staff_name().staff_number().select_region().staff_login_name(staff_login_name)
        self.select_sales_department().confirm_new_password()
        self.staff_new_password(new_password).staff_email().staff_phone().staff_tel().staff_role()
        return self
