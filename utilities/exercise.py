# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://116.62.207.57')
driver.find_element_by_name('username').send_keys('wulala')
driver.find_element_by_name('password').send_keys('wulala')
driver.find_element_by_css_selector('.btn.btn-primary.btn-block.waves-effect.waves-classic').click()
time.sleep(1)
message = driver.find_element_by_xpath('/html/body/div/div/div[2]/p').text
print message
