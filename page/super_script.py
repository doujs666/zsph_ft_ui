# coding=UTF-8
from page.base_page import BasePage
import time


class SuperScript(BasePage):
    url = '/superscript/view?customer.id={}'

    # 项目编号
    def project_no(self, project_no):
        self.find_element_by_id('projectNo').send_keys(project_no)
        time.sleep(0.5)
        return self

    # 点击下载按钮
    def click_generate_Button(self):
        self.find_element_by_id('generateBtn').click()
        time.sleep(0.5)
        return self

    # 点击完成按钮
    def click_apply_button(self):
        self.find_element_by_id('apply').click()
        return self

    # 流程
    def super_script_flow(self, project_no):
        self.project_no(project_no)
        self.click_generate_Button()
        self.click_apply_button()



