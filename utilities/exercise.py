# coding=UTF-8
import time
import hashlib
import requests


def get_token(credit_id, key):
    data_str = time.strftime("%Y%m%d", time.localtime())
    src = credit_id + "|" + data_str + "|" + key
    md5 = hashlib.md5(src.encode('utf-8')).hexdigest()
    return md5


a = str(input(u'输入合同编号'))
b = get_token(a, 'irongbei0321')
print b

url = 'http://101.37.114.86:8010/api/notify/firstPayment'
data = {
    "creditId": a,
    "token": b
}
s = requests.session()
response = s.post(url=url, json=data)
print(response.text)