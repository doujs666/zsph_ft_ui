# -*- coding:utf-8 -*-
import json
import requests
from api import settings
from api.settings import WEB_TEST_BASE_URL


class WebBaseApi(object):
    url = ""

    def __init__(self, url_params=None):
        if not url_params:
            url_params = []
        self.url_params = url_params
        self.response = None
        self.base_url = WEB_TEST_BASE_URL

    def web_api_url(self):
        if not self.url:
            raise RuntimeError("no url been set")          #抛出异常
        return self._get_url()

    def _get_url(self):
        format_url = self.url.format(self.url_params)
        return "{0}{1}".format(self.base_url, format_url)

    def post(self, data=None):
        if not data:
            data = {}
        self.response = requests.session().post(url=self.web_api_url(), json=data, headers=settings.headers, allow_redirects = True)
        return self.response

    def get_code(self):
        if self.response:
            return json.loads(self.response.text)['code']

    def get_status_code(self):
        if self.response:
            return self.response.status_code

    def get_response_message(self):
        if self.response:
            return json.loads(self.response.text)['message']

    # def build_base_param(self):
    #     return {
    #         "baseParam": {
    #             "userId": '',
    #             "osVersion": "9.0.2",
    #             "appVersion": "9.0.2",
    #             "deviceId": self.device_id,
    #             "phoneNum": '',
    #             "platform": "IOS",
    #             "token": "",
    #             "screenW": "750",
    #             "screenH": "1334",
    #             "deviceModel": "iPhone",
    #             "channel": ""}
    #     }
    #
    # def build_custom_param(self, data):
    #     return {}
