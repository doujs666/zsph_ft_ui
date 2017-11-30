# coding=UTF-8
from page.base_page import BasePage
import time


class InfoVerifyTel(BasePage):
    url = '/infoVerify/tel/list?customer.id={}'

    def info_verify_detail(self, text):
        for i in range(1, 55):
            num = 'infoVerifyList[' + str(i) + '].remarks'
            self.find_element_by_name(num).send_keys(text)
            time.sleep(0.5)
        return self

    # 点击保存按钮
    def click_info_verify_save(self):
        self.find_element_by_css('.btn.btn-primary.rit.put-right.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 保存成功关闭按钮
    def click_info_verify_quit(self):
        self.find_element_by_css('.btn.btn-default.btn-pure.waves-effect.waves-classic.waves-effect.waves-classic').click()
        time.sleep(0.5)
        return self

    # 流程
    def info_verify(self, text):
        self.info_verify_detail(text)
        self.click_info_verify_save()
        self.click_info_verify_quit()



