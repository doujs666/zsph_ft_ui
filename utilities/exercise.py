# coding=UTF-8
import time
import hashlib
from utilities.my_sql import select_customer, clear_customer, clear_credit_report, clear_info_verify, clear_contract, \
    clear_sign_page, get_credit_person_login_name


def getToken(credit_id,key):
    dataStr = time.strftime("%Y%m%d",time.localtime())
    src = credit_id+"|"+dataStr+"|"+key
    md5 = hashlib.md5(src.encode('utf-8')).hexdigest()
    return md5

print getToken('2018042300004','irongbei0321')

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


def clear_data(customer_id):
    clear_credit_report(customer_id)
    clear_info_verify(customer_id)
    clear_contract(customer_id)
    clear_sign_page(customer_id)
    clear_customer(customer_id)

clear_data('37ca32e9d100492884ec8584e7fb2bc1')
