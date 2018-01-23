# coding=UTF-8
import time
import hashlib
from locust import HttpLocust, TaskSet, task

# def getToken(credit_id,key):
#     dataStr = time.strftime("%Y%m%d",time.localtime())
#     src = credit_id+"|"+dataStr+"|"+key
#     md5 = hashlib.md5(src.encode('utf-8')).hexdigest()
#     return md5
#
#
# print getToken('2018011200016',' irongbei0321')

# 定义用户行为
class UserBehavior(TaskSet):

    @task
    def baidu_page(self):
        self.client.get("/")

class WebSiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000