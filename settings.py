# -*- coding:utf-8 -*-
ENV = 'test'
WEB_TEST_BASE_URL = "http://101.37.114.86:8010"
# WEB_TEST_BASE_URL = "http://116.62.144.138"
WAIT_TIME = 10

# redis
REDIS_HOST = '192.168.1.157'
REDIS_PORT = 20016
SESSION_REDIS_DB = 2

# UMPAY_BASE_URL = "http://192.168.1.157:5000/spay/pay/payservice.do"
GECKODRIVER_PATH = 'geckodriver'  # used by FireFox
# GECKODRIVER_PATH = 'chromedriver' #used by chrome

# Mysql配置
TEST_MYSQL_CONFIG = {'host': 'test-zsph.mysql.rds.aliyuncs.com', 'port': 3306, 'user': 'credit_test', 'password': '1XPFrpm^D!8#lxbWa3'}
TEST_DEFAULT_DB = 'credit_test'


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SNAPSHOT_DIRECTORY = os.path.join(BASE_DIR, 'logs')

SETTING_LOCAL_DIR = os.path.join(BASE_DIR, "settings_local.py")
if os.path.exists(SETTING_LOCAL_DIR):
    execfile(SETTING_LOCAL_DIR)
