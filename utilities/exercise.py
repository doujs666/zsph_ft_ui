# coding=UTF-8
import time
import hashlib
from selenium import webdriver
#
def getToken(credit_id,key):
    dataStr = time.strftime("%Y%m%d",time.localtime())
    src = credit_id+"|"+dataStr+"|"+key
    md5 = hashlib.md5(src.encode('utf-8')).hexdigest()
    return md5

print getToken('2018032300002','irongbei0321')

#
#
# foo = ['a', 'b', 'c', 'd', 'e']
# from random import choice
# print choice(foo)

# def get_number(number):
#     print 159391.61 * 0.0005 * number
#
# get_number(4)

# def get_mouth(mouth):
#     print 5269.24 * mouth
#
# get_mouth()
