ENV = 'test'
WEB_TEST_BASE_URL = "http://116.62.207.57/a"
WAIT_TIME = 10

#redis
REDIS_HOST = '192.168.1.157'
REDIS_PORT = 20016
SESSION_REDIS_DB = 2

# UMPAY_BASE_URL = "http://192.168.1.157:5000/spay/pay/payservice.do"
# GECKODRIVER_PATH = 'geckodriver'  # used by FireFox
GECKODRIVER_PATH = 'chromedriver'

DB_CONFIG = {
    "HOST": '116.62.207.57',
    "PORT": 3306,
    "USER": 'credit',
    "PASSWORD": '!Mi~p1Kkli&ASe'
}

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SNAPSHOT_DIRECTORY = os.path.join(BASE_DIR, 'logs')

SETTING_LOCAL_DIR = os.path.join(BASE_DIR, "settings_local.py")
if os.path.exists(SETTING_LOCAL_DIR):
    execfile(SETTING_LOCAL_DIR)