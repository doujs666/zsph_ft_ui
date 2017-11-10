# coding=utf-8
user_name = u'测试'
ret = ['123', '232', '123213']
val = {'name': u'测试'}
ret.append(val['name'])
print ret[0]
index = ret.index(user_name)
print index