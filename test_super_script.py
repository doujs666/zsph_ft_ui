# coding=UTF-8
from base import BaseSeleniumTestCase
from page.test_page import TestPage
from page.audit_superscript_list import AuditSuperScript
from page.super_script import SuperScript
from utilities.my_sql import select_customer, clear_super_script


class TestSuperScript(BaseSeleniumTestCase):
    # 审核上标测试
    login_name = 'dulr'
    password = 'admin'
    customer_name = u'测试审核商标'
    project_no = '998556'

    # 验证点击查看按钮url跳转
    def test_click_examine_button(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        # 校验跳转成功后url跳转
        AuditSuperScript(self.selenium).click_button()
        handles = AuditSuperScript(self.selenium).get_window_handles()
        url = AuditSuperScript(self.selenium).choose_window_handle(handles[1]).get_current_page_url()
        get_customer_id = select_customer(self.customer_name)['id']
        new_url = 'http://116.62.207.57/superscript/view?customer.id=' + str(get_customer_id)
        self.assertEqual(url, new_url)

    # 验证流程和状态
    def test_super_script_flow(self):
        TestPage(self.selenium).console_login(self.login_name, self.password)
        status = AuditSuperScript(self.selenium).get_super_script_status(self.customer_name)
        self.assertEqual(status, u'未处理')
        get_customer_id = select_customer(self.customer_name)['id']
        SuperScript(self.selenium, [get_customer_id]).super_script_flow(self.project_no)
        status1 = AuditSuperScript(self.selenium).get_super_script_status(self.customer_name)
        self.assertEqual(status1, u'已处理')

    def tearDown(self):
        super(TestSuperScript, self).tearDown()
        customer_id = select_customer(self.customer_name)['id']
        clear_super_script(customer_id)
