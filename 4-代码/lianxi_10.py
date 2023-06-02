# 导包
import requests


class TestHouziLogin(object):

    def test01_login_success(self):
        # 准备测试数据
        login_url = ' https://www.72crm.com/api-11/login'
        login_header = {'Content-Type': 'application/json;charset=UTF-8'}
        login_data = {"username": "15122571345", "password": "123456qwer"}

        # 发送接口请求
        resp_login = requests.post(url=login_url, headers=login_header, json=login_data)

        # 获取响应结果，并打印pyt
        print('响应码', resp_login.status_code)
        print('返回文本', resp_login.json())

        # 断言
        assert resp_login.status_code == 200
        assert resp_login.json().get('code') == 0
        assert resp_login.json().get('msg') == 'success'

    def test02_mobile_error(self):
        # 准备测试数据
        login_url = ' https://www.72crm.com/api-11/login'
        login_header = {'Content-Type': 'application/json;charset=UTF-8'}
        login_data = {"username": "15122571346", "password": "123456qwer"}

        # 发送接口请求
        resp_login = requests.post(url=login_url, headers=login_header, json=login_data)

        # 获取响应结果，并打印pyt
        print('响应码', resp_login.status_code)
        print('返回文本', resp_login.json())

        # 断言
        assert resp_login.status_code == 200
        assert resp_login.json().get('code') == 1009
        assert resp_login.json().get('msg') == '账号或密码错误'

    # 密码为空
    def test03_password_error(self):
        # 准备测试数据
        login_url = ' https://www.72crm.com/api-11/login'
        login_header = {'Content-Type': 'application/json;charset=UTF-8'}
        login_data = {"username": "15122571346"}

        # 发送接口请求
        resp_login = requests.post(url=login_url, headers=login_header, json=login_data)

        # 获取响应结果，并打印pyt
        print('响应码', resp_login.status_code)
        print('返回文本', resp_login.json())

        # 断言
        assert resp_login.status_code == 200
        assert resp_login.json().get('code') == 1003
        assert resp_login.json().get('msg') == '请输入密码或短信验证码'