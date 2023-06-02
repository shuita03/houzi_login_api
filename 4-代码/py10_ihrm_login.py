import requests


class TestIHRMLogin:

    #登录成功
    def test_login_success(self):
        #设置url ,header,body,获取响应结果
        login_url = "http://ihrm-test.itheima.net/api/sys/login"
        login_header = {"Content-Type": "application/json"}
        login_data = {"mobile": "13800000002","password": "123456"}
        login_resp = requests.post(url=login_url,headers=login_header,json=login_data)
        print("login_resp=",login_resp.json())
        #断言
        assert login_resp.status_code == 200
        assert login_resp.json().get("success") == True
        assert login_resp.json().get("code") == 10000
        assert login_resp.json().get("message") == '操作成功！'


    #mobile 错误
    def test_mobile_error(self):
        # 设置url ,header,body,获取响应结果
        login_url = "http://ihrm-test.itheima.net/api/sys/login"
        login_header = {"Content-Type": "application/json"}
        login_data = {"mobile": "13810000002", "password": "123456"}
        login_resp = requests.post(url=login_url, headers=login_header, json=login_data)
        print("login_resp=", login_resp.json())
        # 断言
        assert login_resp.status_code == 200
        assert login_resp.json().get("success") == False
        assert login_resp.json().get("code") == 20001
        assert login_resp.json().get("message") == '用户名或密码错误'

    #password错误
    def test_password_error(self):
        # 设置url ,header,body,获取响应结果
        login_url = "http://ihrm-test.itheima.net/api/sys/login"
        login_header = {"Content-Type": "application/json"}
        login_data = {"mobile": "13800000002", "password": "123956"}
        login_resp = requests.post(url=login_url, headers=login_header, json=login_data)
        print("login_resp=", login_resp.json())
        # 断言
        assert login_resp.status_code == 200
        assert login_resp.json().get("success") == False
        assert login_resp.json().get("code") == 20001
        assert login_resp.json().get("message") == '用户名或密码错误'

