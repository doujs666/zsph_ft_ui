# -*- coding:utf-8 -*-
import json
import urllib
import requests
import session
from api import settings
# from api.base_api.image_captcha_api import ImageCaptchaApi
from base_api import BaseApi


class LoginApi(BaseApi):
    """
    用户登录
    """
    url = '/login'

    # def get_captcha(self):
    #     ImageCaptchaApi(device_id=self.device_id).post()
    #     return session.get_captcha(self.device_id)
    #
    # def login(self, mobile, password, source='android'):
    #     # captcha = self.get_captcha()
    #     captcha = self.re
    #     data = {'deviceId': settings.DEVICE_ID, 'password': password, 'source': source,
    #             'mobile': mobile, 'captcha': captcha}
    #
    #     login_data = urllib.urlencode(data)
    #     self.response = requests.post(url=self.api_url(),
    # data=login_data, headers={'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
    #     return json.loads(self.response.content)['data']['token']

    def login(self, mobile, password):
        data = {'mobile': mobile, 'password': password}

        login_data = urllib.urlencode(data)
        self.response = requests.post(url=self.api_url(), data=login_data,
                                      headers={'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
        return json.loads(self.response.content)['data']['token']
