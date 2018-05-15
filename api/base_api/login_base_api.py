# -*- coding:utf-8 -*-
from api.base_api.base_api import BaseApi
from api.base_api.login_api import LoginApi
# from utilities import user


class LoginBaseApi(BaseApi):
    def __init__(self, mobile, password, *args, **kwargs):
        super(LoginBaseApi, self).__init__(*args, **kwargs)
        self.mobile = mobile
        self.password = password

    def build_base_param(self):
        base_param = super(LoginBaseApi, self).build_base_param()
        token = LoginApi().login(self.mobile, self.password)
        base_param['baseParam']['token'] = token
        base_param['baseParam']['phoneNum'] = self.mobile
        base_param['baseParam']['userId'] = user.get_user_login_name(self.mobile)
        return base_param
