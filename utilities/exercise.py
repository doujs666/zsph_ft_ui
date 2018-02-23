# coding=UTF-8
import time
import hashlib

def getToken(credit_id,key):
    dataStr = time.strftime("%Y%m%d",time.localtime())
    src = credit_id+"|"+dataStr+"|"+key
    md5 = hashlib.md5(src.encode('utf-8')).hexdigest()
    return md5

print getToken('2018021200002','irongbei0321')



val = ['张三', '历史']
print val.index('历史')