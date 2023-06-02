import requests


class TestTpshopLogin:

    # 登录成功
    '''
    def test_login_success(self):
        session = requests.session()
        # 发送验证码
        verify_url = "http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify"
        session.get(verify_url)
        # 登录操作
        login_url = "http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login"
        login_header = {"Content-Type": "application/x-www-form-urlencoded"}
        login_data = {"username": "13012345678", "password": "123456", "verify_code": "8888"}
        login_resp = session.post(url=login_url, headers=login_header, data=login_data)
        print("login_resp=", login_resp.json())
        # 断言
        assert login_resp.status_code == 200
        assert login_resp.json().get("status") == 1
        assert login_resp.json().get("msg") == '登陆成功'

        '''

    # 账号不存在
    def test_username_error(self):
        session = requests.session()
        # 发送验证码
        verify_url = "http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify"
        session.get(verify_url)
        # 登录操作
        login_url = "http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login"
        login_header = {"Content-Type": "application/x-www-form-urlencoded"}
        login_data = {"username": "1301222345678", "password": "123456", "verify_code": "8888"}
        login_resp = session.post(url=login_url, headers=login_header, data=login_data)
        print("login_resp=", login_resp.json())
        # 断言
        assert login_resp.status_code == 200
        assert login_resp.json().get("status") == -1
        assert login_resp.json().get("msg") == '账号不存在!'

    # 密码错误
    def test_password_error(self):
        session = requests.session()
        # 发送验证码
        verify_url = "http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=verify"
        session.get(verify_url)
        # 登录操作
        login_url = "http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login"
        login_header = {"Content-Type": "application/x-www-form-urlencoded"}
        login_data = {"username": "13012345678", "password": "1223456", "verify_code": "8888"}
        login_resp = session.post(url=login_url, headers=login_header, data=login_data)
        print("login_resp=", login_resp.json())
        # 断言
        assert login_resp.status_code == 200
        assert login_resp.json().get("status") == -2
        assert login_resp.json().get("msg") == '密码错误!'


